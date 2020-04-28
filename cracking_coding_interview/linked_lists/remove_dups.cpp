// Problem: remove duplicates from an unsorted linked list
// keep a set of seen numbers

// Follow up: how would you solve this if a temporary buffer is not allowed?
// use two pointers, one to iterate through the list and a runner pointer which goes down the list each time to check for a match
// this will take N^2 time

// linked list geeks for geeks
// https : //www.geeksforgeeks.org/linked-list-set-1-introduction/

#include <iostream>
#include <vector>
#include <set>

using namespace std;

class Node {
    public:
    Node *next;
    int data;

    Node (int d) {
        data = d;
    }
};

void printList(Node *n) {
    while (n != NULL) {
        cout << n -> data << " ";
        n = n -> next;
    }
    cout << endl;
}

void removeDuplicates(Node *n) {
    set<int> seen;

    while (n != NULL) {
        set<int>::iterator it = seen.find(n -> data);
        if (it != seen.end()) {
            n -> data = n -> next -> data;
            n -> next = n -> next -> next;
        } else {
            seen.insert(n -> data);
            n = n -> next;
        }
    }

}



int main() {

    Node *head = NULL;
    Node *second = NULL;
    Node *third = NULL;
    Node *fourth = NULL;

    head = new Node(2);
    second = new Node(2);
    third = new Node(3);
    fourth = new Node(4);

    head -> next = second;
    second -> next = third;
    third -> next = fourth;
    fourth->next = NULL;

    printList(head);
    removeDuplicates(head);
    printList(head);

    return 0;
}
