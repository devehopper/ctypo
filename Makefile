#              Typo Make File
#
#        Script for installing, uninstalling
#   and building Typo programming language from source.
#
#                    - Written with hand by maDeveloper.

all:
	g++ console.c -o bin/tcon

build:
	g++ console.c -o bin/tcon

install:
	cp bin/* /usr/bin

uninstall:
	rm -rf /usr/bin/tcon

clean:
	rm -rf bin/
	mkdir bin/