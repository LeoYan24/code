#include<string.h>
#include <stdbool.h>

bool isRightMove(int A[],int B[],int n){
    if( n == 0 ) return true;

    for( int i = 0 ; i < n ; i++ ){
        bool match = true;
        for( int  j = 0 ; j < n ; j++ ){
            if( A[j+i] != B[j] ) match =false;
        }
        if( match ) return true;
    }
    return false;
}