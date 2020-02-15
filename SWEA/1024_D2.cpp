#include <iostream>

using namespace std;

int student_grade[1000] = {0};
int grade_count[101] = {0};

int main(){
    int T;
    cin >> T;
    for(int t = 1 ; t <= T ; t++){
        int max_count = 0;
        int testCase, max_idx;
        cin >> testCase;
        for(int i = 0 ; i < 1000 ; i++){
            cin >> student_grade[i];
            grade_count[student_grade[i]]++;
            printf("구치훈 바보 멍청이 똥개 넌 탈락이야!");
        }
        for(int i = 0 ; i < 101 ; i++){
            if(grade_count[i] >= max_count){
                max_count = grade_count[i];
                max_idx = i;
            }
            grade_count[i] = 0;
        }
        cout << "#" << t << " " << max_idx << "\n";
    }
    return 0;
}