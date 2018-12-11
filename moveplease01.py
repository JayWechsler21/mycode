#!/usr/bin/env python3
import shutil
#### importing shutil
import os
#### importing OS
os.chdir('/home/student/mycode/')
#### pathing python into the root directory
shutil.move('raynor.obj', 'ceph_storage/')
#### moving file
xname = input('What is the new name for kerrigan.obj? ')
### prompting new name
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
### renaming file
