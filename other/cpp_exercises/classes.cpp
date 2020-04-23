#include <iostream>
#include <sstream>
using namespace std;

/*
Enter code for class Student here.
Read statement for specification.
*/  

class Student {
        int age;
        string first_name;
        string last_name;
        int standard;
    public:
        Student()
        {
        age = 0;
        standard = 0;
        first_name.clear();
        last_name.clear();
        }
        int get_age(){ return age; }; 
        void set_age(int a) {
            age = a;
        };
        string get_first_name() { return first_name; };
        void set_first_name(string first){
            first_name = first;
        };
        string get_last_name() { return last_name; };
        void set_last_name(string last){
            last_name = last;
        };
        int get_standard(){ return standard; }; 
        void set_standard(int a) {
            standard = a;
        };

        string to_string(){
            stringstream ss;
            char c = ',';
            ss << age << c << first_name << c << last_name << c << standard;

            return ss.str();
        }
    
};

int main() {
    int age, standard;
    string first_name, last_name;
    
    cin >> age >> first_name >> last_name >> standard;
    
    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);
    
    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    cout << st.to_string();
    
    return 0;
}
