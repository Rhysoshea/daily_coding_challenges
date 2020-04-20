// https: //www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

// first implement a queue using two stacks. Then process q queries, where each query is one of the following types :

// input 
// number of queries q
// query type 
// 1 x : enqueue x into the queue
// 2: dequeue element at front of the queue
// 3: print element at front of the queue

// solution: keep pushing to one stack always
// when it comes time to pop or print out the top, if the other stack is empty push everything from one stack to the other, this will reverse the order
// only when the reversed stack is empty does everything need to be shifted over again as the stack is in correct order
// meanwhile the other stack is filling up in reverse order again which can be flipped when the reverse stack becomes empty


#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
using namespace std;

class MyQueue
{

public:
    stack<int> stack_newest_on_top, stack_oldest_on_top;
    void push(int x)
    {
        stack_newest_on_top.push(x);
    }

    void pop()
    {
        if (stack_oldest_on_top.empty()){
            while (!stack_newest_on_top.empty()){
                int n = stack_newest_on_top.top();
                stack_newest_on_top.pop();
                stack_oldest_on_top.push(n);
            }
            stack_oldest_on_top.pop();

        } else {
            stack_oldest_on_top.pop();
        }
    }

    int front()
    {
        if (stack_oldest_on_top.empty()){
            while (!stack_newest_on_top.empty()) {
                int n = stack_newest_on_top.top();
                stack_newest_on_top.pop();
                stack_oldest_on_top.push(n);
            }
        }
        return stack_oldest_on_top.top();
    }
};

int main()
{
    MyQueue q1;
    int q, type, x;
    cin >> q;

    for (int i = 0; i < q; i++)
    {
        cin >> type;
        if (type == 1)
        {
            cin >> x;
            q1.push(x);
        }
        else if (type == 2)
        {
            q1.pop();
        }
        else
            cout << q1.front() << endl;
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    return 0;
}