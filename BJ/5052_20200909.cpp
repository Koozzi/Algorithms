#include <iostream>
#include <algorithm>
using namespace std;
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
        int cur = s[0] - 'A';
        if(Node[cur] == NULL){
            Node[cur] = new trie();
        }
        Node[cur]->insert(s.substr(1));
    }
    bool find(string s){
        int next = s[0] - 'A';
        if(s[0] == '\0') return true;
        if(Node[next] == NULL) return false;
        return Node[next]->find(s.substr(1));
    }
};
int main(){
    trie tri;
    tri.insert("ABCDE");
    cout << tri.find("ABC") << "\n";
    cout << tri.find("CDE") << "\n";
}