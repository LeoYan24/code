#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTEX_NUM 20 

typedef struct {
    int vexs[MAX_VERTEX_NUM];                 // 顶点表 (存顶点编号 v1~v6 即 1~6)
    int arcs[MAX_VERTEX_NUM][MAX_VERTEX_NUM]; // 邻接矩阵 (0表示无边，1表示有边)
    int vexnum, arcnum;                       // 图的当前顶点数和边数
} Mgraph;

typedef struct ArcNode {
    int adjvex;               // 该边所指向的顶点在顶点表中的下标
    struct ArcNode *nextarc;  // 指向下一条边的指针
} ArcNode;

typedef struct VNode {
    int data;                 // 顶点信息 (v1~v6 即 1~6)
    ArcNode *firstarc;        // 指向第一条依附该顶点的边的指针
} VNode, AdjList[MAX_VERTEX_NUM];

typedef struct {
    AdjList vertices;         // 顶点表数组
    int vexnum, arcnum;       // 图的当前顶点数和边数
} Agraph;

void convert(Mgraph g, Agraph *G) {
    int i, j;
    ArcNode *p;
    
    G->vexnum = g.vexnum;
    G->arcnum = g.arcnum;

    for (i = 0; i < g.vexnum; i++) {
        G->vertices[i].data = g.vexs[i];
        G->vertices[i].firstarc = NULL;
    }

    for (i = 0; i < g.vexnum; i++) {
        for (j = g.vexnum - 1; j >= 0; j--) {
            if (g.arcs[i][j] != 0) {//存在边
                p = (ArcNode *)malloc(sizeof(ArcNode));
                p->adjvex = j;
                p->nextarc = G->vertices[i].firstarc;
                G->vertices[i].firstarc = p;
            }
        }
    }
}