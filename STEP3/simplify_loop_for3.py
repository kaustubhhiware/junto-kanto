#!/usr/bin/env python
import graph
import merge
from shutil import copyfile
import os
import time

# run junto for each part in Step 3
# author: Kaustubh

def juntofy(i):
    """
        generate all outputs file
    """
    #copy the simple_config to generate output
    copyfile("simple_config","part"+str(i)+"/simple_config")
    #go to each part
    os.chdir("part"+str(i))

    if os.path.isfile("label_prop_output.txt"):
        print "\t\t\t\tremoving older builds for part",str(i)
        os.system("rm -f label_prop_output.txt")

    if i==1:
        os.system("junto config simple_config")
    else:
        os.system("touch dump")
        os.system("junto config simple_config > dump")
    print '+--- output for part',i,'generated'
    #return to main STEP dir for next parts
    os.chdir("..")

nope = (5,10,12,18,22,24)
# i is the iterator to run all parts
print '+--- Initiate Graph Generation ---+\n'

for i in range(1,31):
    #part removed
    if i in nope:
        print '\npart',i,'ignored\n'
        continue
    else :
        #use input for graph
        print '\nRunning part',i,'\n'
        graph.main(i)
        merge.main(i)
        print 'Part',i,'graph generated\n'

        juntofy(i)
        time.sleep(0.5)
