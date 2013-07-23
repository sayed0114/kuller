#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "hsqldb"

def install():
    pisitools.insinto("/usr/share/java", "lib/hsqldb.jar")

    pisitools.dohtml("doc/*.html", "doc/guide/*", "doc/src/*")
    pisitools.dodoc("readme.txt", "doc/*.txt")