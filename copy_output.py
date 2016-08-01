from shutil import copyfile
import os.path

def demo():
	print 'Attempting copy simple_config to STEP1/part1'

	dest = "STEP1/part2/simple_config"
	copyfile("simple_config",dest)

	print ' check ?'
	if not os.path.isfile(dest):
		print '\tOperation failed :(..'
	else:
		print 'Success!'

def copy_output(is_gold):

	src = "STEP1"
	dest = "no_gold"
	if is_gold=="y":
		dest = "with_gold"
		#need to change the config file correspondingly

	nope = (5,10,12,18,22,24)# parts rejected
	for i in range(1,31):

		if i in nope:
			print '\nnot copying for part',i,'\n'
			continue

		else:
			current_part = "/part"+str(i)
			fname = "/label_prop_output"
			srcfile = src+current_part+fname+".txt"
			destfile = dest+fname+"_part"+str(i)+".txt"
			
			copyfile(srcfile,destfile)
			print 'Copied for part',i,'\n'


	print 'all label_prop_output from STEP1 copied to ',dest
	print 'with the extension part'

gold = raw_input("Enter y to copy to gold folder : ")
copy_output(gold)