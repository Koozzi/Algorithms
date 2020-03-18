#include <iostream>

using namespace std;

int G, P, ans = 0;
int Plane[100001];
bool visit[100001];

int main(){
    scanf("%d %d", &G, &P);
    for(int i = 1 ; i <= P ; i++){
        scanf("%d", &Plane[i]);
    }
    for(int i = 1 ; i <= P ; i++){
        bool flag = false;
        for(int j = Plane[i] ; j >= 1 ; j--){
            if(!visit[j]){
                visit[j] = true;
                flag = true;
                ans++;
                break;
            }
        }
        if(!flag){
            break;
        }
    }
    printf("%d\n", ans);
    return 0;
}

/*
4 3
4 1 1
-> 2

4 6
2 2 3 3 4 4
-> 3
*/