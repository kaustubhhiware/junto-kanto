import os
from shutil import copyfile# copy files
import sys
#This program copies all label_prop_outputs from copy_argument to copy_argument+1
# ex : 1 to 2 , 2 to 3
def copy(loc):
	"""
		Copy all label_prop_outputs to STEP(loc+1)
	"""
	# only inputs are 1 and 2
	if(loc!=1 and loc!=2):
		print 'This wasn\'t suppose to happen'
		quit()
	
	src = "STEP"+str(loc)
	dest = "STEP"+str(loc+1)

	nope = (5,10,12,18,22,24)# parts rejected
	for i in range(1,31):

		if i in nope:
			print '\nnot copying for part',i,'\n'
			continue

		else:
			current_part = "/part"+str(i)
			fname = "/label_prop_output"
			srcfile = src+current_part+fname+".txt"
			destfile = dest+current_part+fname+"_step"+str(loc)+".txt"
			
			if os.path.isfile(destfile):
				print "removing older copies in part",str(i),"\n"
				os.system("rm -f "+destfile)

			copyfile(srcfile,destfile)
			if os.path.isfile(destfile):
				print 'Copied for part',i,'\n'
			else:
				print 'Failure !exit'
				sys.exit()

			if loc==2:
				#copy prop output as well as input graph1 and 2 for step 2 --> 3
				fname="/input_graph"
				srcfile1 = "STEP1"+current_part+fname+".txt"
				srcfile2 = "STEP2"+current_part+fname+".txt"
				destfile1 = "STEP3"+current_part+fname+"_step1.txt"
				destfile2 = "STEP3"+current_part+fname+"_step2.txt"
				
				if os.path.isfile(destfile1):
					print "removing older copies in part",str(i),"\n"
					os.system("rm -f "+destfile1)				
				if os.path.isfile(destfile2):
					print "removing older copies in part",str(i),"\n"
					os.system("rm -f "+destfile2)

				copyfile(srcfile1,destfile1)
				copyfile(srcfile2,destfile2)

	print 'all label_prop_output from STEP',str(loc),'copied to STEP',str(loc+1)
	print 'with the extension _step',i

	if loc==2:
		print 'input graphs from STEP1 and STEP2 copied '
		print 'to STEP3 with appropriate extensions'



#x = raw_input("Enter some num : ")
#copy(int(x))