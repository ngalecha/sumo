#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.dev/sumo
# Copyright (C) 2009-2024 German Aerospace Center (DLR) and others.
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# https://www.eclipse.org/legal/epl-2.0/
# This Source Code may also be made available under the following Secondary
# Licenses when the conditions for such availability set forth in the Eclipse
# Public License 2.0 are satisfied: GNU General Public License, version 2
# or later which is available at
# https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html
# SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2016-11-25

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, referencePosition = netedit.setupAndStart(neteditTestRoot)

# go to additional mode
netedit.additionalMode()

# select parkingArea
netedit.changeElement("parkingArea")

# create parkingArea in mode "Reference Left"
netedit.leftClick(referencePosition, 475, 256)

# select space
netedit.changeElement("space")

# set invalid width (dummy)
netedit.selectAdditionalChild(netedit.attrs.parkingSpace.create.parent, 0)
netedit.changeDefaultValue(netedit.attrs.parkingSpace.create.width, "dummyWidth")

# try to create area
netedit.leftClick(referencePosition, 292, 371)

# set invalid width (empty)
netedit.changeDefaultValue(netedit.attrs.parkingSpace.create.width, "")

# try to create area
netedit.leftClick(referencePosition, 336, 371)

# set invalid width (negative)
netedit.changeDefaultValue(netedit.attrs.parkingSpace.create.width, "-3")

# try to create area
netedit.leftClick(referencePosition, 383, 371)

# set valid width
netedit.changeDefaultValue(netedit.attrs.parkingSpace.create.width, "2.5")

# create area
netedit.leftClick(referencePosition, 429, 371)

# Check undo redo
netedit.checkUndoRedo(referencePosition)

# save netedit config
netedit.saveNeteditConfig(referencePosition)

# quit netedit
netedit.quit(neteditProcess)
