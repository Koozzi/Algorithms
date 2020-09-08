#include <iostream>
#include <algorithm>
#include <sstream>
#include <cstring>
#include <string>
#include <vector>

using namespace std;

string change_string(string s){
    string new_str = s;
    for(int i = 0 ; i < new_str.size() ; i++){
        if(new_str[i] == '#'){
            new_str[i-1] = new_str[i-1] + 32;
            new_str.erase(new_str.begin() + i, new_str.begin() + i + 1);
        }
    }
    return new_str;
}

int get_time(string str1, string str2){
    string s = "";
    s += str1[0]; s += str1[1];
    int start_hour = stoi(s);
    
    s = "";
    s += str1[3]; s += str1[4];
    int start_min = stoi(s);
    
    s = "";
    s += str2[0]; s += str2[1];
    int end_hour = stoi(s);
    
    s = "";
    s += str2[3]; s += str2[4];
    int end_min = stoi(s);
    
    int hour = end_hour - start_hour;
    int min = end_min - start_min;
    if(min < 0){
        hour -= 1;
        min = 60 - end_min + start_min;
    }
    return 60 * hour + min;
}

vector<string> split(string s){
    vector<string> v;
    string token = "";
    istringstream iss(s);
    while(getline(iss, token, ',')){
        v.push_back(token);
    }
    return v;
}

string get_real_music(int t, string s){
    string str = "";
    if(t < s.size()){
        for(int i = 0 ; i < t ; i++){
            str.push_back(s[i]);
        }
    }
    else{
        int idx1 = 0; int idx2 = 0;
        while(1){
            if(idx1 == s.size()) idx1 = 0;
            if(idx2 == t) break;
            str.push_back(s[idx1]);
            idx1++; idx2++;
        }
    }
    return str;
}

string solution(string m, vector<string> v){
    string answer = "(None)";
    int longest_time = 0;
    for(int t = 0 ; t < v.size() ; t++){
        vector<string> vec;
        string real_music;
        vec = split(v[t]);
        // 방송 정보를 ','로 나누어서 새로운 벡터에 저장
        // vec[0] : start time
        // vec[1] : end time
        // vec[2] : music_name
        // vec[3] : music_melody
        m = change_string(m); // #이 있는 멜로디 문자열을 바꿔줌
        int Time = get_time(vec[0], vec[1]); // 방송 시간 구해줌
        real_music = get_real_music(Time, change_string(vec[3])); // 방송에서 나온 멜로디

        if(real_music.size() < m.size()) continue; // 만약에 기억에 남은 멜로디가 방송에서 나온 멜로디보다 길면 넘김
        long long isIn = real_music.find(m); // 방송에서 나온 멜로디에서 기억에 남은 멜로디가 있는지 확인
        if(isIn != string::npos){
            if(Time > longest_time){
                longest_time = Time;
                answer = vec[2];
            }
        }
    }
    return answer;
}

int main(){
    string m = "ABCDEFG";
    vector<string> v;
    v.push_back("12:00,12:14,HELLO,CDEFGAB");
    v.push_back("13:00,13:05,WORLD,ABCDEF");
    cout << solution(m, v) << "\n";
}