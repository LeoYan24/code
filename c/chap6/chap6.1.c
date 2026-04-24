#include <stdbool.h>
#include<stdlib.h>

typedef struct BiTNode {
    char data;
    struct BiTNode *lchild, *rchild;
} BiTNode, *BiTree;

bool Similar(BiTree p,BiTree q){
    if( p == NULL && q == NULL ) return true;
    else if( p == NULL || q == NULL ) return false;
    else return Similar( p->lchild , q->lchild ) && Similar( p->rchild , q->rchild );
}