# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("LDFLAGS", "")
    autotools.configure("--libdir=/usr/lib \
                         --disable-static")

def build():
    autotools.make("-j1 LDFLAGS='%s'" % get.LDFLAGS())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())