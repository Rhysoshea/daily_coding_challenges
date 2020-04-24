// reverse a list in cpp using STL function and my own function 
// raise an error if the list is empty

#include <iostream>
#include <vector>
#include <list>
#include <cmath>
#include <stdexcept>

using namespace std;

void printList(list<int> input) {
    for (auto& i:input) {
        cout << i << " ";
    }
    cout << endl;
}

void printVect(vector<int> input)
{
    for (auto &i : input)
    {
        cout << i << " ";
    }
    cout << endl;
}

// void myReverseList(list<int> input){
//     // list in cpp is a doubly linked list so we want to switch the direction of the pointers
// }

void myReverseVect(list<int> input){
    // try to swap inplace so we don't use additional memory for a vector
    // need to convert list to a vector to be able to access the indices
    try {
        if (input.size() < 1)
        {
            throw std::invalid_argument("received empty list");
        }
    } catch (...) {
        cout << " received empty list" << endl; 
    }


    vector<int> vect;
    for (auto& c: input){
        vect.push_back(c);
    }

    int limit = floor(vect.size() / 2);
    if (vect.size()%2 == 0) {
        limit = floor(vect.size() / 2)-1;
    }

     for (int i = 0; i <=limit; i++)
    {
        int temp = vect[i];
        vect[i] = vect[vect.size()-i-1];
        vect[vect.size()-i-1] = temp;
        printVect(vect);
    }
    printVect(vect);
}

void builtinReverse(list<int> input){
    input.reverse();
    printList(input);
}

int main(){

    list<int> exampleList;

    // builtinReverse(exampleList);
    myReverseVect(exampleList);
    return 0;
}