from collections import defaultdict
import io,json
import csv
import os
import time
d = defaultdict(lambda : list())

# change python2 code to python3
# running on server

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

## not needed this function

def unlabelledSet(i,G,S):
	"""
		create a set of nodes , such that they're not in 
		Gold labels or seeds
	"""
	print("unlabeled\n")
	U = dict()
	f = open("part"+str(i)+"/input_graph.txt","r")
	string = f.read().split("\n")
	f.close()
	for line in string :
		#try:
		word = line.split("\t")
		if word[0] == "":
			continue
		#d[word[0]].append(word[1]+" "+word[2])
		#d[word[1]].append(word[0]+" "+word[2])
		if word[0] not in G and word[0] not in S:
			U[word[0]] = 0
		if word[1] not in G and word[1] not in S:
			U[word[1]] = 0	
		#except:
			#print(line)
		return U	


def evalScore(i):

	y = 0											#
	U = dict() 	#Unlabeeled set

	G = getSet("part"+str(i)+"/gold_labels.txt")
	#print ("setG")
	#print(G)
	S = getSet("part"+str(i)+"/seeds.txt")

	f = open("part"+str(i)+"/input_graph.txt","r")
	string = f.read().split("\n")
	f.close()
	for line in string :

		y+= 1										#
		if(y%100000)==0:							#
			print(y)								# speed check
		try:
			word = line.split("\t")
			if word[0] == "":
				continue
			d[word[0]].append(word[1]+" "+word[2])
			d[word[1]].append(word[0]+" "+word[2])
			if word[0] not in G and word[0] not in S:
				U[word[0]] = 0
			if word[1] not in G and word[1] not in S:
				U[word[1]] = 0	
		except:
			print(line)

	#with io.open("graph.txt", "w", encoding="utf8") as f:
	#	f.write(unicode(json.dumps(d,f,indent=4,ensure_ascii=False,sort_keys=True)))
	print("start")


	print("Gold#"),print(len(G))
	print("Seed#"),print(len(S))
	print("Unlabeled#"),print(len(U))
	# U = unlabelledSet(i,G,S)
	#print(U)

	L1score = defaultdict(lambda : 0)
	L2score = defaultdict(lambda : 0)

	n11 = defaultdict(lambda : 0)
	n21 = defaultdict(lambda : 0)
	n31 = defaultdict(lambda : 0)# nth neighbor
	n12 = defaultdict(lambda : 0)# L2 nieghbors
	n22 = defaultdict(lambda : 0)
	n32 = defaultdict(lambda : 0)# nth neighbor

	print("start for sure")
	x=0					#
	for each in G:
		L1score[each] = 0
		L2score[each] = 0
		n11[each] = 0
		n21[each] = 0
		n31[each] = 0
		n12[each] = 0
		n22[each] = 0
		n32[each] = 0
		x += 1			#
		if (x%10)==0:	#
			print(x)		# speed check
		if each not in d:
			continue


		for nodestr in d[each]:# each neighbor
			node=nodestr.split(" ")
			
			for subnodestr in d[node[0]]:# second neighbor
				subnode=subnodestr.split(" ")

#	3rd neighbor skipped , for part 15 very high number of 
#	2nd neighbors itself

#				for fartheststr in d[subnode[0]]: # third neighbor , farthest
#					farthest=fartheststr.split(" ")
#
#					if farthest[0] in S:
#						if d[farthest[0]]=="L1":
#							L1score[each] += float (farthest[1])*1
#							n31[each] += 1
#						else:
#							L2score[each] += float (farthest[1])*1
#							n32[each] += 1

				if subnode[0] in S:
					if d[subnode[0]]=="L1":
						L1score[each] += float(subnode[1])*2
						n21[each] += 1
					else:
						L2score[each] += float(subnode[1])*2
						n22[each] += 1

			if node[0] in S:
				if d[node[0]]=="L1":
					L1score[each] += float(node[1])*3
					n11[each] += 1
				else:
					L2score[each] += float(node[1])*3
					n12[each] += 1

		

	l=list()
	l.append(("Node(Gold)","L1Score","L2Score","#1st nb L1","#1st nb L2","#2nd nb L1","#2nd nb L2","#3rd nb L1","#3rd nb L2",))
	for each in G:
		l.append((each,L1score[each],L2score[each],n11[each],n12[each],n21[each],n22[each],n31[each],n32[each]))

	outfile = "../results/periphery/part"+str(i)+"_gold.csv"
	with open(outfile,'w') as csvfile:
		writer = csv.writer(csvfile , delimiter = ',')
		for eachrow in l : 
			 writer.writerow(eachrow)

	print("Gold labels analysis done ..Repeating for unlabelled nodes")
#same code repeated
	print("start for sure")
	x=0					#
	for each in U:
		L1score[each] = 0
		L2score[each] = 0
		n11[each] = 0
		n21[each] = 0
		n31[each] = 0
		n12[each] = 0
		n22[each] = 0
		n32[each] = 0
		x += 1			#
		if (x%10)==0:	#
			print(x)		# speed check
		if each not in d:
			continue


		for nodestr in d[each]:# each neighbor
			node=nodestr.split(" ")
			
			for subnodestr in d[node[0]]:# second neighbor
				subnode=subnodestr.split(" ")

#	3rd neighbor skipped , for part 15 very high number of 
#	2nd neighbors itself

#				for fartheststr in d[subnode[0]]: # third neighbor , farthest
#					farthest=fartheststr.split(" ")
#
#					if farthest[0] in S:
#						if d[farthest[0]]=="L1":
#							L1score[each] += float (farthest[1])*1
#							n31[each] += 1
#						else:
#							L2score[each] += float (farthest[1])*1
#							n32[each] += 1

				if subnode[0] in S:
					if d[subnode[0]]=="L1":
						L1score[each] += float(subnode[1])*2
						n21[each] += 1
					else:
						L2score[each] += float(subnode[1])*2
						n22[each] += 1

			if node[0] in S:
				if d[node[0]]=="L1":
					L1score[each] += float(node[1])*3
					n11[each] += 1
				else:
					L2score[each] += float(node[1])*3
					n12[each] += 1

		

	l=list()
	l.append(("Node(Unlabel)","L1Score","L2Score","#1st nb L1","#1st nb L2","#2nd nb L1","#2nd nb L2","#3rd nb L1","#3rd nb L2",))
	for each in U:
		l.append((each,L1score[each],L2score[each],n11[each],n12[each],n21[each],n22[each],n31[each],n32[each]))

	outfile = "../results/periphery/part"+str(i)+"_unlabel.csv"
	with open(outfile,'w') as csvfile:
		writer = csv.writer(csvfile , delimiter = ',')
		for eachrow in l : 
			 writer.writerow(eachrow)




#imp_part = (2,15,23,26,29)
#for i in imp_part:
#	print("Periphery condition for part",i)
#	evalScore(i)

evalScore(29)