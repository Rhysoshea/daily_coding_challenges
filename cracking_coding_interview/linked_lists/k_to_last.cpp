// Problem: return the Kth to last element in a singly linked list

#include <iostream>

using namespace std;


class Node {
    public:
    int data;
    Node *next;

    Node (int d) {
        data = d;
    }
};

Node *kthLast(Node *n, int k){
    Node *slow = n;
    Node *fast = n;

    for (int i=0; i<k; i++){
        fast = fast -> next;
    }

    while (fast != NULL) {
        slow = slow -> next;
        fast = fast -> next;
    }
    return slow;

};

int main() {

    Node *head = new Node(1);
    Node *two = new Node(2);
    Node *three = new Node(3);
    Node *four = new Node(4);

    head -> next = two;
    two -> next = three;
    three -> next = four;
    four -> next = NULL;

    int k = 2;

    Node *n = kthLast(head, k);

    cout << n -> data << endl;


    return 0;
}