#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    int bf;
    struct node *left, *right;
} BiTNode, *BSTree;

int Height(BSTree t) {
    if (t == NULL) return 0;

    if (t->bf == 1) return Height(t->left) + 1;
    else if (t->bf == -1)  return Height(t->right) + 1;
    else return Height(t->left) + 1;
}