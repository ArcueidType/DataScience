# Generated automatically from Makefile.in by configure.
#   Generated automatically from Makefile.in by configure.
#
#   Makefile for the command-line-argument-processing library, libargp
#   Written by:  Miles Bader <miles@gnu.ai.mit.edu>

SHELL = /bin/sh

#### Start of system configuration section. ####

default: libargp.a

srcdir = .
RANLIB = ranlib
INSTALL = /usr/bin/install -c
INSTALL_PROGRAM = ${INSTALL}
INSTALL_DATA = ${INSTALL} -m 644

CC = gcc

DEFS =  -DHAVE_GETOPT_H=1 -DHAVE_GETOPT_LONG=1 -DHAVE_STRERROR=1 -DHAVE_STRNDUP=1 -DHAVE_MEMMOVE=1 -DHAVE_VSNPRINTF=1 -DHAVE_STRERROR=1 -DHAVE_STRINGS_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 
LIBS = 
     
# All these are optional.  You can redifine CFLAGS, CPPFLAGS,
# INCLUDEFLAGS and LDFLAGS on the command line however you like.
CFLAGS = -g -O -Wall
CPPFLAGS = 
INCLUDEFLAGS =
LDFLAGS =

prefix = /usr/local
exec_prefix = ${prefix}

# Installation locations
bindir = $(exec_prefix)/bin
libdir = $(exec_prefix)/lib
includedir = $(prefix)/include
infodir = $(prefix)/info

#### End of system configuration section. ####

ARGP_VERSION = 0.1

ARGP_H_FILES = \
argp.h

ARGP_C_FILES = \
argp-ba.c \
argp-fmtstream.c \
argp-fs-xinl.c \
argp-help.c \
argp-parse.c \
argp-pv.c \
argp-pvh.c \
argp-xinl.c \
argp.c \
pin.c \
strndup.c

ARGP_O_FILES = $(ARGP_C_FILES:.c=.o)

ARGP_GETOPT_C_FILES = \
getopt.c \
getopt1.c

ARGP_GETOPT_O_FILES = $(ARGP_GETOPT_C_FILES:.c=.o)

ARGP_CHECK_C_FILES = \
argp-ex1.c \
argp-ex2.c \
argp-ex3.c \
argp-ex4.c \
argp-test.c \
tester.c

ARGP_CHECK_O_FILES = $(ARGP_CHECK_C_FILES:.c=.o)
ARGP_CHECK_PROGRAMS = $(ARGP_CHECK_C_FILES:.c=)

DIST_FILES = \
$(ARGP_C_FILES) \
$(ARGP_H_FILES) \
$(ARGP_GETOPT_C_FILES) \
$(ARGP_CHECK_C_FILES) \
ChangeLog \
INSTALL \
Makefile.in \
README \
configure \
configure.in \
install-sh \
mkinstalldirs \
getopt.h \
argp1.h \
argp-fmtstream.h \
argp-namefrob.h

# Rules

# Pattern rule
ALL_CPPFLAGS = $(CPPFLAGS) -I$(srcdir) $(INCLUDEFLAGS) $(DEFS)
ALL_CFLAGS = $(CFLAGS)
.c.o:
	$(CC) -c $(ALL_CPPFLAGS) $(ALL_CFLAGS) -o $@ $<

all: libargp.a

# Compiling code

libargp.a: $(ARGP_O_FILES) 
	$(AR) rc $@ $^
	$(RANLIB) $@

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
INSTALL_FILES = libargp.a argp.h
install: $(INSTALL_FILES) installdirs
	rm -f $(libdir)/libargp.a
	cp libargp.a $(libdir)
	$(RANLIB) $(libdir)/libargp.a
	rm -f $(includedir)/argp.h
	cp argp.h $(includedir)

# Compiling examples and test programs
$(ARGP_CHECK_PROGRAMS): libargp.a
	$(CC) -I. $@.c -L. -largp -o $@

checks: $(ARGP_CHECK_PROGRAMS)

# Cleaning

mostlyclean:
	rm -f core *~
clean: mostlyclean
	rm -f *.o libargp.a *.info *.dvi tester
maintainer-clean: clean
	rm -f configure config.log config.cache config.status

# Making a distribution .tar.gz file

# Copy all the dist files into the directory named by $(SNAP)
snap: $(DIST_FILES)
	for file in $(DIST_FILES); do \
	  ln $$file $(SNAP)/$$file ; \
	done

dist: $(DIST_FILES)
	cvs rtag -F release-`tr . - $(ARGP_VERSION)` argp
	echo argp-$(ARGP_VERSION) > .fname
	rm -rf `cat .fname`
	mkdir `cat .fname`
	for file in $(DIST_FILES); do \
	  ln $$file `cat .fname`/$$file ; \
	done
	tar -chvf `cat .fname`.tar `cat .fname`
	rm -f `cat .fname`.tar.gz
	gzip -9 `cat .fname`.tar
	rm -rf `cat .fname` .fname

snapshot: $(DIST_FILES)
	echo argp-`date +%y%m%d` > .fname
	cvs rtag -F snapshot-`cat .fname` argp
	rm -rf `cat .fname`
	mkdir `cat .fname`
	for file in $(DIST_FILES); do \
	  ln $$file $(SNAP)/$$file ; \
	done
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
	gunzip -c argp-$(NEW).tar.gz | (cd /tmp ; tar -xf -)
	gunzip -c argp-$(OLD).tar.gz | (cd /tmp ; tar -xf -)
	rm -f argp-$(OLD)-$(NEW).diff
	-diff -u -r /tmp/argp-$(OLD) /tmp/argp-$(NEW) > argp-$(OLD)-$(NEW).diff
	rm -rf /tmp/argp-$(NEW)
	rm -rf /tmp/argp-$(OLD)

