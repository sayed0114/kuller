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
    # autotools.autoreconf("-vfi")
    autotools.configure("--disable-static --disable-bugbuddy")

def build():
    # autotools.make("LIBS=-lm")
    autotools.make()

def install():
    autotools.install()
