AM_CFLAGS = -Wall -Werror

config_acdbdata = acdbdata/acdb_cal.acdb\
		 acdbdata/workspaceFileXml.qwsp

config_acdbdatadir = $(sysconfdir)/acdbdata/
config_acdbdata_DATA = $(config_acdbdata)

config_carddef = card-defs.xml

config_carddefdir = $(sysconfdir)
config_carddef_DATA = $(config_carddef)

if HAVE_LIBALSA
config_alsa_confdir = $(sysconfdir)/alsa/conf.d
config_alsa_conf_DATA = alsalib/agm.conf

config_ucmdir = $(datadir)/alsa/ucm2/conf.virt.d
config_ucm_DATA = alsalib/agmvirtualsndcard.conf \
		  alsalib/PCMPlayback.conf
endif
