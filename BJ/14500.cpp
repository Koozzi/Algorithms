#include <iostream>

using namespace std;

int main(){
    int map[500][500] = {0};
    int M, N, ans = 0; cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> map[i][j];
        }
    }
    /*
    o
    o
    o
    o
    */
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N - 3 ; j++){
            ans = max(ans, map[i][j] + map[i][j+1] + map[i][j+2] + map[i][j+3]);
        }
    }
    /*
    oooo
    */
    for(int i = 0 ; i < M - 3 ; i++){
        for(int j = 0 ; j < N ; j++){
            ans = max(ans, map[i][j] + map[i+1][j] + map[i+2][j] + map[i+3][j]);
        }
    }
    /*
    oo
    oo
    */
    for(int i = 0 ; i < M - 1 ; i++){
        for(int j = 0 ; j < N - 1 ; j++){
            ans = max(ans, map[i][j] + map[i+1][j] + map[i][j+1] + map[i+1][j+1]);
        }
    }
    /*
     o
    oo
     o
    */
    for(int i = 0 ; i < M - 2 ; i++){
        for(int j = 1 ; j < N ; j++){
            ans = max(ans, map[i][j] + map[i+1][j] + map[i+2][j] + map[i+1][j-1]);
        }
    }
    /*
     o
    ooo
    */
    for(int i = 0 ; i < M - 1 ; i++){
        for(int j = 1 ; j < N - 1 ; j++){
            ans = max(ans, map[i][j] + map[i+1][j] + map[i+1][j-1] + map[i+1][j+1]);
        }
    }
    /*
    o
    oo
    o
    */
    for(int i = 0 ; i < M - 2 ; i++){
        for(int j = 0 ; j < N - 1 ; j++){
            ans = max(ans, map[i][j] + map[i+1][j] + map[i+2][j] + map[i+1][j+1]);
        }
    }
    /*
    ooo
     o
    */
    for(int i = 0 ; i < M - 1 ; i++){
        for(int j = 0 ; j < N - 1 ; j++){
            ans = max(ans, map[i][j] + map[i][j+1] + map[i][j+2] + map[i+1][j+1]);
        }
    }
    /*
    oo
    o
    o
    */
    for(int i = 0 ; i < M - 2 ; i++){
        for(int j = 0 ; j < N - 1 ; j++){
            ans = max(ans, map[i][j] + map[i][j+1] + map[i+1][j] + map[i+2][j]);
        }
    }
    /*
    ooo
      o
    */
    for(int i = 0 ; i < M - 1 ; i++){
        for(int j = 0 ; j < N - 2 ; j++){
            ans = max(ans, map[i][j] + map[i][j+1] + map[i][j+2] + map[i+1][j+2]);
        }
    }
    /*
     o
     o
    oo
    */
    for(int i = 0 ; i < M - 2 ; i++){
        for(int j = 1 ; j < N ; j++){
            ans = max(ans, map[i][j] + map[i+1][j] + map[i+2][j] + map[i+2][j-1]);
        }
    }
    /*
    o
    ooo
    */
    for(int i = 0 ; i < M - 1 ; i++){
        for(int j = 0 ; j < N - 2 ; j++){
            ans = max(ans, map[i][j] + map[i+1][j] + map[i+1][j+1] + map[i+1][j+2]);
        }
    }
    /*
    oo
     o
     o
    */
    for(int i = 0 ; i < M - 2 ; i++){
        for(int j = 0 ; j < N - 1 ; j++){
            ans = max(ans, map[i][j] + map[i][j+1] + map[i+1][j+1] + map[i+2][j+1]);
        }
    }
    /*
      o
    ooo
    */
    for(int i = 1 ; i < M ; i++){
        for(int j = 0 ; j < N - 2 ; j++){
            ans = max(ans, map[i][j] + map[i][j+1] + map[i][j+2] + map[i-1][j+2]);
        }
    }
    /*
    o
    o
    oo
    */
    for(int i = 0 ; i < M - 2 ; i++){
        for(int j = 0 ; j < N - 1 ; j++){
            ans = max(ans, map[i][j] + map[i+1][j] + map[i+2][j] + map[i+2][j+1]);
        }
    }
    /*
    ooo
    o
    */
    for(int i = 0 ; i < M - 1 ; i++){
        for(int j = 0 ; j < N -2 ; j++){
            ans = max(ans, map[i][j] + map[i][j+1] + map[i][j+2] + map[i+1][j]);      
        }
    }
    /*
    o
    oo
     o
    */
    for(int i = 0 ; i < M -  2 ; i++){
        for(int j = 0 ; j < N - 1 ; j++){
            ans = max(ans, map[i][j] + map[i+1][j] + map[i+1][j+1] + map[i+2][j+1]);
        }
    }
    /*
     o
    oo
    o
    */
    for(int i = 0 ; i < M - 2; i++){
        for(int j = 1 ; j < N ; j++){
            ans = max(ans, map[i][j] + map[i+1][j] + map[i+1][j-1] + map[i+2][j-1]);
        }
    }
    /*
     oo
    oo
    */
    for(int i = 0 ; i < M - 1 ; i++){
        for(int j = 1 ; j < N - 1 ; j++){
            ans = max(ans, map[i][j] + map[i][j+1] + map[i+1][j] + map[i+1][j-1]);
        }
    }
    /*
    oo
     oo
    */
    for(int i = 0 ; i < M - 1; i++){
        for(int j = 0 ; j < N - 2 ; j++){
            ans = max(ans, map[i][j] + map[i][j+1] + map[i+1][j+1] + map[i+1][j+2]);
        }
    }
    cout << ans << "\n";
}

































