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

# Go to data supermode
netedit.supermodeData()

# change to TAZRelData
netedit.TAZRelData()

# create dataSet
netedit.createDataSet()

# create data interval
netedit.createDataInterval()

# create TAZRelData
netedit.leftClick(referencePosition, 300, 180)
netedit.leftClick(referencePosition, 700, 180)
netedit.typeEnter()

# go to inspect mode
netedit.inspectMode()

# inspect TAZRelData
netedit.leftClick(referencePosition, 425, 254)

# Change parameter 3 with a non valid value (empty speed)
netedit.modifyAttribute(netedit.attrs.TAZRelData.inspect.fromTAZ, "", False)

# Change parameter 3 with a non valid value (empty speed)
netedit.modifyAttribute(netedit.attrs.TAZRelData.inspect.fromTAZ, "dummyTAZ", False)

# Change parameter 3 with a non valid value (empty speed)
netedit.modifyAttribute(netedit.attrs.TAZRelData.inspect.fromTAZ, "taz_1", False)

# Change parameter 3 with a non valid value (empty speed)
netedit.modifyAttribute(netedit.attrs.TAZRelData.inspect.fromTAZ, "taz_2", False)

# Check undo
netedit.checkUndoRedo(referencePosition)

# save Netedit config
netedit.saveNeteditConfig(referencePosition)

# quit netedit
netedit.quit(neteditProcess)
