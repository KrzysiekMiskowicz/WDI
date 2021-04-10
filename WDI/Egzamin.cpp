#include <iostream>
using namespace std;

int f(int n){
if (n<2) return n;
return abs(n%2-f(n/2));
}

int main()
{
    /*
    for(int i = 1; i < 10; i++)
        cout << f(i) << endl;
    */
    float a = 1;
    float digit = 1;
    int acc = 0;
    while(true)
    {
        a /= 10;
        digit *= 10;
        cout << a * digit << endl;
        if(int(a * digit) != 1)
            break;
        acc += 1;
    }
    cout << acc;
    cout << a;
    cout << digit;
}


