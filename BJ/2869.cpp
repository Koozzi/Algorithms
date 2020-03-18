#include <iostream>

using namespace std;

int A, B, V, ans = 0; // 낮, 밤, 목표

// int main(){
//     cin >> A >> B >> V;
//     int dest = 0;
//     while(1){
//         ans++;
//         dest += A;
//         if(dest >= V){
//             cout << ans << endl;
//             break;
//         }
//         dest -= B;
//     }
//     return 0;
// }

int main(){
    cin >> A >> B >> V;
    if(A == V){
        cout << 1 << endl;
        return 0;
    }
    if((V - A) % (A - B) == 0){
        cout << (V - A) / (A - B) + 1 << endl;
    }
    else{
        cout << (V - A) / (A - B) + 2 << endl;
    }
    return 0;
}

/* V - A 
3 1 7           7-3=4
-> 3            3 2 / 5 4 / 7 

5 2 12          12-5=7
-> 4            5 3 / 8 6 / 11 9 / 16

4 2 12          12-4=8
-> 5            4 2 / 6 4 / 8 6 / 10 8 / 12

2 1 5           5-2=3
-> 4            2 1 / 3 2 / 4 3 / 5

10 8 12         12-10=2
-> 2            10 2 / 12
*/
