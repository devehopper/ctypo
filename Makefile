#              Typo Make File
#
#        Script for installing, uninstalling
#   and building Typo programming language from source.
#
#                    - Written with hand by maDeveloper.

all:
	gcc devkit.cpp -o bin/tpm

build:
	gcc devkit.cpp -o bin/tpm

install:
	cp bin/* /usr/bin

uninstall:
	rm -rf /usr/bin/tpm

clean:
	rm -rf bin/
	mkdir bin/