# Algorithms

반복 숙달

## BAEKJOON Online Judge

* [SW 역량테스트 준비 기초 - 수학](https://www.acmicpc.net/workbook/view/3935)
* [SW 역량테스트 준비 기초 - 브루트 포스](https://www.acmicpc.net/workbook/view/3936) ⭐
* [SW 역량테스트 준비 기초 - 부르트 포스(N과 M)](https://www.acmicpc.net/workbook/view/3937) ⭐
* [SW 역량테스트 준비 기초 - 그래프와 BFS](https://www.acmicpc.net/workbook/view/3938) 
* [SW 역량테스트 준비 기초 - 다이나믹 프로그래밍](https://www.acmicpc.net/workbook/view/3939) 

## Set

set은 '어디에' 데이터를 추가할지에 대한 정보가 없음. 그냥 한 상자에 데이터를 때려박는다고 생각하면 됨. 그래서 내가 찾고자 하는 데이터가 어디에 있는지는 신경쓰지 않고 내가 찾고자 하는 데이터가 있는지 없는지 검사하는데 적합하다.

그리고 set에 insert할 때 똑같은 데이터를 계속해서 넣으면 하나면 저장된다. 예를들어 s라는 set에 1을 3번 insert했다면 s에는 1이 하나만 들어가있다. 

## Map

Set이랑 크게 다를 것이 없다. 다만 Map은 Set과 다르게 Key와 Value 한 짝을 이루어서 저장한다. 

## String find()
~~~c
#include <iostream>
#include <string>
using namespace std;

int main(){
    string s("asdKOOZZIsdhf");
    long long isIN = s.find("KOOZZI");
    if(isIN != string::npos){ // 포함하고 있다는 뜻.
        ...
    }
}
~~~