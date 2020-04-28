#include <iostream>
#include <string.h>
#include <algorithm>
#define MAX_NUM 100001
using namespace std;

int M;
int atk[MAX_NUM];
Channel info[MAX_NUM];

class Channel{
public:
    int per;
    int start;
    int end;
    Channel(int a, int b, int c){
        per = a;
        start = b;
        end = c;
    }
    Channel(){
        per = 0;
        start = 0;
        end = 0;
    }
};

bool cmp(Channel a, Channel b){
        return a.start > b.start;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    memset(atk, 0, sizeof(atk));

    cin >> M;
    for(int i = 0 ; i < M ; i++){
        int a,b; cin >> a >> b;
        info[i] = Channel(i, a, b);
    }
    sort(info, info+M, cmp);

    for(int i=0 ; i < M ; i++){
        for(int j = i+1 ; j < M ; j++){
            if(info[i].start < info[j].end && info[i].start > info[j].start){
                atk[info[i].per]++;
            }
            if(info[i].start < info[i].start) break;
        }   
    }

    for(int i = 0 ; i < M ; i++){
        cout << atk[i] << "\n";
    }

    return 0;
}
