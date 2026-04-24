#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#define MAX_SYMBOLS 256
#define BUF_SIZE    1024

typedef struct Node {
    int symbol;
    struct Node *left, *right;
} Node;
typedef struct {
    struct {
        Node *node;
        uint64_t freq;
    } *array;
    int size;
    int capacity;
} MinHeap;
typedef struct{
    FILE *fp;
    unsigned char buf;
    int pos;
} BitReader;

MinHeap* create_min_heap(int capacity);
void swap_heap_elements(MinHeap *heap, int i, int j);
void heapify(MinHeap *heap, int idx);
void insert_min_heap(MinHeap *heap, Node *node, uint64_t freq);
void extract_min(MinHeap *heap, Node **node, uint64_t *freq);
void free_min_heap(MinHeap *heap);
Node* rebuild_huffman_tree(uint64_t *freq);
void free_tree(Node *root);
BitReader* bit_reader_create(FILE *fp);
int bit_reader_read(BitReader *br);

int main(int argc, char *argv[]){
    system("chcp 65001 > nul"); 
    char input_path[512], output_dir[512] = "";

    if (argc >= 2) {
        strncpy(input_path, argv[1], sizeof(input_path)-1);
        input_path[sizeof(input_path)-1] = '\0';
        if (argc == 3) {
            strncpy(output_dir, argv[2], sizeof(output_dir)-1);
            output_dir[sizeof(output_dir)-1] = '\0';
        }
    } else {
        printf("输入要解压的压缩文件名：");
        if (fgets(input_path, sizeof(input_path), stdin) == NULL) {
            fprintf(stderr, "读取文件名失败。\n");
            return 1;
        }
        input_path[strcspn(input_path, "\n")] = '\0';

        printf("输入解压输出目录（直接回车则解压到当前目录）：");
        if (fgets(output_dir, sizeof(output_dir), stdin) == NULL) {
            fprintf(stderr, "读取目录失败。\n");
            return 1;
        }
        output_dir[strcspn(output_dir, "\n")] = '\0';
    }

    FILE *fin = fopen(input_path, "rb");
    if (!fin) {
        fprintf(stderr, "无法打开压缩文件 %s: %s\n", input_path, strerror(errno));
        return 1;
    }

    /* 验证魔数 */
    char magic[4];
    if (fread(magic, 1, 4, fin) != 4 || memcmp(magic, "HUFF", 4) != 0) {
        fprintf(stderr, "文件格式错误，不是有效的 Huffman 压缩文件。\n");
        fclose(fin);
        return 1;
    }

    /* 读取原文件名 */
    uint16_t name_len;
    if (fread(&name_len, sizeof(name_len), 1, fin) != 1) {
        fprintf(stderr, "读取文件名长度失败。\n");
        fclose(fin);
        return 1;
    }
    char original_name[1024];
    if (name_len >= sizeof(original_name)) {
        fprintf(stderr, "文件名过长。\n");
        fclose(fin);
        return 1;
    }
    if (fread(original_name, 1, name_len, fin) != name_len) {
        fprintf(stderr, "读取文件名失败。\n");
        fclose(fin);
        return 1;
    }
    original_name[name_len] = '\0';

    /* 读取原始文件大小 */
    uint64_t original_size;
    if (fread(&original_size, sizeof(original_size), 1, fin) != 1) {
        fprintf(stderr, "读取原始文件大小失败。\n");
        fclose(fin);
        return 1;
    }

    /* 读取频率表 */
    uint64_t freq[MAX_SYMBOLS];
    if (fread(freq, sizeof(uint64_t), MAX_SYMBOLS, fin) != MAX_SYMBOLS) {
        fprintf(stderr, "读取频率表失败。\n");
        fclose(fin);
        return 1;
    }

    /* 重建哈夫曼树 */
    Node *root = rebuild_huffman_tree(freq);
    if (!root) {
        fprintf(stderr, "重建哈夫曼树失败。\n");
        fclose(fin);
        return 1;
    }

    /* 构造输出文件路径 */
    char output_path[2048];
    if (strlen(output_dir) > 0) {
        int len = strlen(output_dir);
        if (output_dir[len-1] != '/' && output_dir[len-1] != '\\')
            snprintf(output_path, sizeof(output_path), "%s/%s", output_dir, original_name);
        else
            snprintf(output_path, sizeof(output_path), "%s%s", output_dir, original_name);
    } else {
        strncpy(output_path, original_name, sizeof(output_path)-1);
        output_path[sizeof(output_path)-1] = '\0';
    }

    FILE *fout = fopen(output_path, "wb");
    if (!fout) {
        fprintf(stderr, "无法创建输出文件 %s: %s\n", output_path, strerror(errno));
        fclose(fin);
        free_tree(root);
        return 1;
    }

    /* 解码并写入 */
    BitReader *br = bit_reader_create(fin);
    if (br == NULL) {
        fprintf(stderr, "内存不足。\n");
        fclose(fin); fclose(fout);
        free_tree(root);
        return 1;
    }

    uint64_t bytes_written = 0;
    Node *current = root;
    int error_occurred = 0;

    while (bytes_written < original_size) {
        int bit = bit_reader_read(br);
        if (bit < 0) {
            fprintf(stderr, "压缩数据意外结束。\n");
            error_occurred = 1;
            break;
        }
        current = (bit == 0) ? current->left : current->right;

        if (!current->left && !current->right) {
            fputc(current->symbol, fout);
            bytes_written++;
            current = root;
        }
    }

    /* 清理 */
    free(br);
    fclose(fin);
    fclose(fout);
    free_tree(root);

    if (!error_occurred && bytes_written == original_size)
        printf("解压完成：%s -> %s\n", input_path, output_path);
    else
        fprintf(stderr, "解压过程可能出错，输出文件可能不完整。\n");

    return 0;
}

