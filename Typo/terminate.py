# terminate.py
#
# Terminate using
# terminate(exit_code: int)
# function.

from colored import fg
from colored import stylize

def terminate(exit_code: int):
    if (exit_code != 0):
        print("\n [ Process terminated with code %d. ] " % stylize(exit_code, fg("red")))

    exit(1)
