from threading import Thread
import os
import math

def calc():
	for i in range(0, 4000000):
	   math.sqrt(i)
threads =[]

for i in range(os.cpu_count()):
	print('registering thread %d' % i)
	threads.append(Thread(target=calc))

for thread in threads:
	thread.start()

for thread in threads:
	thread.join()

************************************************************
from multiprocessing import Process
import os
import math

def calc():
	for i in range(0, 70000000):
	   math.sqrt(i)
processes =[]

for i in range(os.cpu_count()):
	print('registering process %d' % i)
	processes .append(Process(target=calc))

for process in processes:
	process.start()

for process in processes:
	process.join()
