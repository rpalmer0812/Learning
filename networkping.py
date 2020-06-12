import os
import re

pingfiles = []
filepath = input('Please enter where files are stored:(Ex: C:files)  :   ')
filepath = filepath + ''
beginning = input('Please enter what each file starts with: (Ex: ping_plant)  :  ')
for root, dirs, files in os.walk(filepath):
	for file in files:
		if file.startswith(beginning):
			pingfiles.append(file)

pingtimes = []

for file in pingfiles:
    filename = filepath + file
    openfile = open(filename, 'r')
    lines = openfile.readlines()
    responsetimes = re.findall(r'bytes=32 time=(d+)ms', str(lines))
    pingtimes = pingtimes + responsetimes
    openfile.close()

pingtimes = [int(i) for i in pingtimes]
print("Maximum ping time is", max(pingtimes))
print("Minimum ping time is", min(pingtimes))
print("Average ping time is", round(sum(pingtimes) / len(pingtimes)),) 
