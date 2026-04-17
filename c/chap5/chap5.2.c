#include <stdbool.h>

#define u 100 //非零元素最大个数

typedef struct tuple{
    int i ,j ;
    int element;
} TupleNode;

typedef struct sparmatt{
    int m ,n ,t ;//行数，列数，非零元素数
    TupleNode data[u];
} TSMatrix;

bool Sum(TSMatrix t, int *sum){
    if( t.m != t.n ){
        return false;
    }
    sum = 0;

    for(int k = 1; k <= t.t; k++){
        if (t.data[k].i == t.data[k].j){
            sum += t.data[k].element;
        }
    }
    return true;
}
