## -*- coding: utf-8 -*-
#
# «skeletor» - An Example Plugin for showing how to use MCC as a developer
#
# Copyright (C) 2009, Mario Limonciello, for Mythbuntu
#
#
# Mythbuntu is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this application; if not, write to the Free Software Foundation, Inc., 51
# Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
##################################################################################

from MythbuntuControlCentre.plugin import MCCPlugin
from gi.repository import Gtk
import time

class SkeletonPlugin(MCCPlugin):
    """An Example Plugin for showing how to use MCC as a developer"""
    #
    #Load GUI & Calculate Changes
    #

    def __init__(self):
        #Initialize parent class
        information = {}
        information["name"] = "Skeletor"
        information["icon"] = "gtk-stop"
        information["ui"] = "tab_skeletor"
        MCCPlugin.__init__(self,information)

    def captureState(self):
        """Determines the state of the items on managed by this plugin
           and stores it into the plugin's own internal structures"""
        import os
        self.changes = {}
        self.changes['user_file'] = os.path.exists('/tmp/user_file')
        self.changes['root_file'] = os.path.exists('/tmp/root_file')
        self.changes['tuxeyes'] = self.query_installed('tuxeyes')

    def applyStateToGUI(self):
        """Takes the current state information and sets the GUI
           for this plugin"""
        self.user_touch_checkbox.set_active(self.changes['user_file'])
        self.root_touch_checkbox.set_active(self.changes['root_file'])
        self.tuxeyes_checkbox.set_active(self.changes['tuxeyes'])

    def compareState(self):
        """Determines what items have been modified on this plugin"""
        MCCPlugin.clearParentState(self)
        if self.user_touch_checkbox.get_active() != self.changes['user_file']:
            self._markReconfigureUser('user_file',self.user_touch_checkbox.get_active())
        if self.root_touch_checkbox.get_active() != self.changes['root_file']:
            self._markReconfigureRoot('root_file',self.root_touch_checkbox.get_active())
        if self.tuxeyes_checkbox.get_active() != self.changes['tuxeyes']:
            if self.tuxeyes_checkbox.get_active():
                self._markInstall('tuxeyes')
            else:
                self._markRemove('tuxeyes')
    #
    # Callbacks
    #
    def callback_example(self,widget,data=None):
        """Shows an example of how a callback can do stuff"""
        widget_was_visible = self.callback_image.flags() & Gtk.VISIBLE
        if widget_was_visible:
            self.callback_image.hide()
        else:
            self.callback_image.show()

    #
    # Process selected activities
    #

    def root_scripted_changes(self,reconfigure):
        """System-wide changes that need root access to be applied.
           This function is ran by the dbus backend"""
        self.emit_progress("Setting to 20 percent as a root", 20)
        time.sleep(2)
        for item in reconfigure:
            if item == "root_file":
                if reconfigure[item]:
                    file = open("/tmp/root_file", "a")
                else:
                    import os
                    os.remove("/tmp/root_file")
        self.emit_progress("Setting to 90 percent as a root", 90)
        time.sleep(2)

    def user_scripted_changes(self,reconfigure):
        """Local changes that can be performed by the user account.
           This function will be ran by the frontend"""
        self.emit_progress("Setting to 20 percent as a user", 20)
        time.sleep(2)
        for item in reconfigure:
            if item == "user_file":
                if reconfigure[item]:
                    file = open("/tmp/user_file", "a")
                else:
                    import os
                    os.remove("/tmp/user_file")
        self.emit_progress("Setting to 90 percent as a user", 90)
        time.sleep(2)
