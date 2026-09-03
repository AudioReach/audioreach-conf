# audioreach-paths.m4 -- shared installation paths for AudioReach
# serial 1
#
# SPDX-License-Identifier: BSD-3-Clause
#
# Usage, in configure.ac:
#
#     AC_CONFIG_MACRO_DIRS([m4])
#     AR_PATHS
#
# Provides three directories, as configure options and as make variables:
#
#     audioreachconfdir    integrator-editable configuration
#     audioreachdatadir    read-only vendor data
#     audioreachdeltadir   runtime-writable ACDB deltas
#
# Do not AC_DEFINE these. ${sysconfdir} is unexpanded at configure time, so
# AC_DEFINE would put a literal "${prefix}" into config.h. Pass them to the
# compiler from Makefile.am instead, where make expands them:
#
#     AM_CFLAGS += -DCARD_DEF_FILE=\"$(audioreachconfdir)/card-defs.xml\"

AC_DEFUN([AR_PATHS], [

  AC_ARG_WITH([audioreach-confdir],
    [AS_HELP_STRING([--with-audioreach-confdir=DIR],
      [AudioReach configuration directory @<:@SYSCONFDIR/audioreach@:>@])],
    [audioreachconfdir="$withval"],
    [audioreachconfdir='${sysconfdir}/audioreach'])

  AC_ARG_WITH([audioreach-datadir],
    [AS_HELP_STRING([--with-audioreach-datadir=DIR],
      [AudioReach read-only data directory @<:@DATADIR/audioreach@:>@])],
    [audioreachdatadir="$withval"],
    [audioreachdatadir='${datadir}/audioreach'])

  AC_ARG_WITH([audioreach-deltadir],
    [AS_HELP_STRING([--with-audioreach-deltadir=DIR],
      [AudioReach ACDB delta directory @<:@LOCALSTATEDIR/lib/audioreach/acdb-delta@:>@])],
    [audioreachdeltadir="$withval"],
    [audioreachdeltadir='${localstatedir}/lib/audioreach/acdb-delta'])

  AC_SUBST([audioreachconfdir])
  AC_SUBST([audioreachdatadir])
  AC_SUBST([audioreachdeltadir])
])
