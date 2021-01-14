// throw.hpp
//
// Throws error and
// terminates the process.

#pragma once
#ifndef _THROW_HPP
#define _THROW_HPP

#include "terminate.hpp"

#include <string>
#include <iostream>

namespace Typo
{
    void throw_error(std::string _err_name, std::string _err_desc, std::string _err_sln, int _err_pos, int _err_exit_code)
    {
        std::cout << "\033[31m" << _err_name << "\033[0m at \033[33m" << _err_pos << "\033[33m.\n";
        std::cout << " " << _err_desc << "\n";
        std::cout << " " << _err_sln << "\n";

        Typo::terminate(_err_exit_code);
    }
}

#endif