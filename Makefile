##
# The first version of pylo.
# With a Makefile to install
# the dependencies.
##

all: parser-3.0.00 jbofihe-deb

jbofihe: contrib/jbofihe
	cd contrib/jbofihe; ./configure
	$(MAKE) -C contrib/jbofihe all

contrib/jbofihe:
	git clone https://github.com/rc0/jbofihe.git $@

contrib/pybison-0.1.8: contrib/pybison-0.1.8.tar.gz
	cd contrib; tar xf pybison-0.1.8.tar.gz

contrib/pybison-0.1.8.tar.gz: contrib
	cd contrib; wget -c http://web.archive.org/web/20100526152350/http://www.freenet.org.nz/python/pybison/pybison-0.1.8.tar.gz

jbofihe-deb:
	aptitude install jbofihe ||\
	apt-get install jbofihe

parser-3.0.00: contrib/parser-3.0.00
	$(MAKE) -C contrib/$@

contrib/parser-3.0.00: contrib/parser-3.0.00.tar.gz
	cd contrib; tar xf parser-3.0.00.tar.gz

contrib/parser-3.0.00.tar.gz: contrib
	cd contrib; wget -c http://home.ccil.org/~cowan/parser-3.0.00.tar.gz

contrib:
	mkdir -p $@



.PHONY : all
