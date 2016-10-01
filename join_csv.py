import io,json
import csv
import os
import time
#python 2

def listFromcsv(filename):
	
	d = dict()
	with open(filename, 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			if row==0:
				continue
			d[row[0]] = (row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
	return d

def dicttFromcsv(filename):

	with open(filename, mode='r') as infile:
		reader = csv.reader(infile)
		d = dict()
		for row in reader:
			d[row[0]]=(row[2],row[3])
	return d

def merger(i):
	"""
		pick up results/periphery/part(i)_gold.csv
		and results_git/step3_part_(i)_results.csv
		and add predict , goldlabel in first
	"""
	d = listFromcsv('results/periphery/part'+str(i)+'_gold.csv')
	d2 = dicttFromcsv('results_git/step3_part_'+str(i)+'_results.csv')
	#print d2
	L=list()
	L.append(("Node(Unlabel)","GoldLabel","Predicted","L1Score","L2Score","#1st nb L1","#1st nb L2","#2nd nb L1","#2nd nb L2","#3rd nb L1","#3rd nb L2",))
	for each in d:
		if each in d2:
			L.append((each,d2[each][0],d2[each][1],d[each][0],d[each][1],d[each][2],d[each][3],d[each][4],d[each][5],d[each][6],d[each][7]))

	#print L
	outfile = "results/periphery/part"+str(i)+"_gold_predict.csv"
	if os.path.isfile(outfile):
		os.system("rm "+outfile)
	os.system("touch "+outfile)
	with open(outfile,'wb') as csvfile:
		writer = csv.writer(csvfile , delimiter = ',')
		for eachrow in L : 
			 writer.writerow(eachrow)

imp_part = (2,15,23,26,29)
for i in imp_part:
	print("Merge for part",i)
	merger(i)

