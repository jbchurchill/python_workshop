from os import listdir
import re
from os.path import isfile, join
onlyfiles = [ f for f in listdir('./') if isfile(join('./',f)) ]
for file in onlyfiles:
	print file
# curFile = open('S15828210_observations.csv', 'r')
# for line in curFile:
# 	print line
# print curFile.readlines()