#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct {
    int row, col;
    double val;
} Triple;
typedef struct {
    int rows, cols, num;
    Triple *data;
} SparseMatrix;

SparseMatrix readMatrix(void);
SparseMatrix multiply(const SparseMatrix *A, const SparseMatrix *B);
int compareTriple(const void *a, const void *b);
SparseMatrix mergeDuplicates(SparseMatrix *mat);
void freeMatrix(SparseMatrix *mat);

int main(){
    system("chcp 65001 > nul"); 
    SparseMatrix user=readMatrix(),item=readMatrix();
    if( user.cols != item.rows ){
        printf("错误：用户-物品矩阵的列数必须等于物品相似度矩阵的行数！\n");
        freeMatrix(&user);
        freeMatrix(&item);
        return 1;
    }

    SparseMatrix prod = multiply(&user, &item);
    SparseMatrix merged = mergeDuplicates(&prod);
    freeMatrix(&prod);
    printf("推荐权重矩阵（%d行 × %d列，%d个非零元）：\n", merged.rows, merged.cols, merged.num);
    for( int i = 0; i < merged.num ; i++ ){
        printf("用户%d-产品%d：推荐权重：%.2lf\n", merged.data[i].row, merged.data[i].col, merged.data[i].val);
    }

    freeMatrix(&user);
    freeMatrix(&item);
    freeMatrix(&merged);
    return 0;
}

SparseMatrix readMatrix(void){
    SparseMatrix mat;
    scanf("%d%d%d",&mat.rows,&mat.cols,&mat.num);
    mat.data = (Triple*)malloc(mat.num * sizeof(Triple));
    if (mat.data == NULL) {
        fprintf(stderr, "内存分配失败\n");
        exit(1);
    }
    for( int i=0 ; i < mat.num ; i++ ){
        scanf("%d%d%lf",&mat.data[i].row,&mat.data[i].col,&mat.data[i].val);
    }
    return mat;
}

SparseMatrix multiply(const SparseMatrix *A, const SparseMatrix *B) {
    SparseMatrix C;
    C.rows = A->rows;
    C.cols = B->cols;
    C.num = 0;
    int maxPossible = A->num * B->num;
    C.data = (Triple*)malloc(maxPossible * sizeof(Triple));
    if (C.data == NULL) {
        fprintf(stderr, "内存分配失败\n");
        exit(1);
    }

    for (int i = 0; i < A->num; i++) {
        int k = A->data[i].col;
        for (int j = 0; j < B->num; j++) {
            if (B->data[j].row == k) {
                C.data[C.num].row = A->data[i].row;
                C.data[C.num].col = B->data[j].col;
                C.data[C.num].val = A->data[i].val * B->data[j].val;
                C.num++;
            }
        }
    }
    C.data = (Triple*)realloc(C.data, C.num * sizeof(Triple));
    return C;
}

// 用于qsort的比较函数：先按行，再按列
int compareTriple(const void *a, const void *b) {
    const Triple *ta = (const Triple*)a;
    const Triple *tb = (const Triple*)b;
    if (ta->row != tb->row) return ta->row - tb->row;
    return ta->col - tb->col;
}

SparseMatrix mergeDuplicates(SparseMatrix *mat) {
    if (mat->num == 0) {
        SparseMatrix empty = {mat->rows, mat->cols, 0, NULL};
        return empty;
    }

    qsort(mat->data, mat->num, sizeof(Triple), compareTriple);

    Triple *merged = (Triple*)malloc(mat->num * sizeof(Triple));
    if (merged == NULL) {
        fprintf(stderr, "内存分配失败\n");
        exit(1);
    }

    int cnt = 0;
    merged[0] = mat->data[0];
    for (int i = 1; i < mat->num; i++) {
        if (mat->data[i].row == merged[cnt].row &&
            mat->data[i].col == merged[cnt].col) {
            merged[cnt].val += mat->data[i].val;
        } else {
            cnt++;
            merged[cnt] = mat->data[i];
        }
    }
    cnt++;

    SparseMatrix result;
    result.rows = mat->rows;
    result.cols = mat->cols;
    result.num = cnt;
    result.data = (Triple*)malloc(cnt * sizeof(Triple));
    if (result.data == NULL) {
        fprintf(stderr, "内存分配失败\n");
        exit(1);
    }
    memcpy(result.data, merged, cnt * sizeof(Triple));
    free(merged);
    return result;
}

void freeMatrix(SparseMatrix *mat){
    if (mat->data) {
        free(mat->data);
        mat->data = NULL;
    }
    mat->num = 0;
}