#pragma once
#ifndef _VM_THREAD_H
#define _VM_THREAD_H

#include "vm.h"

VirtualMachine main_vm = VirtualMachine("main"); // Main Virtual Machine
VirtualMachine fallback_vm = VirtualMachine("fallback"); // Fallback Virtual Machine

#endif