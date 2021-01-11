#pragma once
#ifndef _THROW_H
#define _THROW_H

#include "misc/newline.h"

#include <stdio.h>

void throw_error(const char* error_name, const char* error_desc, const char* error_solution, const int error_line, const int error_exit_code) {
    printf("%s at %d.\n", error_name, error_line);
    printf(" %s\n", error_desc);
    printf(" %s\n", error_solution);

    newline;
}

#endif