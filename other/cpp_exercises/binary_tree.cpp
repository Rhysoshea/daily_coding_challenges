// create a binary tree using classes
// print out the values of the tree using DFS

#include <iostream>
#include <vector>

using namespace std;

struct Node {
    public:
        int value;
        Node *left;
        Node *right;

};

Node* newNode(int value){

    Node *node = (Node *)malloc(sizeof(Node));
    node->value = value;
    node->left = node->right = NULL;
    return node;
}

class BinaryTree {
    public:

    Node* buildLevelOrder(vector<int> vect, Node* root, int start, int end){
        if (start < end)   {
            Node* temp = newNode(vect[start]);
            root = temp;
            root->left = buildLevelOrder(vect, root->left, (2*start)+1, end);

            root->right = buildLevelOrder(vect, root->right, (2*start)+2, end);
        }

        return root;
    }

    void bfsOrder(Node* root){

        if (root!=NULL) {
            bfsOrder(root->left);
            cout << root->value << " ";
            bfsOrder(root->right);
        }
    }

    void dfsOrder(Node *root)
    {

        if (root != NULL)
        {
            dfsOrder(root->left);
            dfsOrder(root->right);
            cout << root->value << " ";
        }
    }

};


int main() {

    //         1
    //     2       3
    // 4      5 6      7

    // printing by DFS should show 4,5,2,6,7,3,1
    // printing by BFS should show 4,2,5,1,6,3,7

    vector<int> vect {1,2,3,4,5,6,7};
    // index is value of node, value in vector is parent index

    BinaryTree tree;
    
    Node* root = tree.buildLevelOrder(vect, root, 0, vect.size());

    tree.bfsOrder(root);
    cout << endl;
    tree.dfsOrder(root);



    return 0;
}