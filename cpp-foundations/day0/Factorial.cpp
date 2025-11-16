//factorial function using for loop

int factorial(int n)
{
    for (int i=n; i > 1; i--)
    {
        //std::cout << i <<":"<< n << "\n";
        n = n*(i-1);
    }

    return n;

}
