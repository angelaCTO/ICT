#!/usr/bin/python -O

import os

os.system("curl -o ZooIP.txt http://whatsmyip.us/showipsimple")
os.system("git add ZooIP.txt")
os.system("git commit -m 'update1' ZooIP.txt")
os.system("git push -u origin master")
