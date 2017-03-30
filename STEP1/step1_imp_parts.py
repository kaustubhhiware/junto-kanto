#!/usr/bin/env python
import Step1
import part2
import part4
import part15
import part19
import part23
import part26
import time
from shutil import copyfile
import os
import csv

# writes into results/step1_counts.csv
# step1_counts.csv has the following details for important parts
# partnum,Negative,Positive,Total,num_vruddhi,not_vruddhi,not_sure_vruddhi,Edges
# author: Kaustubh

run_separate = (2,4,15,19,23,26)
separate_exe = {'2':part2,'4':part4,'15':part15,'19':part19,'23':part23,'26':part26}
nope = (5,10,12,18,22,24)
imp_part = (2,15,23,26,29)

# i is the iterator to run all parts
count_data = [["partnum","Negative","Positive","Total","num_vruddhi","not_vruddhi","not_sure_vruddhi","Edges"]]
for i in range(1,31):
    #part removed
    if i in nope:
        print '\npart',i,'ignored\n'
        continue
    # textbook
    elif i==1:

        #use input for graph
        print '\nRunning part',i,'\n'
        count_data.append(Step1.main_new())
        print 'Part',i,'graph generated\n'

        #juntofy(i)
        time.sleep(0.5)
    elif i not in run_separate :
        print 'already generated graph for part',i
    #separate run
    else :
        print '\nRunning part',i,'\n'
        if i not in imp_part:
            separate_exe[str(i)].main_new()
        else:
            count_data.append(separate_exe[str(i)].main_new())

        print 'part',i,'graph generated\n'
        #juntofy(i)
        time.sleep(0.5)


print 'Writing now'
#print count_data
with open('../results/step1_counts.csv','wb') as csvfile:
    writer = csv.writer(csvfile , delimiter = ',')
    for eachrow in count_data :
        writer.writerow(eachrow)

"""
print '+--- Initiate Graph Generation ---+\n'
for i in range(1,31):
    if i in imp_part:
        count_data.append(m)
        """
