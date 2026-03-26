#include<stdio.h>
#include<stdlib.h>

typedef struct node{
    int data;
    struct node *next;
} linknode, *link;

link ListSort(link la){
    if (la == NULL || la->next == NULL) return la;

    link p = la;
    int swapped = 1;
    int temp;

    while( swapped == 1 ){  
        swapped = 0;
        p = la;
        while( p ){
            if( p->data > p->next->data ){
                temp = p->data;
                p->data = p->next->data;
                p->next->data = temp;
                swapped = 1;
            }
            p = p->next;
        }
    }

    return la;
}