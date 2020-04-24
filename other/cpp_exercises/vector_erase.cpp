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

    vect.erase(vect.begin() + q - 1);

    int k,p;
    cin >> k >> p;

    vect.erase(vect.begin()+k-1, vect.begin()+p-1 );

    cout << vect.size() << endl;
    for (auto& i : vect) {
        cout << i << " ";
    }

    return 0;
}