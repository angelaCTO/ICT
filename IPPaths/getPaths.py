#!/usr/bin/python -O

import os

for root, dirs, files in os.walk("."):  #TopDown = True
   for name in dirs:
      # print 'dir:'
      print os.path.relpath(name)

   for name in files:
      # print 'files:'
       print os.path.relpath(name)
       print 

