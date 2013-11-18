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

"""This module provides functionality to work with directories."""

# Perhaps all methods should work with a wildcard to limit searches in some
# way (examples: *.po, base.xlf, pootle-terminology.tbx)

#TODO: consider also providing directories as we currently provide files
import os
import shutil
from translate.storage import factory


class Directory:
    """This class represents a directory."""

    def __init__(self, subdir=None):
        self.dir = subdir
        self.filedata = []
        self.storedata = []
        self.scanfiles()
        self.scanstores()

    def file_iter(self):
        """Iterator over (dir, filename) for all files in this directory."""
        if not self.filedata:
            self.scanfiles()
        for filetuple in self.filedata:
            yield filetuple

    def getfiles(self):
        """Returns a list of (dir, filename) tuples for all the file names in
        this directory."""
        return [filetuple for filetuple in self.file_iter()]

    def savefiles(self):
        """Try to save all files in this directory."""
        for store in self.storedata:
            print(type(store))
            store.save()
            
    def clearfiles(self):
        """Try to remove all temp files in this directory."""
        for store in self.storedata:
            store.close()
        for dirname, filename in self.filedata:
            if os.path.exists(dirname):
                try:
                    shutil.rmtree(dirname)
                except:
                    raise ValueError("Cannot remove temp files.")
            if os.path.exists(os.path.join(dirname, filename)):
                try:
                    os.remove(os.path.join(dirname, filename))
                except:
                    raise ValueError("Cannot remove temp files.")

    def unit_iter(self):
        """Iterator over all the units in all the files in this directory."""
        for dirname, filename in self.file_iter():
            # let skip the other filetypes            
            root, ext = os.path.splitext(filename)
            if ext[1:] not in factory.classes_str: continue
            store = factory.getobject(os.path.join(dirname, filename))
            self.storedata.append(store)
            #TODO: don't regenerate all the storage objects
            for unit in store.unit_iter():
                yield unit

    def getunits(self):
        """List of all the units in all the files in this directory."""
        return [unit for unit in self.unit_iter()]
    
    def scanstores(self):
        """Populate the internal store data."""
        for dirname, filename in self.file_iter():
            # let skip the other filetypes            
            root, ext = os.path.splitext(filename)
            if ext[1:] not in factory.classes_str: continue
            store = factory.getobject(os.path.join(dirname, filename))
            self.storedata.append(store)
            
    def scanfiles(self):
        """Populate the internal file data."""
        self.filedata = []
        '''
        def addfile(arg, dirname, fnames):
            for fname in fnames:
                if os.path.isfile(os.path.join(dirname, fname)):
                    self.filedata.append((dirname, fname))

        os.walk(self.dir, addfile, None)
        '''
        for dirname, subdirs, files in os.walk(self.dir):
            for fname in files:
                self.filedata.append((dirname, fname))
