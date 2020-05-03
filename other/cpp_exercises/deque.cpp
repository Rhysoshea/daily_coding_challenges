// print out the maximum value of a rolling window in an array

#include <iostream>
#include <deque> 
using namespace std;

void printKMax(int arr[], int n, int k){
	//Write your code here.
    deque<int> deck(k);

    // initially going to push the first window values
    // deque will store the indices of the array
    // going to swap in bigger values at the back
    int i;
    for (i=0; i<k; i++) {
        while ((!deck.empty()) && arr[i] >= arr[deck.back()]){
            deck.pop_back();
        }
        deck.push_back(i);
    }

    for (; i<n; i++) {
        cout << arr[deck.front()] << " "; // the front of deque will always be the maximum of the previous window

        while ((!deck.empty()) && deck.front() <= i-k) {
            deck.pop_front();
        } // removing any indices that are no longer valid in the window

        while ((!deck.empty()) && arr[i] >= arr[deck.back()]) {
            deck.pop_back();
        } // if current value is larger than the minimum one at the back then get rid of the one at back

        deck.push_back(i); // push the latest index
    }

    cout << arr[deck.front()] << endl;
    // print out the max value of the last window

}

int main(){
  
	int t;
	cin >> t;
	while(t>0) {
		int n,k;
    	cin >> n >> k;
    	int i;
    	int arr[n];
    	for(i=0;i<n;i++)
      		cin >> arr[i];
    	printKMax(arr, n, k);
    	t--;
  	}
  	return 0;
}
