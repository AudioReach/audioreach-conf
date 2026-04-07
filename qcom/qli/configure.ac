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
AC_PROG_LIBTOOL
AC_PROG_AWK
AC_PROG_CPP
AC_PROG_INSTALL
AC_PROG_LN_S
AC_PROG_MAKE_SET
AM_PROG_AR
PKG_PROG_PKG_CONFIG

AC_CONFIG_FILES([ \
    qcm6490/Makefile qcm6490/config.pc \
    qcs615/Makefile  qcs615/config.pc  \
    qcs8275/Makefile qcs8275/config.pc \
    qcs8300/Makefile qcs8300/config.pc \
    qcs9100/Makefile qcs9100/config.pc \
    qcs9075/Makefile qcs9075/config.pc \
    sm8750/Makefile  sm8750/config.pc \
    shikra/Makefile  shikra/config.pc
    ])

AC_OUTPUT
