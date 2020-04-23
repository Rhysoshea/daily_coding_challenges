#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n;
    cin >> n;
    vector<int> vect(n);
    for (int i=0; i<n; i++) {
        cin >> vect[i];
    }

    int q;
    cin >> q;

    for (int j=0; j<q; j++) {
        vector<int>::iterator low, up;
        int num;
        cin >> num;
        low=lower_bound (vect.begin(), vect.end(), num); 
        if (low != vect.end() && *low==num){
            cout << "Yes " << (low- vect.begin()+1) << '\n';
        } else {
            cout << "No " << (low- vect.begin()+1) << '\n';
        }

    }





    return 0;
}
