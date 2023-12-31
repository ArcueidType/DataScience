# Generated automatically from Makefile.in by configure.
#   Generated automatically from Makefile.in by configure.
#
#   Makefile for the "Bag Of Words Library", libbow.
#   Copyright (C) 1996, 1997, 1998, 1999 Andrew McCallum
#
#   Written by:  Andrew Kachites McCallum <mccallum@cs.cmu.edu>
#   Date: September 1996
#
#   This file is part of the Bag-Of-Words Library, `libbow'.
#
#   This library is free software; you can redistribute it and/or
#   modify it under the terms of the GNU Library General Public
#   License as published by the Free Software Foundation; either
#   version 2 of the License, or (at your option) any later version.
#   
#   This library is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   Library General Public License for more details.
#
#   You should have received a copy of the GNU Library General Public
#   License along with this library; if not, write to the Free
#   Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

SHELL = /bin/sh

#### Start of system configuration section. ####

default: all

srcdir = .
RANLIB = ranlib
INSTALL = /usr/bin/install -c
INSTALL_PROGRAM = ${INSTALL}
INSTALL_DATA = ${INSTALL} -m 644
MAKEINFO = makeinfo
TEXI2DVI = texi2dvi
PERL = /usr/bin/perl
YACC = bison -y
FLEX = flex

CC = gcc

DEFS =  -DHAVE_STRERROR=1 -DHAVE_GETTIMEOFDAY=1 -DHAVE_RANDOM=1 -DHAVE_SRANDOM=1 -DHAVE_SETENV=1 -DHAVE_STRCHR=1 -DHAVE_STRRCHR=1 -DHAVE_LOG2F=1 -DHAVE_SQRTF=1 -DHAVE_ALLOCA_H=1 -DCONSTRUCTOR_FAILS=1 
LIBS = 

# All these are optional.  You can redifine CFLAGS, CPPFLAGS,
# INCLUDEFLAGS and LDFLAGS on the command line however you like.
CFLAGS = -g -O -Wall -Wimplicit
CPPFLAGS = 
INCLUDEFLAGS =
LDFLAGS =

prefix = /usr/local
exec_prefix = ${prefix}

# Installation locations
bindir = $(exec_prefix)/bin
libdir = $(exec_prefix)/lib
includedir = $(prefix)/include/bow
infodir = $(prefix)/info

#### End of system configuration section. ####

HAVE_PR_LOQO = \
$(shell if ((test -f pr_loqo.c) && (test -f bow/pr_loqo.h)) ; then echo true ; else echo false ; fi)

ifeq ($(HAVE_PR_LOQO),true)
DEFS += -DHAVE_LOQO
SVM_FILES = svm_smo.c svm_al.c svm_trans.c svm_fisher.c svm_loqo.c
PR_LOQO = pr_loqo.c
else
SVM_FILES = svm_smo.c svm_al.c svm_trans.c svm_fisher.c
endif

include $(srcdir)/Version
-include $(srcdir)/Makefile.preamble
-include Makefile.local

# convenience lex and yacc filename conversion rules:
LEX_RULE = _lex.c
Y_RULE = _y.c

DEMO_EXECUTABLES = rainbow arrow archer crossbow 

all: libbow.a $(DEMO_EXECUTABLES) $(PERL_RUNNABLE_FILES) kl-div

%.o: %.c
	$(CC) -c $(ALL_CPPFLAGS) $(ALL_CFLAGS) -o $@ $<
%$(LEX_RULE): %.lex
	$(FLEX) -o$@ -P$(basename $<)_ $<
%$(Y_RULE): %.y
	$(YACC) -d -o$@ -p$(basename $<)_ $<

# cancel the default .y->.c rule --- otherwise it gives us trouble
# because we have both archer_query.c and archer_query.y 
%.c: %.y


# Pattern rule
ALL_CPPFLAGS = $(CPPFLAGS) $(INCLUDEFLAGS) -Ibow -I$(srcdir) -I$(srcdir)/argp $(DEFS)
ALL_CFLAGS = $(CFLAGS)
ALL_LIBS = $(LIBS) -L. -lbow -L./argp -largp -lm -lcrypt


# Libbow section

STANDARD_LIBBOW_H_FILES = \
bow/libbow.h 

LIBBOW_H_FILES = $(STANDARD_LIBBOW_H_FILES)

