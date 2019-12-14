 // Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
#include <iostream>
#include <random>
#include <vector>

using std::vector;
using namespace std;

int random_element(vector<int> stream) {
  int el;
  for (int i=0; i < stream.size(); ++i) {
    if (rand()%(i+1)+1 == 1) {
      el = stream[i];
    }
  }
  return el;
}

int random_generator(){
  return rand()%10+1;
}

int main() {
  int n = 10000; //number of iterations to run code
  vector<int> count(10,0); //numbers range from 1 to 10

  // outer loop is a check to see if random element has any bias
  for (int i=0; i<n; ++i) {
    vector<int> stream;
    for (size_t i=0; i<n; ++i){
      stream.push_back(random_generator());
    }
    int el = random_element(stream);
    count[el-1] += 1;
    // cout << "The random element is " << el << endl;
  }

  for (int i=0; i<count.size(); ++i){
    cout << "Number: " << i+1 << " count: " << count[i] << endl;
  }

}
