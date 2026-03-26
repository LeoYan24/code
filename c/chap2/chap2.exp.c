#include<stdio.h>
#include<stdlib.h>
#include<time.h>

typedef struct node{
    int id;//编号
    int power;//电量，10-100
    struct node* next;
} node;

#define MAX_n 1000
#define MAX_m 100

node* createCircularList(int n);
void freeList(node* head, int n);
void printRemaining(node* start, int count);

int main(){
    int n,k,m;//设备总数(1-1000)；起始遍历位置(1-n)；遍历步长(1-100)
    srand((unsigned int)time(NULL)); 

    printf("Please enter the total number of devices n (1~1000): ");
    if (scanf("%d", &n) != 1 || n < 1 || n > 1000){
        printf("Error: n must within 1 and 1000!\n");
        return 1;
    }
    printf("Please enter the initial position k (1~%d): ", n);
    if (scanf("%d", &k) != 1 || k < 1 || k > n){
        printf("Error: k must within 1 and n !\n");
        return 1;
    }
    printf("Please enter the basic step size m (1~100): ");
    if (scanf("%d", &m) != 1 || m < 1 || m > 100){
        printf("Error: m must within 1 and 100!\n");
        return 1;
    }

    int eliminated[1000];//淘汰设备
    int remain_cnt = n;//剩余设备数
    int round = 0;//轮数

    node* head = createCircularList(n);
    if (head == NULL) {
        printf("Failed to create linked list!\n");
        return 1;
    }

    node* current = head;
    for (int i = 1; i < k; i++) {
        current = current->next;
    }

    printf("Initial devices queue:\n");
    printRemaining(head,n);

    while( remain_cnt > 1 ){
        round++;
        int step = m + (100 - current->power) / 10;
        node* target = current;
        node* targetPrev = NULL;//记录前驱
        for (int i = 1; i < step; i++) {
            targetPrev = target;
            target = target->next;
        }

        printf("\n Round %d eliminated the device with ID %d.\n",round ,target->id);
        targetPrev->next = target->next;
        if (target == head) {
            head = target->next;
        }

        current = target->next;
        eliminated[round-1] = target->id;

        free(target);
        remain_cnt--;
        
        printf("Remaining devices after elimination:\n");
        printRemaining(current,remain_cnt);
    }

    printf("The core inspection device ID: %d (power: %d%%)\n", current->id, current->power);

    printf("Core device inspection path (reverse order of elimination): ");
    for (int i = n - 2; i >= 0; i--){
        printf("%d ", eliminated[i]);
    }

    free(current);
    return 0;
}

node* createCircularList(int n){
    if(n <= 0) return NULL;
    node *head = NULL, *tail = NULL;
    for(int i = 1; i <= n; i++){
        node* newNode = (node*)malloc(sizeof(node));
        if(!newNode){
            printf("Failed to create linked list!\n");
            exit(1);
        }
        newNode->id = i;
        newNode->power = rand() % 90 + 10;// 随机生成10~100
        newNode->next = NULL;
        
        if(head == NULL){
            head = newNode;
            tail = newNode;
        }else{
            tail->next = newNode;
            tail = newNode;
        }
    }
    tail->next = head;//环状结构
    return head;
}

void freeList(node* head, int n){
    if(head == NULL) return;
    node* curr = head;
    for(int i = 0; i < n; i++){
        node* temp = curr;
        curr = curr->next;
        free(temp);
    }
}

void printRemaining(node* start, int count){
    if(start == NULL || count == 0){
        printf("[]\n");
        return;
    }
    node* curr = start;
    printf("[");
    for(int i = 0; i < count; i++){
        printf("%d", curr->id);
        if(i < count - 1) printf(", ");
        curr = curr->next;
    }
    printf("]\n");
}