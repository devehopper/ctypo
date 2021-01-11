#pragma once
#ifndef _TERMINATE_H
#define _TERMINATE_H

#include "vm.h"

#include <stdio.h>
#include <stdlib.h>

void terminate(int exit_code, VirtualMachine vm) {
    if (exit_code != 0) {
        printf("\n [ Process terminated with code %d. ] \n", exit_code);
    }

    vm.shut();
    exit(exit_code);
}

void terminate(int exit_code) {
    if (exit_code != 0) {
        printf("\n [ Process terminated with code %d. ] \n", exit_code);
    }

    exit(exit_code);
}

#endif