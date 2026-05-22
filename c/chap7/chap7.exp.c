#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

// 队列结构（用于BFS）
typedef struct {
    int *data;
    int front, rear, size, capacity;
} Queue;

Queue* createQueue(int cap) {
    Queue *q = (Queue*)malloc(sizeof(Queue));
    q->data = (int*)malloc(cap * sizeof(int));
    q->front = q->rear = 0;
    q->size = 0;
    q->capacity = cap;
    return q;
}

void enqueue(Queue *q, int val) {
    if (q->size == q->capacity) return;
    q->data[q->rear] = val;
    q->rear = (q->rear + 1) % q->capacity;
    q->size++;
}

int dequeue(Queue *q) {
    if (q->size == 0) return -1;
    int val = q->data[q->front];
    q->front = (q->front + 1) % q->capacity;
    q->size--;
    return val;
}

bool isEmpty(Queue *q) {
    return q->size == 0;
}

void freeQueue(Queue *q) {
    free(q->data);
    free(q);
}

// 从顶点s出发BFS计算可达顶点数（包括自身）
int bfsReachable(int **adj, int V, int s) {
    bool *visited = (bool*)calloc(V, sizeof(bool));
    Queue *q = createQueue(V);
    visited[s] = true;
    enqueue(q, s);
    int count = 1;

    while (!isEmpty(q)) {
        int u = dequeue(q);
        for (int v = 0; v < V; v++) {
            if (adj[u][v] && !visited[v]) {
                visited[v] = true;
                count++;
                enqueue(q, v);
            }
        }
    }
    free(visited);
    freeQueue(q);
    return count;
}

int main() {
    system("chcp 65001 > nul"); 
    int V, E;

    printf("请输入顶点数 V（正整数，取值范围：1 ~ 任意正整数）: ");
    scanf("%d", &V);

    printf("请输入边数 E（非负整数，最大可能边数为 V*(V-1)）: ");
    scanf("%d", &E);

    if (V <= 0) {
        printf("错误: V 必须为正整数（≥1）。\n");
        return 1;
    }
    if (E < 0) {
        printf("错误: E 不能为负数。\n");
        return 1;
    }

    int maxEdges = V * (V - 1);
    if (E > maxEdges) {
        printf("错误: E 不能超过 V*(V-1)=%d。\n", maxEdges);
        return 1;
    }

    srand((unsigned int)time(NULL));

    int **adj = (int**)malloc(V * sizeof(int*));
    for (int i = 0; i < V; i++) {
        adj[i] = (int*)calloc(V, sizeof(int));
    }

    // 定义核心服务顶点：前10%的顶点（至少1个）
    int coreCount = V / 10;
    if (coreCount == 0) coreCount = 1;

    // 生成E条随机边，核心服务作为源的概率更高（50%的边源来自核心服务顶点）
    int edgesGenerated = 0;
    int maxAttempts = 1000000;
    int attempts = 0;

    while (edgesGenerated < E && attempts < maxAttempts) {
        int src;
        if (rand() % 100 < 50) {
            src = rand() % coreCount;
        } else {
            if (V == coreCount) continue;
            src = coreCount + rand() % (V - coreCount);
        }

        int dst = rand() % V;
        // 禁止自环、禁止重复边
        if (src == dst) continue;
        if (adj[src][dst]) continue;

        adj[src][dst] = 1;
        edgesGenerated++;
        attempts = 0;
    }
    if (edgesGenerated < E) {
        printf("警告: 仅生成 %d 条边（已达最大尝试次数），实际边数少于 %d\n", edgesGenerated, E);
    }

    // 计算每个顶点的可达顶点数，并求平均值与最大值
    double sum = 0.0;
    int maxReach = 0;
    for (int i = 0; i < V; i++) {
        int reach = bfsReachable(adj, V, i);
        sum += reach;
        if (reach > maxReach) maxReach = reach;
    }
    double avg = sum / V;

    printf("平均值为 %.2f，最大值为 %d，", avg, maxReach);

    // 风险评估
    double avgRatio = avg / V;
    double maxRatio = (double)maxReach / V;
    if (avgRatio >= 0.5 || maxRatio >= 0.5) {
        printf("说明系统耦合度高\n");
    } else {
        printf("说明系统耦合度低\n");
    }

    for (int i = 0; i < V; i++) {
        free(adj[i]);
    }
    free(adj);

    return 0;
}