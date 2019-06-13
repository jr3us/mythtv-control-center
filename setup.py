#!/usr/bin/python3
# Mythbuntu-Control-Centre install script
# Copyright (C) 2007-2009, Mario Limonciello <superm1@mythbuntu.org>
#
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

from distutils.core import setup

import subprocess, glob, os.path
from DistUtilsExtra.command import *

setup(
    name="mythbuntu-control-centre",
    author="Mario Limonciello",
    author_email="superm1@mythbuntu.org",
    maintainer="Ubuntu MythTV Team",
    maintainer_email="ubuntu-mythtv@lists.ubuntu.com",
    url="http://www.mythbuntu.org",
    license="gpl",
    description="configures mythbuntu system settings",
    packages=["MythbuntuControlCentre"],
    data_files=[("/etc/dbus-1/system.d/", glob.glob("backend/*.conf")),
                ('share/dbus-1/system-services', glob.glob('backend/*.service')),
                ('share/mythbuntu', ['backend/mcc-backend']),
                ("share/mythbuntu/ui", glob.glob("data/*.ui")),
                ("share/pixmaps", glob.glob("data/*.png")),
                ("share/mythbuntu/examples/plugins/python", glob.glob("examples/plugins/python/*")),
                ("share/mythbuntu/examples/plugins/ui", glob.glob("examples/plugins/ui/*")),
                ("share/applications", glob.glob("applications/*.desktop"))],
    scripts=["mythbuntu-control-centre"],
    cmdclass = { 'build': build_extra.build_extra,
             'build_i18n': build_i18n.build_i18n,
             'build_icons': build_icons.build_icons,
             'clean': clean_i18n.clean_i18n,
           }

)

