# configure.ac -- Autoconf script for audioreach-conf
#

# Process this file with autoconf to produce a configure script

# Requires autoconf tool later than 2.61
AC_PREREQ(2.69)
# Initialize the acdbdata package version 1.0.0
AC_INIT([audioreach-conf],1.0.0)
# Does not strictly follow GNU Coding standards
AM_INIT_AUTOMAKE([-Wall -Werror foreign subdir-objects])
# defines some macros variable to be included by source
AC_CONFIG_HEADERS([config.h])

# Checks for programs.
AC_PROG_CC
AM_PROG_CC_C_O
AC_PROG_CXX
LT_INIT
AC_PROG_AWK
AC_PROG_CPP
AC_PROG_INSTALL
AC_PROG_LN_S
AC_PROG_MAKE_SET
AM_PROG_AR
PKG_PROG_PKG_CONFIG

AC_CONFIG_FILES([Makefile kvh2xml.pc])
AC_CONFIG_SUBDIRS([qli])

AC_OUTPUT
