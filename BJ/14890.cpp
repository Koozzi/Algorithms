#include <iostream>
#include <vector>

using namespace std;

int M, L;
int map[100][100];

vector<int> v1;
vector<int> v2;

void show(){
    cout << "\n";
    for(int i = 0 ; i < v1.size() ; i++){
        cout << v1[i] << " ";
    }cout << "\n";
}

bool test(vector<int> vec){
    v2.clear();
    int current = 0;
    v2.push_back(vec[current]);
    int T = M;
    while(T--){
        int next = current + 1;
        if(vec[next] == vec[current]){
            current = next;
            if(current >= M - 1){
                return true;
            }
        }
        else if(vec[next] > vec[current]){
            if(vec[next] - vec[current] > 1){
                break;
            }
            else{
                if(v2.size() >= L){
                    v2.clear();
                    current = next;
                    if(current >= M - 1){
                        return true;
                    }
                }else{
                    break;
                }
            }
        }
        else if(vec[next] < vec[current]){
            if(vec[current] - vec[next] > 1){
                break;
            }
            else{
                v2.clear();
                for(int i = next ; i < next + L ; i++){
                    if(i < M){
                        if(vec[i] == vec[next]){
                            v2.push_back(vec[i]);
                        }
                    }
                }
                if(v2.size() == L){ // 내리막 경사길 만들 수 있음
                    current = next + L - 1;
                    v2.clear();
                    if(current >= M - 1){
                        return true;
                    }
                    else{
                        if(vec[current + 1] == vec[current]){
                            current = current + 1;
                        }
                        else if(vec[current + 1] > vec[current]){
                            break;
                        }
                    }
                }
                else{
                    break;
                }
            }
        }
        if(current >= M-1){
            return true;
        }
        v2.push_back(vec[current]);
    }
    return false;
}

int main(){
    cin >> M >> L;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < M ; j++){
            cin >> map[i][j];
        }
    }
    int cnt = 0;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < M ; j++){
            v1.push_back(map[i][j]);
        }
        if(test(v1)){
            cnt++;
        }
        v1.clear();
    }
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < M ; j++){
            v1.push_back(map[j][i]);
        }
        if(test(v1)){
            cnt++;
        }
        v1.clear();
    }
    cout << cnt << "\n";
    return 0;
}