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

# go to select mode
netedit.selectMode()

# select all using invert
netedit.selectionInvert()

# go to inspect mode
netedit.inspectMode()

# inspect container
netedit.leftClick(referencePosition, netedit.positions.demandElements.container.x,
                  netedit.positions.demandElements.container.y)

# change flow value
netedit.modifyAttribute(netedit.attrs.containerFlow.inspectSelection.spacing, "dummyTerminate", False)

# change flow value
netedit.modifyAttribute(netedit.attrs.containerFlow.inspectSelection.spacing, "probability", False)

# change flow value
netedit.modifyAttribute(netedit.attrs.containerFlow.inspectSelection.spacingOption, "dummy", False)

# change flow value
netedit.modifyAttribute(netedit.attrs.containerFlow.inspectSelection.spacingOption, "12.5", False)

# change flow value
netedit.modifyAttribute(netedit.attrs.containerFlow.inspectSelection.spacingOption, "26", False)

# change flow value
netedit.modifyAttribute(netedit.attrs.containerFlow.inspectSelection.spacingOption, "0.3", False)

# Check undo
netedit.checkUndoRedo(referencePosition)

# save Netedit config
netedit.saveNeteditConfig(referencePosition)

# save containers
# quit netedit
netedit.quit(neteditProcess)
