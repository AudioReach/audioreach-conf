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
AC_CONFIG_MACRO_DIR([m4])

# Checks for programs.
AC_PROG_CC
AM_PROG_CC_C_O
AC_PROG_CXX
LT_INIT
AC_PROG_LIBTOOL
AC_PROG_AWK
AC_PROG_CPP
AC_PROG_INSTALL
AC_PROG_LN_S
AC_PROG_MAKE_SET
AM_PROG_AR
PKG_PROG_PKG_CONFIG

AC_ARG_WITH([mbb],
    AS_HELP_STRING([use mbb (default is no)]),
    [with_mbb=$withval],
    [with_mbb=no])
AM_CONDITIONAL([MBB_PL], [test "x${with_mbb}" = "xyes"])

AC_CONFIG_FILES([Makefile kvh2xml.pc])
if (test "x${with_mbb}" = "xno"); then
AC_CONFIG_SUBDIRS([qli])
else
AC_CONFIG_SUBDIRS([mbb])
fi

AC_OUTPUT
