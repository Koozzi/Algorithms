#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> treeInfo[11][11];

int mapSize, treeNum, year, ans = 0;
int map[11][11];
int appendMap[11][11];

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[8] = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};

void SPRINGSUMMER(){
    for(int i = 1 ; i <= mapSize ; i++){
        for(int j = 1 ; j <= mapSize ; j++){
            if(treeInfo[i][j].size() != 0){
                sort(treeInfo[i][j].begin(), treeInfo[i][j].end());        
            }
            for(int t = 0 ; t < treeInfo[i][j].size() ; t++){
                if(map[i][j] >= treeInfo[i][j][t]){
                    map[i][j] -= treeInfo[i][j][t];
                    treeInfo[i][j][t]++;
                }
                else{
                    for(int k = treeInfo[i][j].size() - 1 ; k >= t ; k--){
                        map[i][j] += treeInfo[i][j][k] / 2;
                        treeInfo[i][j].pop_back();
                    }
                    break;
                }
            }
        }
    }
}
void FALL(){
    for(int i = 1 ; i <= mapSize ; i++){
        for(int j = 1 ; j <= mapSize ; j++){
            if(treeInfo[i][j].size() != 0){
                for(int t = 0 ; t < treeInfo[i][j].size() ; t++){
                    if(treeInfo[i][j][t] % 5 == 0 && treeInfo[i][j][t] >= 5){
                        for(int k = 0 ; k < 8 ; k++){
                            int nextI = i + moveDir[k].moveI;
                            int nextJ = j + moveDir[k].moveJ;
                            if(nextI >= 1 && nextI <= mapSize && nextJ >= 1 && nextJ <= mapSize){
                                treeInfo[nextI][nextJ].push_back(1);
                            }
                        }
                    }
                }
            }
        }
    }
}
void WINTER(){
    for(int i = 1 ; i <= mapSize ; i++){
        for(int j = 1 ; j <= mapSize ; j++){
            map[i][j] += appendMap[i][j];
        }
    }
}
void treeCount(){
    for(int i = 1 ; i <= mapSize ; i++){
        for(int j = 1 ; j <= mapSize ; j++){
            ans += treeInfo[i][j].size();
        }
    }
}
int main(){
    cin >> mapSize >> treeNum >> year;
    for(int i = 1 ; i <= mapSize ; i++){
        for(int j = 1 ; j <= mapSize ; j++){
            map[i][j] = 5;
        }
    }
    for(int i = 1 ; i <= mapSize ; i++){
        for(int j = 1 ; j <= mapSize ; j++){
            cin >> appendMap[i][j];
        }
    }
    for(int i = 0 ; i < treeNum ; i++){
        int a, b, c;
        cin >> a >> b >> c;
        treeInfo[a][b].push_back(c);
    }
    while(year--){
        SPRINGSUMMER();
        FALL();
        WINTER();
    }
    treeCount();
    cout << ans << endl;

    // for(int i = 1 ; i <= mapSize ; i++){
    //     for(int j = 1 ; j <= mapSize ; j++){
    //         if(treeInfo[i][j].size() != 0){
    //             for(int t = 0 ; t < treeInfo[i][j].size() ; t++){
    //                 printf("(%d, %d) %d    양분 : %d\n", i, j, treeInfo[i][j][t], map[i][j]);
    //             }
    //         }
    //     }
    // }

    return 0;
}