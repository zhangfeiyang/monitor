#!/usr/bin/env python

import sys
import os
import time
import random 
while True:
	lines = os.popen('hep_q -u zhangfy').readlines()
	while 'ERROR' in lines:
		lines = os.popen('hep_q -u zhangfy').readlines()
	jobs = len(lines)-4

	while jobs < 1005:
		First = lines[-3].split("_")[1].split('.')[0]
		First = int(First)+1 
		seed = int(random.uniform(0,2))
		if seed == 0:
			cmd = "./cls4.py "+str(First)+" "+str(First+10)
		else:
			cmd = "./cls5.py "+str(First)+" "+str(First+10)
			
		os.system(cmd)

		lines = os.popen('hep_q -u zhangfy').readlines()
		jobs = len(lines)-4

	time.sleep(30)