STANDARD_LIBBOW_C_FILES = \
array.c \
barrel.c \
bitvec.c \
bmalloc.c \
deflexer.c \
dv.c \
docnames.c \
email.c \
error.c \
evi.c \
foilgain.c \
goodturing.c \
heap.c \
info_gain.c \
int4docn.c \
int4str.c \
int4word.c \
io.c \
istext.c \
lex-gram.c \
lex-html.c \
lex-next.c \
lex-suffixing.c \
lex-simple.c \
methods.c \
next.c \
normalize.c \
opts.c \
primelist.c \
primes.c \
random.c \
sarray.c \
scale.c \
scan.c \
split.c \
stem.c \
stoplist.c \
stopwords.c \
strtrie.c \
vpc.c \
wa.c \
wicoo.c \
wi2dvf.c \
wv.c 

# note - a library with pr_loqo shouldn't be distributed
LIBBOW_C_FILES = $(STANDARD_LIBBOW_C_FILES) $(PR_LOQO)

$(LIBBOW_C_FILES): $(LIBBOW_H_FILES)

LIBBOW_O_FILES = $(LIBBOW_C_FILES:.c=.o)

libbow.a: $(LIBBOW_O_FILES) $(METHOD_O_FILES)
	$(AR) rc $@ $^
	$(RANLIB) $@

argp/libargp.a:
	cd argp ; $(MAKE) libargp.a

# libbow.h has macros that indicate the libbow's version number; these
# must be kept up-to-date.
bow/libbow.h: Version
	rm -f bow/libbow-tmp.h~
	mv bow/libbow.h bow/libbow-tmp.h~
	cat bow/libbow-tmp.h~ | sed -e \
	's/e BOW_MAJOR_VERSION .*/e BOW_MAJOR_VERSION $(BOW_MAJOR_VERSION)/' \
	| sed -e \
	's/e BOW_MINOR_VERSION .*/e BOW_MINOR_VERSION $(BOW_MINOR_VERSION)/' \
	> $@

# The compiled functions in these files are defined entirely by libbow.h.
io.o bmalloc.o: bow/libbow.h

LIBBOW_DIST_FILES = \
$(STANDARD_LIBBOW_C_FILES) \
$(STANDARD_LIBBOW_H_FILES)


# Perl section

PERL_FILES = \
rainbow-ac.pl \
rainbow-be.pl \
rainbow-pr.pl \
rainbow-rank.pl \
rainbow-stats.pl

PERL_RUNNABLE_FILES = $(PERL_FILES:.pl=)

$(PERL_RUNNABLE_FILES): %: %.pl
	rm -f $@
	cat $< | sed -e 's,/usr/bin/perl,${PERL},' > $@
	chmod a+x $@

PERL_DIST_FILES = \
$(PERL_FILES)


# Documentation section

DOC_TEXI_FILES = \
libbow.texi \
rainbow.texi \

DOC_INFO_FILES = $(DOC_TEXI_FILES:.texi=.info)
DOC_DVI_FILES = $(DOC_TEXI_FILES:.texi=.dvi)

OTHER_TEXI_FILES = \
libbow-desc.texi \
install.texi \
readme.texi \
version.texi

MAKEINFO_FLAGS = -I $(srcdir)
%.dvi: %.texi version.texi
	$(TEXI2DVI) $(srcdir)/$*.texi
%.info: %.texi version.texi
	$(MAKEINFO) $(MAKEINFO_FLAGS) $(srcdir)/$*.texi
INSTALL: install.texi version.texi
	$(MAKEINFO) $(MAKEINFO_FLAGS) -o INSTALL -D INSTALL_ONLY \
	--no-header --no-split $(srcdir)/install.texi
README: readme.texi version.texi
	$(MAKEINFO) $(MAKEINFO_FLAGS) -o README -D README_ONLY \
	--no-header --no-split $(srcdir)/readme.texi

version.texi: $(srcdir)/Version
	rm -f version.texi
	echo '@set BOWVERSION' $(BOW_VERSION) \
		> version.texi
	if [ $(BOW_FTP_MACHINE) ]; then \
		echo '@set BOW_FTP_MACHINE $(BOW_FTP_MACHINE)' \
		>> version.texi; fi
	if [ $(LIBBOW_FTP_DIRECTORY) ]; then \
		echo '@set BOW_FTP_DIRECTORY $(BOW_FTP_DIRECTORY)' \
		>> version.texi; fi

DOC_DIST_FILES = \
$(DOC_TEXI_FILES) \
$(OTHER_TEXI_FILES) \
HACKING \
INSTALL \
NEWS \
README \
TODO 

# Rainbow section

STANDARD_RAINBOW_METHOD_C_FILES = \
active.c \
deflexer.c \
em.c \
emsimple.c \
kl.c \
knn.c \
maxent.c \
naivebayes.c \
nbshrinkage.c \
nbsimple.c \
prind.c \
tfidf.c \
svm_base.c $(SVM_FILES)

