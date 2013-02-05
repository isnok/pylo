##
# The first version of pylo.
# With a Makefile.
#
##

all: parser-3.0.00

parser-3.0.00: contrib/parser-3.0.00
	$(MAKE) -C contrib/$@

contrib/parser-3.0.00: contrib/parser-3.0.00.tar.gz
	cd contrib; tar xf parser-3.0.00.tar.gz

contrib/parser-3.0.00.tar.gz: contrib
	cd contrib; wget -c http://home.ccil.org/~cowan/parser-3.0.00.tar.gz

contrib:
	mkdir -p $@



.PHONY : #all
