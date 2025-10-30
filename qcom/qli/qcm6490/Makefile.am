pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = config.pc
EXTRA_DIST = $(pkgconfig_DATA)

AM_CFLAGS = -Wall -Werror

config_acdbdata = acdbdata/acdb_cal.acdb\
		 acdbdata/workspaceFileXml.qwsp

config_acdbdatadir = $(sysconfdir)/acdbdata/QCS6490_RB3Gen2/
config_acdbdata_DATA = $(config_acdbdata)

config_carddef = card-defs.xml

config_carddefdir = $(sysconfdir)
config_carddef_DATA = $(config_carddef)
