#!/usr/bin/env python
import part29_edge
import part2_edge
import part15_edge
import part23_edge
import part26_edge
import time
from shutil import copyfile
import os
import csv
import io
import json

if __name__=="__main__":

	to_run = (2,15,23,26,29)
	separate_exe = {'2':part2_edge,'15':part15_edge,'23':part23_edge,'26':part26_edge,'29':part29_edge}
	imp_part = (2,15,23,26,29)

	# i is the iterator to run all parts
	edge_data = [['Part#','<<','Vruddhi','>>','Non vruddhi','>>','Confused','Total']]
	edge_data.append([' ','Seed_Gold','Seed_Doubt','Seed_Gold','Seed_Doubt','Seed_Gold','Seed_Doubt','Edges'])

	egdeVSG = 0
	edgeVSUL = 0
	edgenVSG = 0
	edgenVSUL = 0 
	edgeCSG = 0
	edgeCSUL = 0
	numEdge = 0
	i = 1
	for i in to_run:
		print '\n+--- Running for part',i,'\n'
		#count list is not needed here , just for completion sake
		egdeVSG,edgeVSUL,edgenVSG,edgenVSUL,edgeCSG,edgeCSUL,numEdge = separate_exe[str(i)].main_new()

		edge_data.append([i,egdeVSG,edgeVSUL,edgenVSG,edgenVSUL,edgeCSG,edgeCSUL,numEdge])

	print 'Writing now'
	#print edge_data
	with open('../results/step1_edges.csv','wb') as csvfile:
		writer = csv.writer(csvfile , delimiter = ',')
		for eachrow in edge_data : 
			 writer.writerow(eachrow)