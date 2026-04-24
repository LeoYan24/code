#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#define MAX_SYMBOLS 256       // 字节值 0~255
#define BUF_SIZE    1024      // 每次统计读取的块大小
#define CODE_BYTES  32 

typedef struct Node {
    int symbol;               // 叶子节点：0~255；内部节点：-1
    uint64_t freq;
    struct Node *left, *right;
} Node;
typedef struct {
    Node **array;
    int size;
    int capacity;
} MinHeap;
typedef struct {
    unsigned char code[CODE_BYTES];
    int len;
} CodeTable;
typedef struct {
    FILE *fp;
    unsigned char buf;
    int pos;   // 当前位位置 0~7
} BitWriter;

MinHeap* create_min_heap(int capacity);
void swap_nodes(Node **a, Node **b);
void heapify(MinHeap *heap, int idx);
void insert_min_heap(MinHeap *heap, Node *node);
Node* extract_min(MinHeap *heap);
void free_min_heap(MinHeap *heap);
Node* build_huffman_tree(uint64_t *freq);
void generate_codes(Node *root, unsigned char *arr, int depth, CodeTable *table);
void free_tree(Node *root);
BitWriter* bit_writer_create(FILE *fp);
void bit_writer_write(BitWriter *bw, const CodeTable *table, int symbol);
void bit_writer_flush(BitWriter *bw);

int main(int argc, char *argv[]){
    system("chcp 65001 > nul"); 
    char input_path[512], output_path[512];

    if (argc == 3) {
        strncpy(input_path, argv[1], sizeof(input_path)-1);
        input_path[sizeof(input_path)-1] = '\0';
        strncpy(output_path, argv[2], sizeof(output_path)-1);
        output_path[sizeof(output_path)-1] = '\0';
    } else {
        printf("输入要压缩的源文件名：");
        if (fgets(input_path, sizeof(input_path), stdin) == NULL) {
            fprintf(stderr, "读取输入文件名失败。\n");
            return 1;
        }
        input_path[strcspn(input_path, "\n")] = '\0';

        printf("输入压缩后的文件名（如 output.huff）：");
        if (fgets(output_path, sizeof(output_path), stdin) == NULL) {
            fprintf(stderr, "读取输出文件名失败。\n");
            return 1;
        }
        output_path[strcspn(output_path, "\n")] = '\0';
    }

    FILE *fin = fopen(input_path, "rb");
    if (!fin) {
        fprintf(stderr, "无法打开输入文件 %s: %s\n", input_path, strerror(errno));
        return 1;
    }

    /* 第一步：统计频率 */
    uint64_t freq[MAX_SYMBOLS] = {0};
    unsigned char buf[BUF_SIZE];
    size_t bytes_read;
    uint64_t total_bytes = 0;

    while ((bytes_read = fread(buf, 1, BUF_SIZE, fin)) > 0) {
        for (size_t i = 0; i < bytes_read; i++)
            freq[buf[i]]++;
        total_bytes += bytes_read;
    }

    if (total_bytes == 0) {
        fprintf(stderr, "输入文件为空，无法压缩。\n");
        fclose(fin);
        return 1;
    }

    /* 第二步：构建哈夫曼树 */
    Node *root = build_huffman_tree(freq);
    if (!root) {
        fprintf(stderr, "构建哈夫曼树失败。\n");
        fclose(fin);
        return 1;
    }

    /* 第三步：生成编码表 */
    CodeTable code_table[MAX_SYMBOLS];
    unsigned char arr[MAX_SYMBOLS];
    generate_codes(root, arr, 0, code_table);

    /* 第四步：打开输出文件 */
    FILE *fout = fopen(output_path, "wb");
    if (!fout) {
        fprintf(stderr, "无法创建压缩文件 %s: %s\n", output_path, strerror(errno));
        fclose(fin);
        free_tree(root);
        return 1;
    }

    /* 写入头部 */
    fwrite("HUFF", 1, 4, fout);

    const char *filename = strrchr(input_path, '/');
    if (!filename) filename = strrchr(input_path, '\\');
    filename = filename ? filename + 1 : input_path;
    uint16_t name_len = (uint16_t)strlen(filename);
    fwrite(&name_len, sizeof(name_len), 1, fout);
    fwrite(filename, 1, name_len, fout);

    fwrite(&total_bytes, sizeof(total_bytes), 1, fout);
    fwrite(freq, sizeof(uint64_t), MAX_SYMBOLS, fout);

    /* 第五步：编码并写入数据 */
    rewind(fin);
    BitWriter *bw = bit_writer_create(fout);
    if (bw == NULL) {
        fprintf(stderr, "内存不足。\n");
        fclose(fin); fclose(fout);
        free_tree(root);
        return 1;
    }

    while ((bytes_read = fread(buf, 1, BUF_SIZE, fin)) > 0) {
        for (size_t i = 0; i < bytes_read; i++) {
            bit_writer_write(bw, code_table, buf[i]);
        }
    }
    bit_writer_flush(bw);

    /* 清理资源 */
    free(bw);
    fclose(fin);
    fclose(fout);
    free_tree(root);

    printf("压缩完成：%s -> %s\n", input_path, output_path);
    return 0;
}

