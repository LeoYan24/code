#include<stdio.h>
#include<stdlib.h>

typedef struct node{
    int data;
    struct node *next;
} linknode, *link;

link Union(link la,link lb){
    link head = NULL;
    link p=la,q=lb;
    link temp;

    while(p && q){
        if(p->data <= q->data){//将p->data头插入至head
            temp = p->next;
            p->next = head;
            head = p;
            p = temp;
        }else{//将q->data头插入至head
            temp = q->next;
            q->next = head;
            head = q;
            q = temp;
        }
    }

    while(p){//如果p剩余
        temp = p->next;
        p->next = head;
        head = p;
        p = temp;
    }

    while(q){//如果q剩余
        temp = q->next;
        q->next = head;
        head = q;
        q = temp;
    }

    return head;
}