STANDARD_RAINBOW_METHOD_H_FILES = \
bow/nbsimple.h \
bow/em.h \
bow/kl.h \
bow/knn.h \
bow/naivebayes.h \
bow/prind.h \
bow/svm.h \
bow/tfidf.h

RAINBOW_METHOD_C_FILES += $(STANDARD_RAINBOW_METHOD_C_FILES)
RAINBOW_METHOD_O_FILES += $(RAINBOW_METHOD_C_FILES:.c=.o)

RAINBOW_C_FILES += \
rainbow.c \
$(RAINBOW_METHOD_C_FILES)

RAINBOW_O_FILES = $(RAINBOW_C_FILES:.c=.o)

foo1: $(RAINBOW_O_FILES)
	echo $^
	echo $(RAINBOW_O_FILES)


rainbow: libbow.a argp/libargp.a $(RAINBOW_O_FILES)
	$(CC) $(CFLAGS) -o $@ $(RAINBOW_O_FILES) $(LDFLAGS) $(ALL_LIBS)


RAINBOW_DIST_FILES = \
rainbow.c \
$(STANDARD_RAINBOW_METHOD_H_FILES) \
$(STANDARD_RAINBOW_METHOD_C_FILES)


# Arrow section

ARROW_METHOD_C_FILES = \
tfidf.c

ARROW_METHOD_O_FILES = $(ARROW_METHOD_C_FILES:.c=.o)

arrow: libbow.a argp/libargp.a arrow.o $(ARROW_METHOD_O_FILES)
	$(CC) $(CFLAGS) $@.o -o $@ $(ARROW_METHOD_O_FILES) $(LDFLAGS) $(ALL_LIBS)

ARROW_DIST_FILES = \
arrow.c


# Crossbow section

STANDARD_CROSSBOW_H_FILES = \
bow/crossbow.h \
bow/treenode.h 

STANDARD_CROSSBOW_C_FILES = \
crossbow.c \
hem.c \
multiclass.c \
treenode.c 

CROSSBOW_H_FILES = $(STANDARD_CROSSBOW_H_FILES)
CROSSBOW_C_FILES = $(STANDARD_CROSSBOW_C_FILES)

CROSSBOW_O_FILES = $(CROSSBOW_C_FILES:.c=.o)

crossbow: libbow.a argp/libargp.a $(CROSSBOW_O_FILES)
	$(CC) $(CFLAGS) -o $@ $(CROSSBOW_O_FILES) $(LDFLAGS) $(ALL_LIBS)

CROSSBOW_DIST_FILES = \
$(STANDARD_CROSSBOW_H_FILES) \
$(STANDARD_CROSSBOW_C_FILES)


# Archer section

ARCHER_H_FILES = \
bow/archer.h

ARCHER_C_FILES = \
deflexer.c \
pv.c \
wi2pv.c 

ARCHER_O_FILES = $(ARCHER_C_FILES:.c=.o)

archer: libbow.a argp/libargp.a archer.o $(ARCHER_O_FILES)
	$(CC) $(CFLAGS) -o $@ archer.o $(ARCHER_O_FILES) $(LDFLAGS) $(ALL_LIBS)

archer.o: archer.c
	$(CC) -c $(ALL_CPPFLAGS) $(ALL_CFLAGS) -o archer.o archer.c

ARCHER_DIST_FILES = \
archer.c \
$(ARCHER_H_FILES) \
$(ARCHER_C_FILES) 

# Other name ideas: longbow, flint, shoelace, bowtie, ...


# Section for other misc tools

OTHER_C_FILES += \
dice.c \
dicefactory.c \
dirichlet.c \
kl-div.c 

# kl-div doesn't actually depend on libargp, but we need ALL_LIBS so that
# libdb will be used when we compile in HDB
kl-div: libbow.a kl-div.o argp/libargp.a
	$(CC) $(CFLAGS) kl-div.o -o $@ $(LDFLAGS) $(ALL_LIBS)

dice: dice.o
	$(CC) dice.o -o $@

dirichlet: dirichlet.o
	$(CC) -O -g dirichlet.o -o $@ -lm

dicefactory: dicefactory.o
	$(CC) $@.o -o $@ -L. -lbow -L./argp -largp

# A special executable for loading into Lisp (for Kamal)
rainbow-lisp.o: rainbow.c
	$(CC) $(ALL_CPPFLAGS) $(ALL_CFLAGS) -c -DNDEBUG -DRAINBOW_LISP $< -o $@


# Compiling the Makefile

Makefile: Makefile.in config.status
	$(SHELL) config.status
config.status: $(srcdir)/configure
	$(SHELL) $(srcdir)/configure --no-create
$(srcdir)/configure: configure.in
	cd $(srcdir); autoconf