MinHeap* create_min_heap(int capacity){
    MinHeap *heap = (MinHeap*)malloc(sizeof(MinHeap));
    heap->capacity = capacity;
    heap->size = 0;
    heap->array = (Node**)malloc(capacity * sizeof(Node*));
    return heap;
}
void swap_nodes(Node **a, Node **b){
    Node *t = *a;
    *a = *b;
    *b = t;
}
void heapify(MinHeap *heap, int idx){
    int smallest = idx;
    int left = 2 * idx + 1;
    int right = 2 * idx + 2;
    if (left < heap->size && heap->array[left]->freq < heap->array[smallest]->freq)
        smallest = left;
    if (right < heap->size && heap->array[right]->freq < heap->array[smallest]->freq)
        smallest = right;
    if (smallest != idx) {
        swap_nodes(&heap->array[idx], &heap->array[smallest]);
        heapify(heap, smallest);
    }
}
void insert_min_heap(MinHeap *heap, Node *node){
    int i = heap->size++;
    heap->array[i] = node;
    while (i > 0 && heap->array[i]->freq < heap->array[(i - 1) / 2]->freq) {
        swap_nodes(&heap->array[i], &heap->array[(i - 1) / 2]);
        i = (i - 1) / 2;
    }
}
Node* extract_min(MinHeap *heap){
    if (heap->size == 0) return NULL;
    Node *min = heap->array[0];
    heap->array[0] = heap->array[--heap->size];
    heapify(heap, 0);
    return min;
}
void free_min_heap(MinHeap *heap){
    if (heap) {
        free(heap->array);
        free(heap);
    }
}
Node* build_huffman_tree(uint64_t *freq){
    MinHeap *heap = create_min_heap(MAX_SYMBOLS);
    for (int i = 0; i < MAX_SYMBOLS; i++) {
        if (freq[i] > 0) {
            Node *node = (Node*)malloc(sizeof(Node));
            node->symbol = i;
            node->freq = freq[i];
            node->left = node->right = NULL;
            insert_min_heap(heap, node);
        }
    }
    if (heap->size == 0) {
        free_min_heap(heap);
        return NULL;
    }
    while (heap->size > 1) {
        Node *left = extract_min(heap);
        Node *right = extract_min(heap);
        Node *parent = (Node*)malloc(sizeof(Node));
        parent->symbol = -1;
        parent->freq = left->freq + right->freq;
        parent->left = left;
        parent->right = right;
        insert_min_heap(heap, parent);
    }
    Node *root = extract_min(heap);
    free_min_heap(heap);
    return root;
}
void generate_codes(Node *root, unsigned char *arr, int depth, CodeTable *table){
    if (root->left) {
        arr[depth] = 0;
        generate_codes(root->left, arr, depth + 1, table);
    }
    if (root->right) {
        arr[depth] = 1;
        generate_codes(root->right, arr, depth + 1, table);
    }
    if (!root->left && !root->right) {
        memset(table[root->symbol].code, 0, sizeof(table[root->symbol].code));
        for (int i = 0; i < depth; i++) {
            if (arr[i])
                table[root->symbol].code[i / 8] |= (1 << (7 - (i % 8)));
        }
        table[root->symbol].len = depth;
    }
}
void free_tree(Node *root){
    if (root) {
        free_tree(root->left);
        free_tree(root->right);
        free(root);
    }
}
BitWriter* bit_writer_create(FILE *fp){
    BitWriter *bw = (BitWriter*)malloc(sizeof(BitWriter));
    bw->fp = fp;
    bw->buf = 0;
    bw->pos = 0;
    return bw;
}
void bit_writer_write(BitWriter *bw, const CodeTable *table, int symbol){
    const unsigned char *code = table[symbol].code;
    int len = table[symbol].len;
    for (int i = 0; i < len; i++) {
        int bit = (code[i / 8] >> (7 - (i % 8))) & 1;
        if (bit)
            bw->buf |= (1 << (7 - bw->pos));
        bw->pos++;
        if (bw->pos == 8) {
            fwrite(&bw->buf, 1, 1, bw->fp);
            bw->buf = 0;
            bw->pos = 0;
        }
    }
}
void bit_writer_flush(BitWriter *bw){
    if (bw->pos > 0) {
        fwrite(&bw->buf, 1, 1, bw->fp);
        bw->buf = 0;
        bw->pos = 0;
    }
}