#!/usr/bin/env python

import sys
import os
import time
import random 
while True:
	lines = os.popen('condor_q zhangfy').readlines()
	jobs = len(lines)-4

	while jobs < 1005:
		First = lines[-3].split("_")[1].split(' ')[0]
		First = int(First)+1 
		cmd = "./cls.py "+str(First)+" "+str(First+100)
		os.system(cmd)

	time.sleep(5)
