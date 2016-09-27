from collections import defaultdict
import io,json
d = defaultdict(lambda : list())

def main():
	f = open("input_graph.txt","r")
	string = f.read().split("\n")
	f.close()
	for line in string :
		try:
			word = line.split("\t")
			if word[0] == "":
				continue
			d[word[0]].append(word[1]+" "+word[2])
			d[word[1]].append(word[0]+" "+word[2])
		except:
			print(line)
	with io.open("graph.txt", "w", encoding="utf8") as f:
		json.dump(d,f,indent=4,ensure_ascii=False,sort_keys=True)
main()