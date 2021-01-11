#pragma once
#ifndef _VM_H
#define _VM_H

#include "stdutil.h"

#include <string.h>
#include <stdlib.h>

struct VirtualMachine {
    char* name;

    VirtualMachine(char* name) {
        this->name = name;
    }

    void shut() {
        char *command = (char*)malloc(strlen(".typo/vm/") + strlen(this->name) + 1);
        strcpy(command, ".typo/vm/");
        strcat(command, this->name);

        rmdir(command);
    }

    void shut(int exit_code) {
        char *command = (char*)malloc(strlen(".typo/vm/") + strlen(this->name) + 1);
        strcpy(command, ".typo/vm/");
        strcat(command, this->name);

        rmdir(command);

        exit(exit_code);
    }
};

#endif