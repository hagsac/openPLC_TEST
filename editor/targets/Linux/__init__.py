#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Beremiz, a Integrated Development Environment for
# programming IEC 61131-3 automates supporting plcopen standard and CanFestival.
#
# Copyright (C) 2007: Edouard TISSERANT and Laurent BESSARD
#
# See COPYING file for copyrights details.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
from targets.toolchain_gcc import toolchain_gcc
import platform


class Linux_target(toolchain_gcc):
    dlopen_prefix = "./"
    extension = ".so"

    def getBuilderCFLAGS(self):
        return toolchain_gcc.getBuilderCFLAGS(self) + ["-fPIC"]

    def getBuilderLDFLAGS(self):
        if platform.system() == 'Darwin':
            return toolchain_gcc.getBuilderLDFLAGS(self) + ["-shared"]
        else:
            return toolchain_gcc.getBuilderLDFLAGS(self) + ["-shared", "-lrt"]
