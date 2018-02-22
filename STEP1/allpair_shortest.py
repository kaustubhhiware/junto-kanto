from collections import defaultdict
import io,json
import csv
import os
import time
import networkx as nx
import matplotlib.pyplot as plt 
from numpy import inf
import math

def getSet(filename):
	"""
		Get elements from file
	"""
	d = dict()
	filer = open(filename,'r')
	text = filer.read()
	data = text.split("\n")
	#print(data)
	for each in data:
		if len(each.split("\t"))<2:
			continue
		node = each.split("\t")[0]
		label = each.split("\t")[1]
		d[node] = label

	return d


def makeGraph(filename,G):
	"""
		populate graph G
	"""
	l = list()
	filer = open(filename,'r')
	text = filer.read()
	data = text.split("\n")
	#print(data)
	y = 0
	for each in data:

		y+= 1										#
		if(y%100000)==0:							#
			print(y)								# speed check		
		x = each.split("\t")
		if len(each.split("\t"))<3:
			continue
		#print x[0],"--",x[1]," > ",x[2]
		G.add_edge(x[0],x[1],weight=1)#float(x[2]))

	# print G
	#nx.draw(G)
	###plt.draw()
	#plt.savefig("part"+str(i)+".png")

def allshorts(i):
	"""
		run all pair shortest path using Floyd Warshall algorithm
	"""
	G = nx.Graph()
	S = getSet("part"+str(i)+"/seeds.txt")
	#Matrix = [[0 for x in range(len(S))] for y in range(G.number_of_edges())] # placeholder for o/p
	r = defaultdict(lambda : dict())

	makeGraph("part"+str(i)+"/input_graph.txt",G)
	f = nx.floyd_warshall(G)

	for each in f:
		#print "Node ---- ",each," +++"
		for every in f[each]:
			if every in S:
				#print every,f[each][every]
				#Matrix[int(every[1:])][int(each[1:])] = f[each][every]
				r[each][every]=f[each][every]

		#print f[each]
		outStr = "\n"
	
	for each in r:
		for every in r[each]:
			outStr +=  ","+every
		break
	outStr += ",Average"
	for each in r:
		outStr += "\n"+each
		sumD = 0
		num = 0
		for every in r[each]:
			outStr += ","+str(r[each][every])
			
			if r[each][every] != inf:#math.inf:
			# no point considering non joint set
				sumD += r[each][every]
				if every!=each:# d = 0  here so ignore
					num += 1
		
		if num!=0:
			outStr += ","+str(int(1000*sumD/num)/1000.0)
		else:
			outStr += ",oo" #infinity
	outStr += "\n"
	outfile = "../results/shortest_path_part"+str(i)+"_.csv"
	with open(outfile,'w') as csvfile:
		#writer = csv.writer(csvfile , delimiter = ',')
		csvfile.write(outStr)	




if __name__ == '__main__':
	
	imp_part = (2,15,23,26,29)
	for i in imp_part:
		print("All pair shortest path for part",i)
		allshorts(i)

	#allshorts(3)