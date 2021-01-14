// terminate.hpp
//
// Terminates program
// without throwing any error.

#pragma once
#ifndef _TERMINATE_HPP
#define _TERMINATE_HPP

#include <cstdlib>
#include <iostream>

namespace Typo
{
    void terminate()
    {
        exit(0);
    }

    void terminate(int _err_exit_code)
    {
        if (_err_exit_code != 0)
        {
            std::cout << "\n [ Process terminated with code \033[31m" << _err_exit_code << "\033[0m. ] \n";
        }

        exit(_err_exit_code);
    }
}

#endif