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


using std::vector;
using namespace std;

struct Node {
  string name;
  bool file;
  int path_length;
  int id;
  Node *parent;
  vector<Node *> children;
  void set_path_length();
  void is_file();

  Node (string name_, int id_) :
  name(name_),
  id(id_)
  // parent(parent_)
  {}

};

void Node::set_path_length() {
  path_length = parent->path_length + name.size();
}

void Node::is_file() {
  if (name.find(".") != string::npos){
    file = true;
  } else {
    file = false;
  }
}

class Tree {
  public:
    vector<Node> tree;
    int size = tree.size();

  void add_to(Node node) {
    tree.push_back(node);
  }

  Node get_node(int id) {
    return tree[id];
  }

  void print_all(){
    for (Node i:tree){
      cout << i.name << endl;
    }
  }
};

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

int main() {
  string path = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext";

  vector<string> items = split(path);

  Tree directory;

  for (string i:items) {
    directory.add_to(Node(i, directory.size ));
  }

  directory.print_all();

}
