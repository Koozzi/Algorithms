#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int cnt = 0;
struct trie{
    bool finish;
    trie *Node[26];
    trie(){
        finish = false;
        for(int i = 0 ; i < 26 ; i++){
            Node[i] = NULL;
        }
    }
    void insert(string s){
        if(s[0] == '\0'){
            finish = true;
            return;
        }
        int cur = s[0] - '0';
        if(Node[cur] == NULL){
            Node[cur] = new trie();
        }
        Node[cur]->insert(s.substr(1));
    }
    bool find(string s, int len){
        cnt++;
        int next = s[0] - '0';
        if(s[0] == '\0') return true;
        if(finish && cnt < len) return false;
        if(Node[next] == NULL) return false;
        return Node[next]->find(s.substr(1), len);
    }
};
int main(){
    int T; cin >> T;
    while(T--){
        int N; cin >> N;
        trie tri;
        vector<string> v;
        for(int i = 0 ; i < N ; i++){
            string s; cin >> s;
            tri.insert(s);
            v.push_back(s);
        }

        bool ans = true;
        for(int i = 0 ; i < N ; i++){
            cnt = -1;
            if(!tri.find(v[i], v[i].size())){
                ans = false;
                break;
            }
        }
        if(ans) cout << "YES" << "\n";
        else cout << "NO" << "\n";
    }
}