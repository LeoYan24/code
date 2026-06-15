#include<stdio.h>
#include<stdlib.h>

typedef struct node{
    int data;
    struct node *left,*right;
}BiTNode,*BiTree;

void Delete(BiTree root, BiTree p, BiTree fp) {
    if (!root || !p || !fp) return;

    //情况一：p没有左孩子
    if (!p->left) fp->left = p->right; 
    //情况二：p没有右孩子，但有左孩子
    else if (!p->right) fp->left = p->left;
    //情况三:p既有左孩子又有右孩子
    else {
        BiTree s = p->left;
        while (s->right) {
            s = s->right;
        }
        s->right = p->right;//直接把p的右子树嫁接到左子树的末尾
        fp->left = p->left; 
    }
    free(p);
}