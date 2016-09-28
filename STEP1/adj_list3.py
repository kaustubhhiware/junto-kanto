from collections import defaultdict
import io,json
import csv
import os

d = defaultdict(lambda : list())
# same file as adj_list , only for 3 uncommented
def getSet(filename):
	"""
		Get elements from file
	"""
	d = dict()
	filer = open(filename,'r')
	text = filer.read()
	data = text.split("\n")
	#print data
	for each in data:
		if len(each.split("\t"))<2:
			continue
		node = each.split("\t")[0]
		label = each.split("\t")[1]
		d[node] = label

	return d


def evalScore(i):

##	y = 0											#
	f = open("part"+str(i)+"/input_graph.txt","r")
	string = f.read().split("\n")
	f.close()
	for line in string :

##		y+= 1										#
##		if(y%100000)==0:							#
##			print y									# speed check
		try:
			word = line.split("\t")
			if word[0] == "":
				continue
			d[word[0]].append(word[1]+" "+word[2])
			d[word[1]].append(word[0]+" "+word[2])
		except:
			print(line)

	#with io.open("graph.txt", "w", encoding="utf8") as f:
	#	f.write(unicode(json.dumps(d,f,indent=4,ensure_ascii=False,sort_keys=True)))
	print "start"

	G = getSet("part"+str(i)+"/gold_labels.txt")
	#print "setG",G
	S = getSet("part"+str(i)+"/seeds.txt")

	score = defaultdict(lambda : 0)
	n1 = defaultdict(lambda : 0)
	n2 = defaultdict(lambda : 0)
	n3 = defaultdict(lambda : 0)# nth neighbor

	print "start for sure"
	x=0						#
	for each in G:
		score[each] = 0
		n1[each] = 0
		n2[each] = 0
		n3[each] = 0
		x += 1			#
		if (x%10)==0:	#
			print x		# speed check
		if each not in d:
			continue


		for nodestr in d[each]:# each neighbor
			node=nodestr.split(" ")
			
			for subnodestr in d[node[0]]:# second neighbor
				subnode=subnodestr.split(" ")

				for fartheststr in d[subnode[0]]: # third neighbor , farthest
					farthest=fartheststr.split(" ")

					if farthest[0] in S:
						score[each] += float (farthest[1])*1
						n3[each] += 1

				if subnode[0] in S:
					score[each] += float(subnode[1])*2
					n2[each] += 1

			if node[0] in S:
				score[each] += float(node[1])*3
				n1[each] += 1

		

	l=list()
	l.append(("Node(Gold)","Score","#1st neighbors","#2nd neighbors","#3rd neighbors"))
	for each in G:
		l.append((each,score[each],n1[each],n2[each],n3[each]))

	outfile = "../results/periphery/part"+str(i)+".csv"
	with open(outfile,'wb') as csvfile:
		writer = csv.writer(csvfile , delimiter = ',')
		for eachrow in l : 
			 writer.writerow(eachrow)


imp_part = (2,15,23,26,29)
#for i in imp_part:
#	print "Periphery condition for part",i
#	evalScore(i)
