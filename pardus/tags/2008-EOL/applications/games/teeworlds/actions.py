#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "teeworlds-%s-src" % get.srcVERSION()
datadir = "/usr/share/teeworlds"
NoStrip = [datadir]

def setup():
    shelltools.export("CC", get.CC())
    shelltools.export("CFLAGS", get.CFLAGS())

    shelltools.cd("bam-0.2.0")
    shelltools.system("./make_unix.sh")

def build():
    shelltools.system("./bam-0.2.0/src/bam release")

def install():
    pisitools.dobin("teeworlds")
    pisitools.dobin("teeworlds_srv")
    pisitools.rename("/usr/bin/teeworlds_srv", "teeworlds-server")

    pisitools.insinto(datadir, "data/*")

    pisitools.dodoc("*.txt")