#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<windows.h>

#define MAX_DEPTH 10000   // 最大嵌套深度
#define MAX_LINE_LEN 4096 // 每行最大长度
#define MAX_FILE 1000     // 最大文件数量

typedef struct {
    char ch;
    int line;
} Node;

typedef struct {
    Node data[MAX_DEPTH];
    int top;
} Stack;

int push( Stack* s ,char ch ,int line );
void pop( Stack* s);
int IsTargetFile( const char* filename );
int isBra( char ch );
int isKet( char ch );
int match( char left, char right );
void ErrorPrint( int error ,int line, char ch );
int scan_files(const char *dir_path, char ***filepaths, int *count);
void free_filepaths(char **filepaths, int count);

int main(){
    char dir_path[MAX_FILE];
    char** filepath = NULL;
    int cnt = 0;

    printf("请输入一个路径：\n");
    if (fgets(dir_path, sizeof(dir_path), stdin) == NULL) {
        printf("读取路径失败\n");
        return -1;
    }
    dir_path[strcspn(dir_path, "\n")] = '\0';//去除末尾的换行符
    if (scan_files(dir_path, &filepath, &cnt) != 0) {
        printf("扫描目录失败\n");
        return -1;
    }
    if (cnt == 0) {
        printf("目录下没有文件\n");
        free_filepaths(filepath, cnt);
        return 0;
    }

    for( int j = 0 ; j < cnt ; j++ ){
        FILE *fp = fopen(filepath[j], "r");
        if (!fp) {
            printf("无法打开文件: %s\n", filepath[j]);
            continue;
        }

        Stack braket;
        braket.top = -1 ;
        int error = 0;//错误类型
        char curline[MAX_LINE_LEN];//当前检查行
        int num = 0;//行数

        while( fgets(curline ,sizeof(curline) ,fp) ){
            num++;
            for (int i = 0; curline[i]; i++) {
                char c = curline[i];
                if( isBra(c) ){
                    if( push(&braket ,c ,num ) != 0 ){
                        printf("文件[%s]：括号嵌套过深（超过%d层）\n", filepath[j], MAX_DEPTH);
                        error = 1;
                        break;
                    }
                }else if( isKet(c) ){
                    if( braket.top == -1 ){
                        error = 3;//未匹配右括号
                        ErrorPrint(3,num,c);
                        break;
                    }
                    else if( match(braket.data[braket.top].ch,c) ) pop(&braket);
                    else{
                        error = 2;//匹配错误
                        ErrorPrint(error,num,c);
                        break;
                    }
                }
            }
            if( error ) break;
        }

        if( error == 0 && braket.top == -1 ) printf("文件[%s]括号匹配合法\n",filepath[j]);
        else if( braket.top >= 0 ){
            error = 4;//未匹配左括号
            ErrorPrint(error,braket.data[0].line,braket.data[0].ch);
        }
        fclose(fp);
    }

    free_filepaths(filepath,cnt);
    return 0;
}

int push( Stack* s ,char ch ,int line ){
    if( s->top < MAX_DEPTH ){
        s->top++;
        s->data[s->top].ch = ch;
        s->data[s->top].line = line;
        return 0;
    }else return -1;
}

void pop( Stack* s){
    if( s->top >= 0 ) s->top--;
}

int IsTargetFile( const char* filename ){
    const char* ext = strrchr(filename, '.');
    if (!ext) return 0;
    return (strcmp(ext, ".c") == 0 ||
            strcmp(ext, ".cpp") == 0 ||
            strcmp(ext, ".java") == 0);
}

int isBra( char ch ){
    if( ch == '(' || ch == '[' || ch == '{' ) return 1;
    else return 0;
}

int isKet( char ch ){
    if( ch == ')' || ch == ']' || ch == '}' ) return 1;
    else return 0;
}

int match( char left, char right ) {
    return (left == '(' && right == ')') ||
           (left == '[' && right == ']') ||
           (left == '{' && right == '}');
}

void ErrorPrint( int error, int line, char ch ){
    if( error == 2 ){
        if( ch == ')' ) printf("第%d行：圆括号嵌套顺序错误\n",line);
        else if( ch == ']' ) printf("第%d行：方括号嵌套顺序错误\n",line);
        else if( ch == '}' ) printf("第%d行：花括号嵌套顺序错误\n",line);
    }else if( error == 3 ){
        if( ch == ')' ) printf("第%d行：未匹配的右圆括号\n",line);
        else if( ch == ']' ) printf("第%d行：未匹配的右方括号\n",line);
        else if( ch == '}' ) printf("第%d行：未匹配的右花括号\n",line);
    }else if( error == 4 ){
        if( ch == '(' ) printf("第%d行：未匹配的左圆括号\n",line);
        else if( ch == '[' ) printf("第%d行：未匹配的左方括号\n",line);
        else if( ch == '{' ) printf("第%d行：未匹配的左花括号\n",line);
    }
}

int scan_files(const char *dir_path, char ***filepaths, int *count){
    if (dir_path == NULL || filepaths == NULL || count == NULL) {
        return -1;
    }

    // 构造搜索模式：目录路径 + "\\*"
    char search_path[MAX_PATH];
    snprintf(search_path, sizeof(search_path), "%s\\*", dir_path);

    WIN32_FIND_DATA find_data;
    HANDLE hFind = FindFirstFile(search_path, &find_data);
    if (hFind == INVALID_HANDLE_VALUE) {
        fprintf(stderr, "无法打开目录: %s\n", dir_path);
        return -1;
    }

    // 动态数组初始容量
    int capacity = 10;
    *filepaths = (char **)malloc(capacity * sizeof(char *));
    if (*filepaths == NULL) {
        FindClose(hFind);
        return -1;
    }
    *count = 0;

    do {
        // 跳过 "." 和 ".." 目录
        if (strcmp(find_data.cFileName, ".") == 0 ||
            strcmp(find_data.cFileName, "..") == 0) {
            continue;
        }

        // 只处理文件（忽略子目录）
        if (!(find_data.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) && IsTargetFile(find_data.cFileName)) {
            // 构建完整文件路径: dir_path + "\" + 文件名
            char full_path[MAX_PATH];
            snprintf(full_path, sizeof(full_path), "%s\\%s", dir_path, find_data.cFileName);

            // 分配字符串内存
            char *path_copy = _strdup(full_path);  // 或 malloc(strlen(full_path)+1); strcpy
            if (path_copy == NULL) {
                // 内存分配失败，清理已分配的资源并退出
                for (int i = 0; i < *count; i++) {
                    free((*filepaths)[i]);
                }
                free(*filepaths);
                *filepaths = NULL;
                FindClose(hFind);
                return -1;
            }

            // 动态扩容
            if (*count >= capacity) {
                capacity *= 2;
                char **new_arr = (char **)realloc(*filepaths, capacity * sizeof(char *));
                if (new_arr == NULL) {
                    free(path_copy);
                    for (int i = 0; i < *count; i++) {
                        free((*filepaths)[i]);
                    }
                    free(*filepaths);
                    *filepaths = NULL;
                    FindClose(hFind);
                    return -1;
                }
                *filepaths = new_arr;
            }

            (*filepaths)[*count] = path_copy;
            (*count)++;
        }
    } while (FindNextFile(hFind, &find_data) != 0);

    FindClose(hFind);
    return 0;
}

void free_filepaths(char **filepaths, int count) {
    if (filepaths == NULL) return;
    for (int i = 0; i < count; i++) {
        free(filepaths[i]);
    }
    free(filepaths);
}