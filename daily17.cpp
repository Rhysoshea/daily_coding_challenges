// Suppose we represent our file system by a string in the following manner:
//
// The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
//
// dir
//     subdir1
//     subdir2
//         file.ext
// The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
//
// The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
//
// dir
//     subdir1
//         file1.ext
//         subsubdir1
//     subdir2
//         subsubdir2
//             file2.ext
// The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
//
// We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).
//
// Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.
//
// Note:
//
// The name of a file contains at least a period and an extension.
//
// The name of a directory or sub-directory will not contain a period.

#include <iostream>
#include <random>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include <stack>


using std::vector;
using namespace std;

class Node {
public:
  string name;
  bool file;
  int path_length;
  int id;
  Node *parent;
  vector<Node *> children;

  Node (string name_) {
    this->name = name_;
    // this->parent = NULL;
  }

  void setParent(Node *theParent){
    this->parent = theParent;
    // cout << this->name << " parent: " << parent->name << endl;
    parent->children.push_back(this);
  }

  void set_path_length() {
    this->path_length = parent->path_length + name.size();
  }

  void is_file() {
    if (name.find(".") != string::npos){
      file = true;
    } else {
      file = false;
    }
  }

};


void print_all(vector<Node> tree){
  for (Node i:tree){
    int indents = 0;
    while(i.name.find("\t") != string::npos){
      indents++;
      i.name = i.name.substr(1,i.name.size());
    }
    // cout << i.name << " indents: " << indents << endl;
    cout << i.name <<  endl; //" parent: " << i.parent->name << endl;

  }
}

void print_path(vector<Node> tree){
  for (Node i:tree){
    cout << i.name << " path: " << i.path_length << endl;
  }
}

vector<string> split(const string& str, char delim = '\n') {
    vector<string> cont;
    std::size_t current, previous = 0;
    current = str.find(delim);
    while (current != std::string::npos) {
        cont.push_back(str.substr(previous, current - previous));
        previous = current + 1;
        current = str.find(delim, previous);
    }
    cont.push_back(str.substr(previous, current - previous));

    return cont;
}

int check_indents(Node i){
  int indents = 0;
  while(i.name.find("\t") != string::npos){
    indents++;
    i.name = i.name.substr(1,i.name.size());
  }
  return indents;
}


int main() {
  string path = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext";

  vector<string> items = split(path);

  vector<Node> directory;

  stack<Node> q;
  int depth = 0;
  Node current_node(items[0]);
  directory.push_back(current_node);

  q.push(current_node);
  Node current_parent = q.top();
  items.erase(items.begin());

  current_node.setParent(&current_parent);
  current_node.set_path_length();

  cout << current_node.name << " " << check_indents(current_node) << " " << depth << endl;


  for (string s:items) {
    Node current_node(s);
    cout << current_node.name << " " << check_indents(current_node) << " " << depth << endl;

    if (check_indents(current_node) > depth) {
      current_parent = q.top();
      depth = check_indents(current_node);
      q.push(current_node);
      // cout << "current parent: " << current_parent.name << endl;

    } else if (check_indents(current_node) < depth) {
      for (int i=0; i<depth; i++){
        // cout << i << endl;
        q.pop();
        // cout << q.top().name << endl;
      }
      current_parent = q.top();
      // cout << "current parent: " << current_parent.name << endl;
      depth = check_indents(current_node);
    }

    directory.push_back(current_node);
    current_node.setParent(&current_parent);
    current_node.set_path_length();
    current_node.is_file();


  }

  print_all(directory);
  // print_path(directory);
  // for (Node i : directory){
  //   cout << i.parent->name << endl;
  // }
  cout << directory[2].name << endl;

}
