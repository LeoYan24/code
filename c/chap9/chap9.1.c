#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int key;              // 关键字（用于排序）
    int otherinfo;   // 其他相关信息
    struct node *next;    // 指向下一个结点的指针
} node, *pointer;

void selectsort(pointer h) {
    if (h == NULL || h->next == NULL) {
        return;
    }

    pointer p = h->next;  // p指向第一个实际存储数据的结点

    while (p != NULL) {
        pointer minNode = p;
        pointer q = p->next;

        while (q != NULL) {
            if (q->key < minNode->key) {
                minNode = q;
            }
            q = q->next;
        }

        // 若找到的最小值结点不是p本身，则交换这两个结点的数据域
        if (minNode != p) {
            int tempKey = p->key;
            p->key = minNode->key;
            minNode->key = tempKey;

            int tempInfo = p->otherinfo;
            p->otherinfo = minNode->otherinfo;
            minNode->otherinfo = tempInfo;
        }

        p = p->next; // p指向下一轮待排序序列的第一个结点
    }
}