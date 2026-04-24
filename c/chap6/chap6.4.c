#include<stdlib.h>

typedef struct CSNode {
    int data;
    struct CSNode *firstchild;
    struct CSNode *nextsibling;
} CSNode, *CSTree;

int Count(CSTree root){
    if( root == NULL ) return 0;
    if (root->firstchild == NULL) return 1 + Count(root->nextsibling);
    else return Count(root->firstchild) + Count(root->nextsibling);
}