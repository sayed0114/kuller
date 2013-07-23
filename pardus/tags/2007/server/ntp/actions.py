#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "ntp-4.2.2p4"

def setup():
    autotools.configure("--bindir=/usr/sbin \
                         --sysconfdir=/etc/ntp \
                         --enable-all-clocks \
                         --enable-parse-clocks \
                         --enable-linuxcaps \
                         --enable-ipv6")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.domove("/usr/bin/sntp", "/usr/sbin")
    pisitools.domove("/usr/bin/ntpdc", "/usr/sbin")
    pisitools.domove("/usr/bin/ntpd", "/usr/sbin")
    pisitools.dodoc("ChangeLog", "NEWS", "README", "TODO", "WHERE-TO-START")
    pisitools.dohtml("html/*")
    pisitools.dodir("/var/lib/ntp")
    pisitools.dodir("/var/lib/ntp/drift")