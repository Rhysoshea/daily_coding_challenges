#include <iostream>
#include <iomanip> 
using namespace std;

int main() {
	int T; cin >> T;
	cout << setiosflags(ios::uppercase);
	cout << setw(0xf) << internal;
	while(T--) {
		double A; cin >> A; //100.345
        double B; cin >> B; //2006.008
        double C; cin >> C; //2331.41592653498

        cout
            << hex << left << showbase << nouppercase; // formatting
        // prints hexadecimal, left aligned, with '0x' and only lowercase
        cout << (long long) A << endl; // actual printed part
        //0x64

        // LINE 2
        cout << dec << right << setw(15) << setfill('_') << showpos << fixed << setprecision(2); // formatting
        // 2 decimal places, preceded by a + or - sign, right justified, and left-padded with underscores so that the printed result is exactly 15 characters wide.
        //fixed ensures that number is printed out entirely and that scientific notation isn't used for larger numbers
        cout << B << endl; // actual printed part
        // _______+2006.01

        // LINE 3
        cout << scientific << uppercase << noshowpos << setprecision(9); // formatting
        //output in scientific notation format
        //Undo previous nouppercase manipulator and ensures that the 'E' in the scientific notation is capitalised
        //Undo previous showpos manipulator and gets rid of the plus at the start of positive values
        // 9 decimal places (previously set to 2)
        cout << C << endl; // actual printed part
        //2.331415927E+03
    }
	return 0;

}