#include <iostream>

using namespace std;

char color[3][7];
char NUM[13];

void setNum(){
    for(int i = 0 ; i < 2 ; i++){
        if(color[i][0] == 'b'){
            if(color[i][1] == 'l'){
                if(color[i][2] == 'a'){
                    NUM[i] = '0';
                }
                else{
                    NUM[i] = '6';
                }
            }
            else{
                NUM[i] = '1';
            }
        }
        else if(color[i][0] == 'r'){
            NUM[i] = '2';
        }
        else if(color[i][0] == 'o'){
            NUM[i] = '3';
        }
        else if(color[i][0] == 'y'){
            NUM[i] = '4';
        }
        else if(color[i][0] == 'g'){
            if(color[i][3] == 'e'){
                NUM[i] = '5';
            }
            else{
                NUM[i] = '8';
            }
        }
        else if(color[i][0] == 'v'){
            NUM[i] = '7';
        }
        else if(color[i][0]){
            NUM[i] = '9'; 
        }
    }
}
void setMult(){
    int i = 2;
    if(color[i][0] == 'b'){
        if(color[i][1] == 'l'){
            if(color[i][2] == 'a'){
                // black
                NUM[2] = 'E';
                return;
            }
            else{
                // blue 
                for(int j = 2 ; j < 8 ; j++){
                    NUM[j] = '0';
                }
                NUM[8] = 'E';
            }
        }
        else{
            // brown
            NUM[2] = '0';
            NUM[3] = 'E';
        }
    }
    else if(color[i][0] == 'r'){
        // red
        NUM[2] = '0';
        NUM[3] = '0';
        NUM[4] = 'E';
    }
    else if(color[i][0] == 'o'){
        // orange
        for(int j = 2 ; j < 5 ; j++){
            NUM[j] = '0';
        }
        NUM[5] = 'E';
    }
    else if(color[i][0] == 'y'){
        // yellow
        for(int j = 2 ; j < 6 ; j++){
            NUM[j] = '0';
        }
        NUM[6] = 'E';
    }
    else if(color[i][0] == 'g'){
        if(color[i][3] == 'e'){
            // green
            for(int j = 2 ; j < 7 ; j++){
                NUM[j] = '0';
            }
            NUM[7] = 'E';
        }
        else{
            // grey
            for(int j = 2 ; j < 10 ; j++){
                NUM[j] = '0';
            }
            NUM[10] = 'E';
        }
    }
    else if(color[i][0] == 'v'){
        // violet
        for(int j = 2 ; j < 9 ; j++){
            NUM[j] = '0';
        }
        NUM[9] = 'E';
    }
    else if(color[i][0]){
        // white
        for(int j = 2 ; j < 11 ; j++){
            NUM[j] = '0';
        }
        NUM[11] = 'E';
    }
}
int main(){
    cin >> color[0] >> color[1] >> color[2];
    setNum();
    setMult();

    // cout << NUM[0] << NUM[1] << endl;

    if(NUM[0] == '0' && NUM[1] == '0'){
        cout << 0 << endl;
        return 0;
    }
    
    else if(NUM[0] == '0' && NUM[1] != 0){
        cout << NUM[1];
    }

    else{
        cout << NUM[0] << NUM[1];
    }

    int idx = 2;
    while(1){
        if(NUM[idx] == 'E'){
            break;
        }
        cout << NUM[idx];
        idx++;
    }cout << "\n";
    return 0;
}