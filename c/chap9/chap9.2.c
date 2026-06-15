#include <stdio.h>
#include <stdlib.h>

#define MAXSIZE 1000
typedef int KeyType;
typedef int InfoType;

typedef struct {
    KeyType key;
    InfoType otherinfo;
} ElemType;

int Index(ElemType r[], int low, int high, KeyType k) {
    int original_low = low;   //保存初始区间的下界，用于计算名次

    while (low <= high) {
        int i = low, j = high;
        ElemType pivot = r[low];

        while (i < j) {
            //从右向左找第一个大于基准的元素
            while (i < j && r[j].key <= pivot.key) j--;
            if (i < j) r[i++] = r[j];

            //从左向右找第一个小于基准的元素
            while (i < j && r[i].key >= pivot.key) i++;
            if (i < j) r[j--] = r[i];
        }
        r[i] = pivot;

        // 判断基准关键字是否等于 k
        if (r[i].key == k) return i - original_low + 1;   //在原始区间中的名次
        else if (k > r[i].key) high = i - 1;
        else low = i + 1;
    }

    return 0;
}