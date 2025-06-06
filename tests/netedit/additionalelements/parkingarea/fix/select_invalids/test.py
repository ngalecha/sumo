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

# go to select mode
netedit.selectMode()

# select all using invert
netedit.selectionInvert()

# go to inspect mode
netedit.inspectMode()

# inspect parking areas
netedit.leftClick(referencePosition, 566, 285)

# disable friendlyPos
netedit.modifyBoolAttribute(netedit.attrs.parkingArea.inspectSelection.friendlyPos, True)

# go to select mode
netedit.selectMode()

# clear selection
netedit.selectionClear()

# save netedit config
netedit.saveNeteditConfig(referencePosition)

# select invalids
netedit.fixStoppingPlace("selectInvalids")

# remove it using DEL key
netedit.deleteUsingSuprKey()

# save netedit config
netedit.saveNeteditConfig(referencePosition)

# quit netedit
netedit.quit(neteditProcess)
