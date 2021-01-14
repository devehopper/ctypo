# Makefile
#
# Compiles and installs
# or uninstalls the Typo.
# Only for Linux.

all:
	g++ Typo/runtime.hpp -o Bin/runtime.out
	g++ Tests/test.cpp -o Bin/test.out

build:
	g++ Typo/runtime.hpp -o Bin/runtime.out
	g++ Tests/test.cpp -o Bin/test.out

install:
	mkdir -p /usr/lib/ctypo/runtime/
	cp -r Typo/*.py /usr/lib/ctypo/
	cp -r Bin/runtime.out /usr/lib/ctypo/runtime/

uninstall:
	rm -rf /usr/lib/ctypo/

clean:
	rm -rf Bin/
	mkdir Bin/

test:
	@./Bin/test.out
