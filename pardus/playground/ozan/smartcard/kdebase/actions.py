#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#

from pisi.actionsapi import kde
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

KeepSpecial=["libtool"]
shelltools.export("HOME", get.workDIR())

def setup():
    # the java test is problematic (see kde bug 100729) and
    # useless. All that's needed for java applets to work is
    # to have the 'java' executable in PATH.
    kde.configure("--with-dpms \
                   --enable-dnssd \
                   --with-libaudit=yes \
                   --with-hal \
                   --with-ldap \
                   --with-cups \
                   --with-gl \
                   --with-ssl \
                   --with-samba \
                   --with-libusb \
                   --with-openexr \
                   --with-libraw1394 \
                   --with-hal \
                   --with-pam=yes \
                   --with-sudo-kdesu-backend \
                   --with-krb5auth \
                   --without-sensors \
                   --without-java")

def build():
    kde.make()

def install():
    kde.install()

    # kdm wants extra interest
    shelltools.cd("kdm")
    kde.install("GENKDMCONF_FLAGS=\"--no-old --no-backup --no-in-notice\" install")

    pisitools.remove("%s/share/templates/.source/emptydir" % get.kdeDIR())

    # remove kcontrol (we have TASMA), but not kinfocenter
    pisitools.remove("/usr/kde/3.5/bin/kinfocenter")
    pisitools.domove("/usr/kde/3.5/bin/kcontrol", "/usr/kde/3.5/bin/", "kinfocenter")
    pisitools.remove("/usr/kde/3.5/share/applications/kde/KControl.desktop")
    pisitools.remove("/usr/kde/3.5/share/applications/kde/Help.desktop")

    # Put kdmrc into /etc/X11/kdm, so it can be modified on live CDs
    pisitools.domove("/usr/kde/3.5/share/config/kdm/kdmrc", "/etc/X11/kdm/")
    pisitools.dosym("/etc/X11/kdm/kdmrc", "/usr/kde/3.5/share/config/kdm/kdmrc")

    # Use common Xsession script
    pisitools.remove("/usr/kde/3.5/share/config/kdm/Xsession")
    pisitools.dosym("/usr/lib/X11/xinit/Xsession", "/usr/kde/3.5/share/config/kdm/Xsession")