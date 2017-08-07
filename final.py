import os
import random
from collections import defaultdict
import results_important

def merge_graph(n):
	partdir = ""
	f2 = open(partdir+"Step2/input_graph.txt",'r')
	f3= open(partdir+"Step3/input_graph_unmerged.txt",'r')
	text2 = f2.read()
	text3 = f2.read()
	data2 = text2.split('\n')
	data3 = text3.split('\n')
	dic = defaultdict(lambda:defaultdict(lambda:float))
	for each in data2:
		try:
			temp = each.split('\t')
			dic[temp[0]][temp[1]] = float(temp[2])
		except IndexError:
			print "IndexError1"
	for each in data3:
		try:
			temp = each.split('\t')
			if temp[0] in dic:
				if temp[1] in dic[temp[0]]:
					dic[temp[0]][temp[1]] += float(temp[2])
				else:
					dic[temp[0]][temp[1]] = float(temp[2])
			else:
				dic[temp[0]][temp[1]] = float(temp[2])
		except IndexError:
			print "IndexError"
	string = ""
	for key in dic:
		for each in dic[key]:
			string += key + '\t' + each +'\t'+ str(dic[key][each])+'\n'
	f = open(partdir+"Step3/input_graph.txt",'wb')
	f.write(string)
	f.close()

def runpyfile(filename):
	os.chmod(filename,0755)#mark executable first
	os.system("python2 "+filename)

def gen_gold(n,l1range,l2range,l1gold,l2gold):
	f = open("Step1/seeds.txt",'r')
	string = f.read()
	f.close()

	string = string.split("\n")
	seedout = ""
	excessout = ""
	goldout = ""
	for each in string:
		if(len(each.split("\t")) < 2):
			print "see"
			continue
		if each.split("\t")[1] == "L1":
			x = random.randrange(0,l1range)
			if x < l1gold:
				excessout += each + "\n"
			else:
				seedout += each + "\n"
		else:
			x = random.randrange(0,l2range)
			if x < l2gold:
				excessout += each + "\n"
			else:
				seedout += each + "\n"

	f = open("Step1/seeds.txt",'wb')
	f.write(seedout)
	f.close()

	f = open("gold_labels.txt",'wb')
	f.write(excessout)
	f.close()




def main(n):
	os.chdir("part"+str(n)+"/")
	runpyfile("1_graph.py")
	print "----->",n," finished 1_graph"
	# generating gold for each file
	if n==23:
		gen_gold(n,100,100,50,30)
	else:
		gen_gold(n,100,100,50,50)
	os.system("junto config junto1")
	print "----->",n," finished junto1"

	runpyfile("2_graph.py")
	print "----->",n," finished 2_graph"

	os.system("junto config junto2")
	print "----->",n," finished junto2"

	runpyfile("3_graph.py")
	merge_graph(n)
	print "----->",n," finished 3_graph"

	os.system("junto config junto3")
	print "----->",n," finished junto3"

	os.chdir("..")


def results(n):
	p_dir = "part"+str(n)+"/"

	f = open(p_dir+"Step3/label_prop_output.txt",'r')
	f1 = open(p_dir+"gold_labels.txt",'r')
	s1 = f.read()
	s2 = f1.read()
	f.close()
	f1.close()

	s1 = s1.split("\n")
	s2 = s2.split("\n")

	tot = [0,0]

	dic = {}
	for each in s2:
		k = each.split("\t")
		if len(k) < 2:
			continue
		dic[k[0]] = k[1]
		if k[1] == "L1":
			tot[0] += 1
		elif k[1] == "L2":
			tot[1] += 1

	res = [0,0]

	for each in s1:
		k = each.split("\t")
		if len(k) < 2:
			continue
		if k[0] in dic:
			if k[1][0:2] == dic[k[0]]:
				if dic[k[0]] == "L1":
					res[0] += 1
				else:
					res[1] += 1

	print "total",tot
	print "result",res


def run():
	parts = [2, 15,23,26,29]
	print "hi\n"
	while True:
		print "Choose an option\n1. Run some part\n2. Get results of some part\n3. generate results\n4. Exit \n"
		choice = int(input())
		if choice == 1:
			print "Give some part number\nEnter 0 to run all parts\n"
			opt = int(input())
			if opt == 0:
				for each in parts:
					print "Running part",each
					main(each)
			else:
				if opt in parts:
					print "Running part",opt
					main(opt)
				else:
					print "Give a proper option\n"
		
		elif choice == 2:
			print "Give some part number\nEnter 0 to get results of all parts\n"
			opt = int(input())
			if opt == 0:
				for each in parts:
					print "Showing results for part",each
					results(each)
			else:
				if opt in parts:
					print "Showing results for part",opt
					results(opt)
				else:
					print "Give a proper option\n"

		elif choice == 3:
			

		elif choice == 4:
			return 

		else:
			print "Give a proper choice\n"

	print "done"

run()
