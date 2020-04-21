#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
#define MAX_NUM 20001
using namespace std;

int T, M, N;
int check[MAX_NUM];
bool flag;
vector<int> v[MAX_NUM];

void init()
{   
    for (int i = 1; i <= M; i++)
    {
        v[i].clear();
        check[i] = 0;
    }
}

void BFS(int start)
{
    queue<int> q;
    q.push(start);
    check[start] = 1;
    while (!q.empty())
    {
        int c = q.front();
        q.pop();
        for (int i = 0; i < v[c].size(); i++)
        {
            int n = v[c][i];
            if (check[n] == 0)
            { // node n 은 방문한 적이 없음.
                q.push(n);
                check[n] = check[c] * -1;
            }
            else
            { // node n 은 방문한 적이 있음.
                if (check[n] == check[c])
                { // 
                    cout << "NO" << "\n";
                    flag = false; // 이분 그래프가 아님
                    return;
                }
            }
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> T;
    while (T--)
    {
        cin >> M >> N;
        for (int i = 0; i < N; i++)
        {
            int a, b;
            cin >> a >> b;
            v[a].push_back(b);
            v[b].push_back(a);
        }
        for (int i = 1; i <= M; i++)
        {
            if (check[i] == 0 && flag)
            {
                BFS(i);
            }
        }
        if (flag){
            cout << "YES" << "\n";
        }
        init();
    }
    return 0;
}