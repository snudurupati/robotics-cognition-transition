#include <iostream>

using namespace std;

double getUserInput ()
{
    double x;
    cout <<"Enter a number:";
    cin >> x;
    return x;
}

double square(double x)
{
    return x*x;
}

int main() 
{
    double n = getUserInput();
    cout << "the square of " << n <<" is: " << square(n) << "\n";
}