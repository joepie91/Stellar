#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2012, 2014 Emilio Coppola
#
# This file is part of Stellar.
#
# Stellar is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Stellar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Stellar.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals


from PyQt4 import QtCore, QtGui
import os, sys

if sys.version_info.major == 2:
    str = unicode


class ConstantsPanel(QtGui.QDialog):
    def __init__(self, main, parent):
        super(ConstantsPanel, self).__init__(parent)
        self.main = main
        self.fname = self.main.fname

        self.InitUI()

    def InitUI(self):
        pass
              
