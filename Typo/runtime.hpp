// runtime.hpp
//
// Typo binary

#ifndef _RUNTIME_HPP
#define _RUNTIME_HPP

#include "../Parser/lexer.hpp"

#include <fstream>

int main(int argc, char *argv[])
{
    std::string sourceFileContent;

    std::ifstream sourceFile ("src/main.typo");
    sourceFile >> sourceFileContent;

    sourceFile.close();

    Lexer lexer = Lexer(sourceFileContent);
}

#endif