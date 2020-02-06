#include <iostream>
#include <algorithm>

using namespace std;
int arr[1001][1001] = {0};
int height[1001] = {0};
int main(){
    int T = 10;
    int testCase;

    for(testCase = 1 ; testCase <= T ; testCase++){
        int width_len = 0;
        int result_count = 0;
        int input_height = 0;
        cin >> width_len;
        for(int i = 1 ; i <= width_len ; i++){
            cin >> input_height;
            height[i] = input_height;
            for(int j = 1 ; j <= height[i] ; j++){
                arr[i][j] = 1;
            }
        }
        for(int i = 3 ; i <= width_len-2 ; i++){
            if(height[i] > height[i-1] && height[i] > height[i+1]){
                int higher = max(height[i-1], height[i+1]);
                for(int j = height[i] ; j > higher ; j--){
                    if(arr[i-2][j] == 0 && arr[i-1][j] == 0 && arr[i+1][j] == 0 && arr[i+2][j] == 0){
                        result_count++;
                    }
                } 
            }
        }
        cout << "#" << testCase << " " << result_count << "\n";
        for(int i = 1 ; i <= 1001 ; i++){
            height[i] = 0;
            for(int j = 1 ; j <= 1001 ; j++){
                arr[i][j] = 0;
            }
        }
    }
    return 0;
}