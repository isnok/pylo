##
# The first version of pylo.
# With a Makefile to install
# the dependencies.
##

CONTRIB = parser-3.0.00 pybison-0.1.8 jbofihe
CONTRIB_TGTS = $(patsubst %,contrib/%,$(CONTRIB))

all: pip-stuff $(CONTRIB_TGTS) jbofihe-deb

pip-stuff:
	pip install Pyrex commandwrapper

jbofihe-git: contrib/jbofihe
	cd contrib/jbofihe; ./configure
	$(MAKE) -C contrib/jbofihe all

contrib/jbofihe:
	git clone https://github.com/rc0/jbofihe.git $@

contrib/%: contrib/%.tar.gz
	cd contrib; tar xf $(subst contrib/,,$@)

pybison-0.1.8: contrib/pybison-0.1.8
	pip install contrib/pybison-0.1.8.tar.gz

contrib/pybison-0.1.8.tar.gz: contrib
	cd contrib; wget -c http://web.archive.org/web/20100526152350/http://www.freenet.org.nz/python/pybison/pybison-0.1.8.tar.gz

contrib/parser-3.0.00.tar.gz: contrib
	cd contrib; wget -c http://home.ccil.org/~cowan/parser-3.0.00.tar.gz

jbofihe-deb:
	aptitude install jbofihe ||\
	apt-get install jbofihe

parser-3.0.00: contrib/parser-3.0.00
	$(MAKE) -C contrib/$@

contrib:
	mkdir -p $@

.PHONY : all
