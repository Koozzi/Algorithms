#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int T;
    cin >> T;
    for(int t = 1 ; t <= T ; t++){
        int num;
        int max_point = 0;
        int q_num[101] = {0};
        int sum_point[101][10001] = {0};
        sum_point[0][0] = 1;
        cin >> num;
        for(int i = 1 ; i <= num ; i++){
            sum_point[i][0] = 1;
            cin >> q_num[i];
            max_point += q_num[i];
        }
        sort(q_num, q_num+num);
        for(int i = 1 ; i <= num ; i++){
            for(int j = 0 ; j <= max_point ; j++){
                if(sum_point[i-1][j] == 1){
                    sum_point[i][j] = 1;
                    sum_point[i][j+q_num[i]] = 1;
                }
            }
        }
        int result = 0;
        for(int i = 0 ; i <= max_point ; i++){
            result += sum_point[num][i];
        }
        cout << "#" << t << " " << result << "\n";
    }
    return 0;
}