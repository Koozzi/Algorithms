#include <iostream>
#include <vector>

using namespace std;

int map[8][8];
int M;
int kingI, kingJ, rockI, rockJ;
int kingNextI, kingNextJ, rockNextI, rockNextJ;
char King[3];
char Rock[3];
char Order[51][3];

void show(){
    cout << "\n";
    for(int i = 0 ; i < 8 ; i++){
        for(int j = 0 ; j < 8 ; j++){
            cout << map[i][j] << " ";
        }cout << "\n";
    }
}
void moveKing(int idx){
    if(Order[idx][0] == 'L'){
        if(Order[idx][1] == '\0'){
            //L
            kingNextJ = kingJ - 1;
            kingNextI = kingI;
        }
        else if(Order[idx][1] == 'T'){
            //LT
            kingNextI = kingI + 1;
            kingNextJ = kingJ - 1;
        }
        else if(Order[idx][1] == 'B'){
            //LB
            kingNextI = kingI - 1;
            kingNextJ = kingJ - 1;
        }
    }
    else if(Order[idx][0] == 'R'){
        if(Order[idx][1] == '\0'){
            //R
            kingNextI = kingI;
            kingNextJ = kingJ + 1;
        }
        else if(Order[idx][1] == 'T'){
            //RT
            kingNextI = kingI + 1;
            kingNextJ = kingJ + 1;
        }
        else if(Order[idx][1] == 'B'){
            //RB
            kingNextI = kingI - 1;
            kingNextJ = kingJ + 1;
        }
    }
    else if(Order[idx][0] == 'B'){
        //B
        kingNextI = kingI - 1;
        kingNextJ = kingJ;
    }
    else if(Order[idx][0] == 'T'){
        //T
        kingNextI = kingI + 1;
        kingNextJ = kingJ;
    }
}
void moveRock(int idx){
    if(Order[idx][0] == 'L'){
        if(Order[idx][1] == '\0'){
            //L
            rockNextI = rockI;
            rockNextJ = rockJ - 1;
        }
        else if(Order[idx][1] == 'T'){
            //LT
            rockNextI = rockI + 1;
            rockNextJ = rockJ - 1;
        }
        else if(Order[idx][1] == 'B'){
            //LB
            rockNextI = rockI - 1;
            rockNextJ = rockJ - 1;
        }
    }
    else if(Order[idx][0] == 'R'){
        if(Order[idx][1] == '\0'){
            //R
            rockNextI = rockI;
            rockNextJ = rockJ + 1;
        }
        else if(Order[idx][1] == 'T'){
            //RT
            rockNextI = rockI + 1;
            rockNextJ = rockJ + 1;
        }
        else if(Order[idx][1] == 'B'){
            //RB
            rockNextI = rockI - 1;
            rockNextJ = rockJ + 1;
        }
    }
    else if(Order[idx][0] == 'B'){
        //B
        rockNextI = rockI - 1;
        rockNextJ = rockJ;
    }
    else if(Order[idx][0] == 'T'){
        //T
        rockNextI = rockI + 1;
        rockNextJ = rockJ;
    }
}

void intLocation(){
    kingI = King[1] - 48;
    kingJ = King[0] - 64;
    rockI = Rock[1] - 48;
    rockJ = Rock[0] - 64; 
}

int main(){
    cin >> King >> Rock >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> Order[i];
    }
    intLocation();
    for(int i = 0 ; i < M ; i++){
        // printf("King : (%d, %d)\n", kingJ, kingI);
        // printf("Rock : (%d, %d)\n", rockJ, rockI);
        moveKing(i);
        // printf("king next move : (%d, %d)\n", kingNextJ, kingNextI);
        if(kingNextI >= 1 && kingNextI <= 8 && kingNextJ >= 1 && kingNextJ <= 8){
            if(kingNextI == rockI && kingNextJ == rockJ){
                moveRock(i);
                // printf("rock next move : (%d, %d)\n", rockNextJ, rockNextI);
                if(rockNextI >= 1 && rockNextI <= 8 && rockNextJ >= 1 && rockNextJ <= 8){
                    rockI = rockNextI;
                    rockJ = rockNextJ;
                    kingI = kingNextI;
                    kingJ = kingNextJ;
                }
            }
            else{
                kingI = kingNextI;
                kingJ = kingNextJ;
            }
        }
        // printf("King : (%d, %d)\n", kingJ, kingI);
        // printf("Rock : (%d, %d)\n", rockJ, rockI);
    }
    char finalK = kingJ + 64;
    char finalR = rockJ + 64;
    cout << finalK << kingI << "\n";
    cout << finalR << rockI << "\n";
    return 0;
}