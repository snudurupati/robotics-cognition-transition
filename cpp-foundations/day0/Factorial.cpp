#include <iostream>

int factorial(int); //forward decleration

int main()
{
    int x {10};
    std::cout<< "factorial of " << x <<" is: " << factorial(x) << "\n";
}

int factorial(int n)
{
    for (int i=n; i > 1; i--)
    {
        //std::cout << i <<":"<< n << "\n";
        n = n*(i-1);
    }

    return n;

}