// #include <iostream>
// #include <vector>
// #include <algorithm>
// #include <deque>
// #include <cmath>
// #include <stdio.h>

// using namespace std;

// int M, N, ans = 0;

// int map[500][500];

// vector<pair<int, int>> v;

// deque<pair<int, int>> dq;



// void rotate(int startI, int startJ){
//     int sum = 0;
//     for(int i = 0 ; i < 4 ; i++){
//         int moveI = (startJ - dq.front().second);
//         int moveJ = (startI - dq.front().first);
//         dq.push_back(make_pair(startI - moveI, startJ + moveJ));
//         dq.pop_front();
//     }
//     for(int i = 0 ; i < 4 ; i++){
//         int I = dq[i].first;
//         int J = dq[i].second;
//         if(I >= 0 && I < M && J >= 0 && J < N){
//             sum += map[I][J];
//         }
//         else{
//             return;
//         }
//     }
//     ans = max(ans, sum);
// }

// void flip(int startI, int startJ){
//     for(int i = 0 ; i < 4; i++){
//         dq.push_back(make_pair(startI - (dq.front().first - startI) , dq.front().second));
//         dq.pop_front();
//     }
// }

// void solve(int startI, int startJ){
//     for(int i = 0 ; i < 4; i++){
//         rotate(startI, startJ);
//     }    
//     flip(startI, startJ);
//     for(int i = 0 ; i < 4 ; i++){
//         rotate(startI, startJ);
//     }
// }

// void tet1(int startI, int startJ){
//     dq.push_back(make_pair(startI, startJ));
//     dq.push_back(make_pair(startI, startJ + 1));
//     dq.push_back(make_pair(startI + 1, startJ));
//     dq.push_back(make_pair(startI + 1, startJ + 1));
//     solve(startI, startJ);
// }

// void tet2(int startI, int startJ){
//     dq.push_back(make_pair(startI, startJ));
//     dq.push_back(make_pair(startI, startJ + 1));
//     dq.push_back(make_pair(startI, startJ + 2));
//     dq.push_back(make_pair(startI, startJ + 3));
//     solve(startI, startJ);
// }

// void tet3(int startI, int startJ){
//     dq.push_back(make_pair(startI, startJ));
//     dq.push_back(make_pair(startI + 1, startJ));
//     dq.push_back(make_pair(startI + 2, startJ));
//     dq.push_back(make_pair(startI + 2, startJ + 1));
//     solve(startI, startJ);
// }

// void tet4(int startI, int startJ){
//     dq.push_back(make_pair(startI, startJ));
//     dq.push_back(make_pair(startI + 1, startJ));
//     dq.push_back(make_pair(startI + 1, startJ + 1));
//     dq.push_back(make_pair(startI + 2, startJ + 1));
//     solve(startI, startJ);
// }

// void tet5(int startI, int startJ){
//     dq.push_back(make_pair(startI, startJ));
//     dq.push_back(make_pair(startI, startJ + 1));
//     dq.push_back(make_pair(startI, startJ + 2));
//     dq.push_back(make_pair(startI + 1, startJ + 1));
//     solve(startI, startJ);
// }

// int main(){
//     cin >> M >> N;
//     for(int i = 0 ; i < M ; i++){
//         for(int j = 0 ; j < N ; j++){
//             cin >> map[i][j];
//         }
//     }
//     for(int i = 0 ; i < M ; i++){
//         for(int j = 0 ; j < N ; j++){
//             tet1(i,j);
//             dq.clear();
//             tet2(i,j);
//             dq.clear();
//             tet3(i,j);
//             dq.clear();
//             tet4(i,j);
//             dq.clear();
//             tet5(i,j);
//             dq.clear();
//         }
//     }
//     cout << ans << "\n";
//     return 0;
// }
