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
  Log(int N){
    vector<int> log(N);
  }

  void record(int order_id) {
    log.push_back(order_id);
  }

  int get_last(int i) {
    return log[log.size()-i];
  }

  void print_log() {
    for (int i:log) {
      cout << i << endl;
    }
  }

};


int main() {
  Log commerce_log(10);

  commerce_log.record(1);
  commerce_log.record(2);
  commerce_log.record(3);
  commerce_log.record(4);

  // commerce_log.print_log();

  int last = commerce_log.get_last(2);

  cout << "Last: " << last << endl;

}
