from shutil import copyfile
import os.path

print 'Attempting copy simple_config to STEP1/part1'

dest = "STEP1/part2/simple_config"
copyfile("simple_config",dest)

print ' check ?'
if not os.path.isfile(dest):
	print '\tOperation failed :(..'
else:
	print 'Success!'
