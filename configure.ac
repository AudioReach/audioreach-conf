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

AC_ARG_WITH([qcom],
    AS_HELP_STRING([Use qcom based configuration (default is no)]),
        [with_qcom=$withval],
        [with_qcom=no])
AM_CONDITIONAL([VENDOR_QCOM], [test "x${with_qcom}" = "xyes"])

AC_CONFIG_FILES([Makefile])

AM_COND_IF([VENDOR_QCOM],
        [AC_CONFIG_FILES([qcom/Makefile qcom/kvh2xml.pc \
                          qcom/qli/qcm6490/Makefile qcom/qli/qcm6490/config.pc \
                          qcom/qli/qcs8300/Makefile qcom/qli/qcs8300/config.pc \
                          qcom/qli/qcs9100/Makefile qcom/qli/qcs9100/config.pc \
                          qcom/qli/qcs9075/Makefile qcom/qli/qcs9075/config.pc \
			  ])])

AC_CONFIG_FILES([ \
        linux/Makefile \
        linux/kvh2xml.pc \
        linux/reference/Makefile \
        linux/reference/config.pc
        ])

AC_OUTPUT
