#!/bin/sh
#Run Edit Device information Test
#Created by guanxingquan
#Time 2015-04-16

cd ../src/unitcase/
nosetests -s -v TestDeleteCamera.py
cd ~/CoreEngine5.0/linux/
