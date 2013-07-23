#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "skanlite-0.3-kde4.2.3"
shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure(installPrefix="/usr/kde/4", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    for d in ["de", "pt", "sv", "uk"]:
        pisitools.remove("/usr/kde/4/share/doc/HTML/%s/%s/common" % (d, get.srcNAME()))
        pisitools.dosym("/usr/kde/4/share/doc/HTML/en/common", "/usr/kde/4/share/doc/HTML/%s/%s/common" % (d, get.srcNAME()))