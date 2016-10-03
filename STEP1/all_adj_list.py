from collections import defaultdict
import io,json
import csv
import os
import time
d = defaultdict(lambda : list())

def create_adjList(i):
	"""
		create adjacency list for each part and save
		it to a json file
	"""
	f = open("part"+str(i)+"/input_graph.txt","r")
	string = f.read().split("\n")
	f.close()
	y = 0
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
		except:
			print(line)
	with io.open("part"+str(i)+"/adj_list.txt", "w", encoding="utf8") as f:
		f.write(unicode(json.dumps(d,f,indent=4,ensure_ascii=False,sort_keys=True)))

if __name__ == '__main__':

	imp_part = (2,15,23,26,29)
	#for i in imp_part:
	#	print"List for part",i
	#	create_adjList(i)
	#	time.sleep(2)
	create_adjList(3)