#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cassert>
using namespace std;

// Write your Student class here

// alternative approach
// sets a variable sum to 0 when constructor is called
// calculates sum as values are read in
class Student {
  private:
    int scores[5];
    int sum;
  public:
    Student() : sum(0) {} // called 'initializer list'
    int calculateTotalScore() {return sum;}
    void input() {
        for(int i=0; i<5; i++) {
            cin >> scores[i];
            sum+=scores[i];
        }
    }
};


// initial approach
class Student {
    vector<int> scores;

    public:

    void input(){
        for (int i=0; i<5 ; i++){
            int score;
            cin >> score;
            scores.push_back(score);
        }
    }
    int calculateTotalScore(){
        int total=0;
        for (auto& i : scores){
            // cout << i << endl;
            total += i;
        }
        return total;
    }

};

int main() {