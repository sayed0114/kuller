#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

#WorkDir = ""

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static --disable-scrollkeeper --disable-schemas-install")

def build():
    autotools.make()

def install():
    shelltools.export("HOME", get.workDIR())
    autotools.install()
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")