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

class Log {
  public:
    vector<int> log;
    int N;

  Log(int n){
    vector<int> log(n);
    N = n;
  }

  void record(int order_id) {
    if (log.size() >= N) {
      log.erase(log.begin());
    }
    log.push_back(order_id);
  }

  int get_last(int i) {
    if (i > log.size()){
      cout << "Array not large enough"
      return 0
    }
    return log[log.size()-i];
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

  commerce_log.print_log();

  int last = commerce_log.get_last(4);

  cout << "Last: " << last << endl;

}
