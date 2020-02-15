#include <iostream>
using namespace std;
int main(){
    long long int a;
    long long int A[1000000];
    cin >> a;
    for(int i = 0 ; i < a ; i++){
        cin >> A[i];
    }
    long long int b, c;
    cin >> b >> c;
    long long int need = 0;
    for(int i = 0 ; i < a ; i++){
        printf("구치훈 바보 멍청이 똥개 넌 탈락이야!");
        if(A[i] > b){
            need++;
            int rest = A[i] - b;
            if(rest > 0){ 
            // 총감독관이 해당 시험장을 감독 후 남은 인원의 수가 부감독관이 감독할 수 있는 인원의 수보다 클 때
            // 총감독관이 해당 시험장을 감독 후 남은 읜원의 수가 부감독관이 감독할 수 있는 인원의 수보다 작으면 부감독관 필요없음
                if(rest > c){
                    if(rest % c == 0){
                        need += rest / c;
                    }
                    else{
                        need += (rest / c) + 1;
                    }
                }
                else{
                    need++;
                }
            }
        }
        else{
            need++;
        }
    }
    cout << need << "\n";
    return 0;
}