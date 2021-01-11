#pragma once
#ifndef _STDUTIL_H
#define _STDUTIL_H

#include <stdlib.h>
#include <string.h>

#ifndef _WIN32
void rmdir(const char* directory) {
    char *command = (char*)malloc(strlen("rm -rf ") + strlen(directory) + 1);
    strcpy(command, "rm -rf ");
    strcat(command, directory);

    system(command);
}
#else
void rmdir(const char* directory) {
    char *command = (char*)malloc(strlen("del /s /q ") + strlen(directory) + 1);
    strcpy(command, "del /s /q ");
    strcat(command, directory);

    system(command);
}
#endif

char* stradd(const char* first_string, const char* second_string) {
    char* result_string = (char*)malloc(strlen(first_string) + strlen(second_string) + 1);
    strcpy(result_string, first_string);
    strcat(result_string, second_string);

    return result_string;
}

#endif