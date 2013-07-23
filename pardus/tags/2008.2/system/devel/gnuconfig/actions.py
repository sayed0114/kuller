#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def check():
    autotools.make("check")

def install():
    pisitools.doexe("config.*", "/usr/share/gnuconfig")

    pisitools.dodoc("ChangeLog")