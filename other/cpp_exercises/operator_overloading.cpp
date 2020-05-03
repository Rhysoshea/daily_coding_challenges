//Operator Overloading

#include<iostream>

using namespace std;

class Complex
{
public:
    int a,b;
    void input(string s)
    {
        int v1=0;
        int i=0;
        while(s[i]!='+')
        {
            v1=v1*10+s[i]-'0';
            i++;
        }
        while(s[i]==' ' || s[i]=='+'||s[i]=='i')
        {
            i++;
        }
        int v2=0;
        while(i<s.length())
        {
            v2=v2*10+s[i]-'0';
            i++;
        }
        a=v1;
        b=v2;
    }
};

//Overload operators + and << for the class complex
//+ should add two complex numbers as (a+ib) + (c+id) = (a+c) + i(b+d)
//<< should print a complex number in the format "a+ib"

// Complex operator+(const Complex& one, const Complex& two) {
//     return {one.a+two.a , one.b+two.b};
// };

Complex operator+(Complex& obj1 , Complex& obj2){
    Complex t ;
     t.a = obj1.a + obj2.a;
     t.b = obj1.b + obj2.b;
     return t;
}
ostream& operator <<(ostream& out , const Complex& obj){
    out<<obj.a<<"+i"<<obj.b<<endl;
    return out;
}

// const stops any accidental data change
// & makes it so we are dealing with the same object and not a copy

int main()
{
    Complex x,y;
    string s1,s2;
    cin>>s1;
    cin>>s2;
    x.input(s1);
    y.input(s2);
    Complex z=x+y;
    cout<<z<<endl;
}
