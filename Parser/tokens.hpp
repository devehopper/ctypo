// tokens.hpp
//
// Tokens for use in lexer.

#pragma once
#ifndef _TOKENS_HPP
#define _TOKENS_HPP

#include "constant.hpp"

#include <string>

namespace Token
{
    std::constant whitespace = " \f\n\r\t\v";
    std::constant number = "0123456789";
    std::constant name_character = "qwertyuopasdfghjklizxcvbnm_";
    std::constant arithmethic_operator = "+-/*";
    std::constant punctuation = "(){}[],;=:";
    std::constant string_indicator = "\"'";
}

#endif