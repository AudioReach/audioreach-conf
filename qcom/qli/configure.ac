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

m4_define([LT_MAJOR], [1])
m4_define([LT_MINOR], [0])
m4_define([LT_PATCH], [0])

AC_SUBST([LT_VERSION], LT_MAJOR.LT_MINOR.LT_PATCH)
AC_SUBST([LT_VERSION_NUMBER], LT_MAJOR:LT_MINOR:LT_PATCH)

AC_CONFIG_FILES([ \
    qcm6490/Makefile qcm6490/config.pc \
    qcs615/Makefile  qcs615/config.pc  \
    qcs8275/Makefile qcs8275/config.pc \
    qcs8300/Makefile qcs8300/config.pc \
    qcs9100/Makefile qcs9100/config.pc \
    qcs9075/Makefile qcs9075/config.pc \
    sm8750/Makefile  sm8750/config.pc \
    GLYMUR/Makefile  GLYMUR/config.pc \
    MAHUA/Makefile   MAHUA/config.pc \
    Kaanapali/Makefile Kaanapali/config.pc \
    X1E80100/Makefile X1E80100/config.pc \
    shikra_cqs/Makefile shikra_cqs/config.pc \
    shikra_iqs/Makefile shikra_iqs/config.pc
    ])

AC_OUTPUT
