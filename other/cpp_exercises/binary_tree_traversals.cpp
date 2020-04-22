// implement in-order , pre-order and post-order traverals of a binary tree

//         4
//     2       5
//   1   3

// input
// 5        number of nodes
// 4 1 2    value, index of left, index of right
// 2 3 4
// 5 -1 -1
// 1 -1 -1
// 3 -1 -1

// ouput 
// 1 2 3 4 5 in order (breadth first)
// 4 2 1 3 5 pre order 
// 1 3 2 5 4 post order (depth first)

#include <iostream>
#include <vector>

using namespace std;

struct Node {
    int value;
    Node* left;
    Node* right;
};

Node* newNode(int value){
    Node *node = (Node *)malloc(sizeof(Node));
    node->value = value;
    node->left = node->right = NULL;
    return node;
}

Node* buildTree(vector<int>values, vector<int>left, vector<int>right, Node* root, int i, int n){

    if (i < n) {
        Node* temp = newNode(values[i]);
        root = temp;
        if (left[i] != -1){
            root->left = buildTree(values, left, right, root->left, left[i],n);
        }
        if (left[i] != -1)
        {
            root->right = buildTree(values, left, right, root->left, right[i], n);
        }
    }
    return root;
}

void postOrder(Node* root) {
    if (root != NULL){
        postOrder(root->left);
        postOrder(root->right);
        cout << root->value << " ";
    }
}

void inOrder(Node* root) {
    if (root != NULL){
        inOrder(root->left);
        cout << root->value << " ";
        inOrder(root->right);
    }
}

void preOrder(Node* root) {
    if (root != NULL){
        cout << root->value << " ";
        preOrder(root->left);
        preOrder(root->right);
    }
}

void printVec(vector<int> vect){
    for (auto& i : vect) {
        cout << i << " ";
    }
    cout<< endl;
}

int main() {

    int n;
    cin >> n;

    vector<Node> nodes;
    vector<int> values(n);
    vector<int> left(n);
    vector<int> right(n);

    // receive input
    for (int i=0; i<n; i++){
        cin >> values[i] >> left[i] >> right[i];
    }

    // printVec(values);
    // printVec(left);
    // printVec(right);

    // build tree structure
    Node* root = buildTree(values,left,right,root,0,n);

    inOrder(root);
    cout << endl;
    preOrder(root);
    cout << endl;
    postOrder(root);
    cout << endl;


    return 0;
}