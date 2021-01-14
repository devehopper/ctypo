// test.hpp
//
// Some debugging stuff.

#include "test.hpp"

#include <iostream>

int main()
{
    std::cout << "::Starting test...\n";

    if (Typo::Test::test())
    {
        std::cout << "\0333[1;32=>\033[0m Tests finished.\n";
    }
    else
    {
        std::cout << "\0333[1;31=>\033[0m An error occured while testing.\n";
    }
}