// You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:
//
// record(order_id): adds the order_id to the log
// get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
// You should be as efficient with time and space as possible.

#include <iostream>
#include <random>
#include <vector>

using std::vector;
using namespace std;

// constant time due to use of circular buffer
class Log {
  public:
    vector<int> log;
    int N;
    int cur = 0;

  Log(int n){
    vector<int> log(n);
    N = n;
  }

  void record(int order_id) {
    if (log.size() == N) {
      log[cur] = order_id;
    } else {
      log.push_back(order_id);
    }
    cur = (cur + 1) % N;
  }

  void get_last(int i) {
    if (i > log.size()){
      cout << "Array not large enough";
    }
    if (i > cur){
      cout << "Last: " << log[N-i-cur] << endl;
    } else {
      cout << "Last: " << log[cur-i] << endl;
    }
  }

  void print_log() {
    for (int i:log) {
      cout << i << " ";
    }
    cout << endl;
  }
};


int main() {
  int N = 3;
  Log commerce_log(N);

  commerce_log.record(1);
  commerce_log.record(2);
  commerce_log.record(3);
  commerce_log.record(4);
  commerce_log.record(5);
  commerce_log.record(6);

  // commerce_log.print_log();

  commerce_log.get_last(3);
}

// O(N) time due to reshuffling the list when it is full
// class Log {
//   public:
//     vector<int> log;
//     int N;
//
//   Log(int n){
//     vector<int> log(n);
//     N = n;
//   }
//
//   void record(int order_id) {
//     if (log.size() >= N) {
//       log.erase(log.begin());
//     }
//     log.push_back(order_id);
//   }
//
//   void get_last(int i) {
//     if (i > log.size()){
//       cout << "Array not large enough"
//     }
//     cout << "Last: " << log[log.size()-i] << endl;
//   }
//
//   void print_log() {
//     for (int i:log) {
//       cout << i << " ";
//     }
//     cout << endl;
//   }
// };
