#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

WorkDir = "PythonCAD-DS1-R37"

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.insinto("/usr/bin", "gtkpycad.py", "pythoncad")
    pisitools.insinto("/etc/pythoncad", "prefs.py")
    pisitools.insinto("/usr/share/applications", "pythoncad.desktop")
    pisitools.insinto("/usr/share/pixmaps", "gtkpycad.png", "pythoncad.png")
