import csv
import random
import numpy as np
import os

# with open('data.csv', 'rb') as csvfile:
# 	reader = csv.reader(csvfile)
# 	for row in reader:
# 		# print row
# 		# mu, sigma = 0, 0.1 
		# s = np.random.normal(mu, sigma, 1000)
os.system('rm newdata.csv')

with open('newdata.csv', 'a') as f:
	f.write('lng,lat\n')

for _ in range(1000):
	first = '%.6f'%(np.random.normal(-0.122222, 2))
	second = '%.6f'%(np.random.normal(51.56417, 2))# float(7) + random.random()-5*10
	# print row 
	with open('newdata.csv', 'a') as f:
		f.write('{},{}\n'.format(first, second))

os.system('pbcopy < newdata.csv')