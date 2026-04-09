#include <string.h>

int LongestString(char s[], int n) {
    int len, i, j;
    for (len = n / 2; len > 0; len--) {
        for (i = 0; i <= n - 2 * len; i++) {
            for (j = i + len; j <= n - len; j++) {
                if (strncmp(&s[i], &s[j], len) == 0)
                    return len;
            }
        }
    }
    return 0;
}