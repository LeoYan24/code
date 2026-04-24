#include <stdbool.h>
#include<stdlib.h>

#define MAXSIZE 1000

typedef struct BiTNode {
    char data;
    struct BiTNode *lchild, *rchild;
} BiTNode, *BiTree;

typedef struct {
    BiTree data[MAXSIZE];
    int front, rear;
} SqQueue;

void InitQueue(SqQueue *Q){
    Q->front = 0;
    Q->rear = 0;
}
bool IsEmpty(SqQueue Q){ return Q.front == Q.rear; }
bool EnQueue(SqQueue *Q, BiTree e){
    if ((Q->rear + 1) % MAXSIZE == Q->front) return false;
    Q->data[Q->rear] = e;
    Q->rear = (Q->rear + 1) % MAXSIZE;
    return true;
}
bool DeQueue(SqQueue *Q, BiTree *e){
    if (IsEmpty(*Q)) return false;
    *e = Q->data[Q->front];
    Q->front = (Q->front + 1) % MAXSIZE;
    return true;
}

bool JudgeComplete(BiTree root){
    if (root == NULL) return true;

    SqQueue Q;
    InitQueue(&Q);
    EnQueue(&Q, root);
    bool metNull = false;

    while(!IsEmpty(Q)){
        BiTree p;
        DeQueue(&Q, &p);
        if(p == NULL) {
            metNull = true;//遇到空结点，后面应全为空
        }else {
            if(metNull) return false;//之前有空结点，现在却遇到非空，不是完全二叉树
            EnQueue(&Q, p->lchild);
            EnQueue(&Q, p->rchild);
        }
    }
    return true;
}