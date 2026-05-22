#include <stdio.h>

#define maxvtxnum 100   // 假定图的最大顶点数为100（可根据实际情况修改）

typedef int adjmatrix[maxvtxnum][maxvtxnum];

/**
 * 求邻接矩阵 A 的传递闭包矩阵 C
 * @param A 输入的邻接矩阵 (有向图)
 * @param C 输出的传递闭包矩阵
 * @param n 图的实际顶点数
 */

void change ( adjmatrix A, adjmatrix C, int n ) {
    int i, j, k;
    
    //初始化
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            C[i][j] = A[i][j];
        }
        C[i][i] = 1; 
    }

    //Warshall
    for (k = 0; k < n; k++) {           //中间顶点k
        for (i = 0; i < n; i++) {       //起点i
            if (C[i][k] == 1) {
                for (j = 0; j < n; j++) {//终点j
                    if (C[k][j] == 1) {
                        C[i][j] = 1;
                    }
                }
            }
        }
    }
}