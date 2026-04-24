#include<stdlib.h>

typedef struct CSNode {
    int data;
    struct CSNode *firstchild;
    struct CSNode *nextsibling;
} CSNode, *CSTree;

int degree(CSTree root){
    if( root == NULL ) return 0;
    int maxDegree = 0;
    int curDegree = 0;
    CSTree p = root->firstchild;

    while( p ){
        curDegree++;
        int subDegree = degree(p);
        if( subDegree > maxDegree ) maxDegree = subDegree;
        p = p->nextsibling;
    }

    if( curDegree > maxDegree ) return curDegree;
    else return maxDegree;
}