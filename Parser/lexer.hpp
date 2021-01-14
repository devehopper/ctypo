// lexer.hpp
//
// Generate tokens
// and return them.

#pragma once
#ifndef _LEXER_HPP
#define _LEXER_HPP

#include "throw.hpp"
#include "tokens.hpp"
#include "../Include/contains.hpp"

#include <tuple>
#include <string>

typedef std::tuple<std::string, std::string> token_pair;

class Lexer
{
    public:
        std::string sourceCode;

        int lexerPosition;
        char currentCharacter;

        Lexer(std::string sourceCode)
        {
            this->sourceCode = sourceCode;
        }

        void ignoreWhitespace()
        {
            if (stringContains(Token::whitespace, this->sourceCode[this->lexerPosition]))
            {
                this->ignoreWhitespace();
            }
        }

        void advance()
        {
            this->lexerPosition++;

            if (stringContains(Token::whitespace, this->sourceCode[this->lexerPosition]))
            {
                this->ignoreWhitespace();
            }
            else
            {
                this->currentCharacter = this->sourceCode[this->lexerPosition];
            }
            
        }

        std::string scanString(int lexerStringIndicatorLocation, char lexerStringIndicator)
        {
            while (this->sourceCode[lexerStringIndicatorLocation + 1] != lexerStringIndicator)
            {
                this->advance();

                if (this->sourceCode[this->lexerPosition] == lexerStringIndicator)
                {
                    if (this->sourceCode[this->lexerPosition - 1] != '\\')
                    {
                        return this->sourceCode.substr(this->sourceCode[lexerStringIndicatorLocation + 1], this->sourceCode[this->lexerPosition]);
                    }
                }
            }
        }

        std::string scanNumber(int firstNumber, int firstNumberLocation)
        {
            std::string returnValue;

            while (stringContains(Token::number, this->sourceCode[this->lexerPosition]))
            {
                this->advance();

                
            }

            return returnValue;
        }

        token_pair startLexing()
        {
            token_pair returnValue;

            while (this->sourceCode[this->lexerPosition + 1] != '\0')
            {
                this->advance();

                if (stringContains(Token::whitespace, this->currentCharacter))
                {
                    Typo::throw_error("FatalError", "There is a problem in the runtime code.", "Try to update the runtime to latest version.", this->lexerPosition, 128);
                }
                else
                {
                    if (stringContains(Token::punctuation, this->currentCharacter))
                    {
                        returnValue = std::make_tuple(this->currentCharacter, "");
                    }
                    else
                    {
                        if (stringContains(Token::arithmethic_operator, this->currentCharacter))
                        {
                            returnValue = std::make_tuple("operator", this->currentCharacter);
                        }
                        else
                        {
                            if (stringContains(Token::string_indicator, this->currentCharacter))
                            {
                                returnValue = std::make_tuple("string", this->scanString(this->lexerPosition, this->currentCharacter));
                            }
                            else
                            {
                                if (stringContains(Token::number, this->currentCharacter))
                                {
                                    returnValue = std::make_tuple("number", scanNumber(this->currentCharacter, this->lexerPosition));
                                }
                            }
                        }
                    }
                }
            } return returnValue;
        }
};

#endif