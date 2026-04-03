#include <stdio.h>
#include <stdbool.h>

bool Judge(char A[]){
    int cnt = 0,i = 0;
    while( A[i] != '\0' ){
        if( A[i] == 'I' ) cnt++;
        else if( A[i] == 'O' ){
            if( cnt == 0 ) return 0;
            else cnt--;
        }
    }
    return cnt == 0;
}