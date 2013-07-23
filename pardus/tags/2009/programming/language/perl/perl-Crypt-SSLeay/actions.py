#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007,2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-0.57_01" % (get.srcNAME()[5:])

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()
    perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.dodoc("README")