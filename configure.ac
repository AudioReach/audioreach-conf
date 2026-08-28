#                                               -*- Autoconf -*-
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

AC_ARG_WITH([qcom],
    AS_HELP_STRING([Use qcom based configuration (default is no)]),
        [with_qcom=$withval],
        [with_qcom=no])
AM_CONDITIONAL([VENDOR_QCOM], [test "x${with_qcom}" = "xyes"])

AC_ARG_WITH([libalsa],
    AS_HELP_STRING([--with-libalsa], [Install ALSA and UCM configuration files (default is no)]),
        [with_libalsa=$withval],
        [with_libalsa=no])
AM_CONDITIONAL([HAVE_LIBALSA], [test "x${with_libalsa}" = "xyes"])

AC_ARG_WITH([nxp],
    AS_HELP_STRING([Use nxp based configuration (default is no)]),
        [with_nxp=$withval],
        [with_nxp=no])
AM_CONDITIONAL([VENDOR_NXP], [test "x${with_nxp}" = "xyes"])

AC_CONFIG_FILES([ \
        Makefile \
        linux/Makefile \
        linux/kvh2xml.pc \
        linux/reference/Makefile \
        linux/reference/config.pc \
        nxp/Makefile \
        nxp/kvh2xml.pc \
        nxp/reference/Makefile \
        nxp/reference/config.pc
        ])


# Declare recursive configure into subpackages
AM_COND_IF([VENDOR_QCOM], [AC_CONFIG_SUBDIRS([qcom])])

AC_OUTPUT
