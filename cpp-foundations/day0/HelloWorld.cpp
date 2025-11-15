#include <iostream>

int main()
{
    std::cout << "Hello, World\n";

    //initialization types
    int a = 5.1; //copy initialization(C-style, implicit type conversion and data truncation)
    int b {3}; //direct list initialization(preferred)
    double c (6.6); //direct initialization
    char d {}; //value initialization or zer0-initialization
    [[maybe_unused]] double pi {3.14159}; //unused variable

    std::cout << a << ", " << b << ", " << c << ", " << d << "\n"; // \n doesnt just adds a new line
    std::cout << sizeof(int) <<" bytes\n"; //prints the size of of int on this machine and this compiler
    std::cout << "bye now!" << std::endl; //endl flushes the buffer
}