# Installing

installdirs:
	$(srcdir)/mkinstalldirs $(bindir) $(includedir) $(libdir)
INSTALL_FILES = libbow.a bow/libbow.h \
	 $(DEMO_EXECUTABLES) $(PERL_RUNNABLE_FILES)
install: $(INSTALL_FILES) installdirs
	cd argp ; $(MAKE) install
	rm -f $(libdir)/libbow.a
	cp libbow.a $(libdir)
	$(RANLIB) $(libdir)/libbow.a
	rm -f $(includedir)/libbow.h
	cp bow/libbow.h $(includedir)
	cd $(bindir) ; rm -f $(DEMO_EXECUTABLES) $(PERL_RUNNABLE_FILES)
	$(INSTALL) $(DEMO_EXECUTABLES) $(bindir)
	$(INSTALL) $(PERL_RUNNABLE_FILES) $(bindir)

# Cleaning

mostlyclean:
	rm -f core *~
	cd argp ; $(MAKE) mostlyclean
clean: mostlyclean
	rm -f *.o libbow.a $(DEMO_EXECUTABLES) *.info *.dvi
	rm -f $(PERL_RUNNABLE_FILES)
	rm -f $(ARCHER_LEX_FILES:.lex=$(LEX_RULE))
	rm -f $(ARCHER_Y_FILES:.y=$(Y_RULE))
	rm -f $(ARCHER_Y_FILES:.y=$(Y_RULE:.c=.h))
	cd argp ; $(MAKE) clean
maintainer-clean: clean
	rm -f $(PERL_RUNNABLE_FILES) README INSTALL
	rm -f configure config.log config.cache config.status
	cd argp ; $(MAKE) maintainer-clean

# Making a distribution .tar.gz file

DIST_FILES = \
$(LIBBOW_DIST_FILES) \
$(DOC_DIST_FILES) \
$(PERL_DIST_FILES) \
$(RAINBOW_DIST_FILES) \
$(ARROW_DIST_FILES) \
$(CROSSBOW_DIST_FILES) \
$(ARCHER_DIST_FILES) \
$(OTHER_C_FILES) \
archer.el \
ChangeLog \
Makefile.in \
Version \
configure \
configure.in \
install-sh \
mkinstalldirs

bow-$(BOW_VERSION).tar.gz: dist
dist: $(DIST_FILES)
	cvs rtag -F release-`echo $(BOW_VERSION) | tr . -` bow
	echo bow-$(BOW_VERSION) > .fname
	rm -rf `cat .fname`
	mkdir `cat .fname`
	mkdir `cat .fname`/bow
	for file in $(DIST_FILES); do \
	  ln $$file `cat .fname`/$$file ; \
	done
	mkdir `cat .fname`/argp
	cd argp ; SNAP=../`cat ../.fname`/argp $(MAKE) snap
	tar -chvf `cat .fname`.tar `cat .fname`
	rm -f `cat .fname`.tar.gz
	gzip -9 `cat .fname`.tar
	rm -rf `cat .fname` .fname

diff: $(DIST_FILES)
	@if [ ! $(OLD) ] ; then \
	  echo You must set OLD to the version number against which to diff ; \
	  exit -1 ; \
	fi
	@if [ ! $(NEW) ] ; then \
	  echo You must set NEW to the version number with which to diff ; \
	  exit -1 ; \
	fi
	gunzip -c bow-$(NEW).tar.gz | (cd /tmp ; tar -xf -)
	gunzip -c bow-$(OLD).tar.gz | (cd /tmp ; tar -xf -)
	rm -f bow-$(OLD)-$(NEW).diff
	-diff -u -r /tmp/bow-$(OLD) /tmp/bow-$(NEW) > bow-$(OLD)-$(NEW).diff
	rm -rf /tmp/bow-$(NEW)
	rm -rf /tmp/bow-$(OLD)

snapshot: $(DIST_FILES)
	echo bow-`date +%Y%m%d` > .fname
	cvs rtag -F snapshot-`cat .fname` bow
	rm -rf `cat .fname`
	mkdir `cat .fname`
	mkdir `cat .fname`/bow
	for file in $(DIST_FILES); do \
	  ln $$file `cat .fname`/$$file ; \
	done
	mkdir `cat .fname`/argp
	cd argp ; SNAP=../`cat ../.fname`/argp $(MAKE) snap
	tar -chvf `cat .fname`.tar `cat .fname`
	rm -f `cat .fname`.tar.gz
	gzip -9 `cat .fname`.tar
	rm -rf `cat .fname` .fname

dist-cmu: bow-$(BOW_VERSION).tar.gz
	cp -f $< /afs/cs/project/theo-11/www/naive-bayes

