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
# @date    2019-07-16

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

# go to demand mode
netedit.supermodeDemand()

# go to route mode
netedit.routeMode()

# set invalid repeat
netedit.changeDefaultValue(netedit.attrs.route.create.repeat, "dummyrepeat")

# try to create route using three edges
netedit.leftClick(referencePosition, netedit.positions.demandElements.edge0.x, netedit.positions.demandElements.edge0.y)
netedit.leftClick(referencePosition, netedit.positions.demandElements.edge1.x, netedit.positions.demandElements.edge1.y)
netedit.leftClick(referencePosition, netedit.positions.demandElements.edge2.x, netedit.positions.demandElements.edge2.y)
netedit.leftClick(referencePosition, netedit.positions.demandElements.edgeRepeat0.x,
                  netedit.positions.demandElements.edgeRepeat0.y)

# press enter to try to create route
netedit.typeEnter()

# set valid repeat
netedit.changeDefaultValue(netedit.attrs.route.create.repeat, "15.6")

# press enter to create route
netedit.typeEnter()

# set valid repeat
netedit.changeDefaultValue(netedit.attrs.route.create.repeat, "13")

# press enter to create route
netedit.typeEnter()

# Check undo redo
netedit.checkUndoRedo(referencePosition)

# save Netedit config
netedit.saveNeteditConfig(referencePosition)

# quit netedit
netedit.quit(neteditProcess)
