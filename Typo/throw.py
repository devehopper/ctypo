from colored import fg
from colored import stylize
from terminate import terminate
import sys

def throw(_err_name: str, _err_desc: str, _err_sln: str, _err_pos: int, _err_exit_code: int):
    print("%s at %d." % stylize(_err_name, fg("red")), stylize(_err_pos, fg("yellow")))
    print(" %s" % _err_desc)
    print(" %s" % _err_sln)
    print()

    terminate(_err_exit_code)
