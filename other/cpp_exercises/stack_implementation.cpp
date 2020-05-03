#include <iostream>
#include <vector>

using namespace std;

#define MAX 1000

class Stack{
    int top;

    public:
        int a[MAX]; //maximum size of stack
        Stack()
        {
        top = -1;
        };

        void push(int i){
            if (top >= (MAX-1)){
                cout << "stack overflow" << endl; //stack exceeds allowed maximum
            }
            a[++top] = i; //++i returns the value after it is incremented, while ++i return the value before it is incremented.
            // so it will be a[0] then top = 1
        };

        int pop() {
            if (top < 0) {
                cout << "stack overflow" << endl; // empty stack
                return 0;
            }
            return a[top--];
        };

        int peek() {
            if (top < 0) {
                cout << "stack is empty" << endl;
                return 0;
            }
            return a[top];
        };

        bool isEmpty() {
            return (top < 0);
        };
};


int main() {

    Stack myStack;
    myStack.push(1);
    myStack.push(4);
    myStack.push(2);

    cout << myStack.peek() << endl;
    myStack.pop();
    cout << myStack.peek() << endl;
    myStack.pop();
    cout << myStack.isEmpty() << endl;
    myStack.pop();
    cout << myStack.isEmpty() << endl;

    return 0;
};