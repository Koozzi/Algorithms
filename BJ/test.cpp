#include <iostream>
#include <algorithm>
#include <queue>
#include <string>
#include <tuple>
#include <cstring>

using namespace std;

int d[1001][1001][2];
int a[1001][1001]; 
int dx[] = {-1,1,0,0};
int dy[] = {0,0,1,-1};
int main()
{   
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n,m;
    cin >> n >> m;
    for(int i=0; i<n; i++){
        string temp;
        cin >> temp;
        for(int j=0; j<m; j++){
            a[i][j] = temp[j] -'0';
        }
    }

    queue< pair<pair<int,int>,int > >q;
    q.push(make_pair(make_pair(0,0),0));
    d[0][0][0] = 1;
    
    while(!q.empty()){
        int x = q.front().first.first; // i
        int y = q.front().first.second; // j
        int z = q.front().second; 
        if(x == n - 1 && y == m - 1){
            cout << d[x][y][z] << "\n";
            return 0;
        }
        q.pop();
        for(int k=0; k<4; k++){
            int nx = x+dx[k];
            int ny = y+dy[k];
            if(nx >= 0 && nx <n && ny>=0 && ny <m){
                if(d[nx][ny][z] == 0 && a[nx][ny]==0){ // 빈방이고 아직 방문 안했을때
                    d[nx][ny][z] = d[x][y][z] + 1;
                    q.push(make_pair(make_pair(nx,ny),z));
                }
                if(d[nx][ny][z+1] == 0 && a[nx][ny]==1 && z==0){ // 벽있고 아직 방문 안했을때
                    d[nx][ny][z+1] = d[x][y][z]+1;
                    q.push(make_pair(make_pair(nx,ny),z+1)); //벽뚫었으니까 +1 해줌
                }
            }
        }
    }

    // if(d[n-1][m-1][0] !=0){ // 벽 안부숨
    //     cout << d[n-1][m-1][0] << "\n";
    // }else if(d[n-1][m-1][1] !=0){ // 벽 부숨
    //     cout << d[n-1][m-1][1] << "\n";
    // }else if(d[n-1][m-1][0] !=0 && d[n-1][m-1][1] != 0 ){ //벽 부순거 안부순거 둘다 존재
    //     cout << min(d[n-1][m-1][0],d[n-1][m-1][1]) << "\n";
    // }else{
    //     cout << -1 << "\n";
    // }

    return 0;

}