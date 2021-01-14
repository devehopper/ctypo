// contains.hpp
//
// Check does string
// contains a character.

#pragma once
#ifndef _CONTAINS_HPP
#define _CONTAINS_HPP

#include <string>

bool stringContains(std::string string, char character)
{
    if (string.find(character) != -1)
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool stringDoesNotContains(std::string string, char character)
{   
    if (string.find(character) != -1)
    {
        return false;
    }
    else
    {
        return true;
    }
}

#endif