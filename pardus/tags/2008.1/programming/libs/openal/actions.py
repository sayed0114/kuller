#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoconf()
    autotools.configure("--disable-static \
                         --disable-esd \
                         --enable-sdl \
                         --enable-alsa \
                         --enable-arts \
                         --enable-mp3 \
                         --enable-vorbis")

def build():
    autotools.make("-j1 all")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS","NOTES", "README", "TODO")