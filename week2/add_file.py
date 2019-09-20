#!/usr/bin/env python3
import os

os.mkdir('/home/shiyanlou/syl')
os.mkdir('/home/shiyanlou/syl/A')
os.mkdir('/home/shiyanlou/syl/B')
os.mkdir('/home/shiyanlou/syl/C')
os.mknod('/home/shiyanlou/syl/__init__.py')
os.mknod('/home/shiyanlou/syl/A/__init__.py')
os.mknod('/home/shiyanlou/syl/B/__init__.py')
os.mknod('/home/shiyanlou/syl/C/__init__.py')


