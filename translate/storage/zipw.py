#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2007 Zuza Software Foundation
#
# This file is part of translate.
#
# translate is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# translate is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

"""This module provides functionality to work with zip files."""

# Perhaps all methods should work with a wildcard to limit searches in some
# way (examples: *.po, base.xlf, pootle-terminology.tbx)

#TODO: consider also providing directories as we currently provide files

import os
import zipfile

from translate.storage import factory
from translate.storage import directory
from translate.misc import wStringIO


class ZIPFile(directory.Directory):
    """This class represents a ZIP file like a directory."""

    def __init__(self, filename=None):
        self.filename = filename
        self.filedata = []
        self.storedata = []
        self.scanfiles()
        self.scanstores()

    def unit_iter(self):
        """Iterator over all the units in all the files in this zip file."""
        for dirname, filename in self.file_iter():
            # TODO: Here os.path.join(dirname, filename) doesn't work.....
            if dirname=='':
                filepath=os.path.join(dirname, filename)
            else:
                filepath=dirname+'/'+filename
            strfile = wStringIO.StringIO(self.archive.read(filepath))
            strfile.filename = filename
            store = factory.getobject(strfile)
            self.storedata.append(store)
            #TODO: don't regenerate all the storage objects
            for unit in store.unit_iter():
                yield unit
                
    def savefiles(self):
        """Try to save all files in this directory."""
        # TODO: need to make more robust
        super(ZIPFile, self).savefiles()
        newzipfile=zipfile.ZipFile(self.filename+"~temp",'w',zipfile.ZIP_DEFLATED)
        for dirname, filename in self.file_iter():
            newzipfile.write(os.path.join(dirname, filename))
        newzipfile.close()
        super(ZIPFile, self).clearfiles()
        self.archive.close()
        try:
            if os.path.isfile(self.filename+".bak"):
                os.remove(self.filename+".bak")
            os.rename(self.filename, self.filename+".bak")
            os.rename(self.filename+"~temp", self.filename)
        except:
            raise ValueError("Cannot rename orignal file %s." % self.filename)
        
    def scanstores(self):
        """Populate the internal store data."""
        for dirname, filename in self.file_iter():
            # TODO: Here os.path.join(dirname, filename) doesn't work.....
            if dirname=='':
                filepath=os.path.join(dirname, filename)
            else:
                filepath=dirname+'/'+filename
            strfile = wStringIO.StringIO(self.archive.read(filepath))
            strfile.filename = filename
            store = factory.getobject(strfile)
            self.storedata.append(store)
            
    def scanfiles(self):
        """Populate the internal file data."""
        self.filedata = []
        self.archive = zipfile.ZipFile(self.filename)
        for completename in self.archive.namelist():
            subdir, name = os.path.split(completename)
            self.filedata.append((subdir, name))

