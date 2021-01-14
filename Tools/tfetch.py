#!/usr/bin/env python3

# tfetch.py
#
# Command line utility
# to fetch information about
# installed Typo version.

import os
import socket

EDITION = 'C'
VERSION = "0:0.1"

print("""      ___     
     /\\  \\        %s Typo v%s
     \\:\\  \\     =========%s
      \\:\\  \\     Typo: %s Typo %s on %s
      /::\\  \\    Host: %s
     /:/\\:\\__\\
    /:/  \\/__/
   /:/  /     
   \\/__/      
              
              
""" % (
    EDITION,
    VERSION,
    "=" * (len(VERSION) + 1),
    EDITION,
    VERSION,
    os.name.upper(),
    socket.gethostname() + "/" + socket.gethostbyname(
    socket.gethostname()
    )
)
)