MinHeap* create_min_heap(int capacity){
    MinHeap *heap = (MinHeap*)malloc(sizeof(MinHeap));
    heap->capacity = capacity;
    heap->size = 0;
    heap->array = (typeof(heap->array))malloc(capacity * sizeof(*(heap->array)));
    return heap;
}

void swap_heap_elements(MinHeap *heap, int i, int j){
    Node *tn = heap->array[i].node;
    uint64_t tf = heap->array[i].freq;
    heap->array[i].node = heap->array[j].node;
    heap->array[i].freq = heap->array[j].freq;
    heap->array[j].node = tn;
    heap->array[j].freq = tf;
}

void heapify(MinHeap *heap, int idx){
    int smallest = idx;
    int left = 2 * idx + 1;
    int right = 2 * idx + 2;
    if (left < heap->size && heap->array[left].freq < heap->array[smallest].freq)
        smallest = left;
    if (right < heap->size && heap->array[right].freq < heap->array[smallest].freq)
        smallest = right;
    if (smallest != idx) {
        swap_heap_elements(heap, idx, smallest);
        heapify(heap, smallest);
    }
}

void insert_min_heap(MinHeap *heap, Node *node, uint64_t freq){
    int i = heap->size++;
    heap->array[i].node = node;
    heap->array[i].freq = freq;
    while (i > 0 && heap->array[i].freq < heap->array[(i - 1) / 2].freq) {
        swap_heap_elements(heap, i, (i - 1) / 2);
        i = (i - 1) / 2;
    }
}

void extract_min(MinHeap *heap, Node **node, uint64_t *freq){
    *node = heap->array[0].node;
    *freq = heap->array[0].freq;
    heap->array[0] = heap->array[--heap->size];
    heapify(heap, 0);
}

void free_min_heap(MinHeap *heap){
    if (heap) {
        free(heap->array);
        free(heap);
    }
}

Node* rebuild_huffman_tree(uint64_t *freq){
    MinHeap *heap = create_min_heap(MAX_SYMBOLS);
    for (int i = 0; i < MAX_SYMBOLS; i++) {
        if (freq[i] > 0) {
            Node *node = (Node*)malloc(sizeof(Node));
            node->symbol = i;
            node->left = node->right = NULL;
            insert_min_heap(heap, node, freq[i]);
        }
    }
    if (heap->size == 0) {
        free_min_heap(heap);
        return NULL;
    }
    while (heap->size > 1) {
        Node *left, *right;
        uint64_t fl, fr;
        extract_min(heap, &left, &fl);
        extract_min(heap, &right, &fr);
        Node *parent = (Node*)malloc(sizeof(Node));
        parent->symbol = -1;
        parent->left = left;
        parent->right = right;
        insert_min_heap(heap, parent, fl + fr);
    }
    Node *root = heap->array[0].node;
    free_min_heap(heap);
    return root;
}

void free_tree(Node *root){
    if (root) {
        free_tree(root->left);
        free_tree(root->right);
        free(root);
    }
}

BitReader* bit_reader_create(FILE *fp){
    BitReader *br = (BitReader*)malloc(sizeof(BitReader));
    br->fp = fp;
    br->buf = 0;
    br->pos = 0;
    return br;
}

int bit_reader_read(BitReader *br){
    if (br->pos == 0) {
        size_t ret = fread(&br->buf, 1, 1, br->fp);
        if (ret != 1) return -1;   // EOF 或读取错误
        br->pos = 8;
    }
    int bit = (br->buf >> 7) & 1;
    br->buf <<= 1;
    br->pos--;
    return bit;
}