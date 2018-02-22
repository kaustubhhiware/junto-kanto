from collections import defaultdict
from collections import OrderedDict
import json
import io
import random
import csv
import sample
import os
import time

def getNodes(filename):
	"""
		return a dict containing all nodes in gold labels
	"""
	#filename="gold_labels.txt"
	if not os.path.isfile(filename):
		print filename,"missing ! Closing now..."
		quit()
	U = dict()
	filer = open(filename,'r')
	text = filer.read()
	data = text.split("\n")
	for each in data:
		if len(each.split("\t"))<2:
			continue
		node = each.split("\t")[0]
		label = each.split("\t")[1]
		U[node] = label
	filer.close()
	return U


def combinations(index,node_dict,dic,count,vruddhi,ends_with,two_vowels,last_second,
				total,count_list):
	string = ""
	seeds_string = ""

	s_vow = ["a","e","i","o","u","f","U","I"]
	l_vow = ["A","E","O","F"]
	verbs = ['sUtra', 'rew', 'stag', 'stam', 'stan', 'stak', 'kzvel', 'vask', 'hrIC', 'vasa', 'tuYj', 'vraRa', 'Kev', 'Gu', 'Gf', 'gUr', 'rOq', 'sPuRq', 'tUl', 'Brez', 'BrAS', 'kuT', 'kuz', 'dviz', 'kuR', 'cezw', 'SlaNg', 'sTUla', 'SlaNk', 'kuw', 'kus', 'kur', 'kup', 'gaRa', 'kuk', 'gaRq', 'BrAj', 'kuq', 'kuc', 'cull', 'akz', 'glE', 'pawa', 'mev', 'mep', 'jamB', 'med', 'Kol', 'Danv', 'Kor', 'zWiv', 'brU', 'mAh', 'mAn', 'mA', 'tard', 'mI', 'Barts', 'tarj', 'kaYc', 'mlew', 'mlev', 'me', 'mi', 'mf', 'hurC', 'Dor', 'Sarb', 'vazka', 'Kaz', 'Sarv', 'Kac', 'hoq', 'saww', 'Kaq', 'Kaj', 'tIk', 'Kan', 'tIv', 'bund', 'Kad', 'lal', 'SroR', 'laj', 'laq', 'lag', 'GuMz', 'gluYc', 'law', 'lap', 'las', 'laK', 'laB', 'laC', 'laz', 'tus', 'tur', 'tup', 'SAn', 'tuw', 'tud', 'SAq', 'vara', 'varc', 'tuq', 'SAs', 'tuj', 'tuh', 'varh', 'tul', 'SAK', 'tuz', 'tuP', 'varz', 'varD', 'tuB', 'varR', 'tuR', 'riK', 'trump', 'aYj', 'hfz', 'aYc', 'tfp', 'GfR', 'vAsa', 'banD', 'tvac', 'Gfz', 'tvar', 'cumb', 'rE', 'rA', 'rI', 'Deka', 'smf', 'smi', 'maYc', 'ri', 'duz', 'AYC', 'GUrR', 'truw', 'dyut', 'trup', 'sPuRw', 'aww', 'dul', 'vyuz', 'duh', 'SvaYc', 'klIb', 'vft', 'vfj', 'vfk', 'vfh', 'diS', 'vfD', 'mrakz', 'dih', 'vfS', 'kumAra', 'vfR', 'div', 'Sev', 'vizka', 'INK', 'GuRR', 'rag', 'spfha', 'ram', 'rak', 'rah', 'mind', 'raw', 'ras', 'rap', 'muRW', 'rad', 'ray', 'raG', 'raB', 'muRq', 'raK', 'raW', 'raP', 'raD', 'stamB', 'palyUla', 'kzipa', 'camp', 'GfRR', 'do', 'hrI', 'stfh', 'nand', 'piYj', 'bust', 'kul', 'Bid', 'sur', 'ned', 'tvaYc', 'KaRq', 'baD', 'baR', 'bad', 'sraMs', 'SraT', 'bal', 'cakAs', 'nud', 'muz', 'luYj', 'raMh', 'muR', 'muw', 'mus', 'mur', 'BUz', 'mud', 'muc', 'muj', 'kAla', 'und', 'tF', 'dIkz', 'nakk', 'pAl', 'mantr', 'puww', 'nakz', 'drE', 'puwa', 'mluc', 'liNg', 'DaR', 'tutTa', 'yez', 'Co', 'sad', 'dyE', 'Ikz', 'iw', 'nikz', 'il', 'cand', 'stIm', 'iz', 'durv', 'Svart', 'iK', 'plih', 'tvakz', 'nij', 'nil', 'Svi', 'kit', 'kiw', 'kil', 'prA', 'ruMs', 'yAc', 'niS', 'ruMS', 'kala', 'prI', 'SraR', 'kall', 'pyAy', 'yakz', 'Dan', 'GaG', 'hal', 'han', 'Sram', 'Gaw', 'had', 'hay', 'vizk', 'has', 'haw', 'jri', 'jyA', 'SraTa', 'jyu', 'Svall', 'Svalk', 'vawa', 'umB', 'stfkz', 'aNga', 'gozw', 'SaNk', 'ciri', 'plu', 'pluz', 'nizk', 'plI', 'vaNK', 'Cur', 'Cup', 'SUz', 'trap', 'Dras', 'tras', 'tan', 'vaNk', 'tal', 'tak', 'SUl', 'vaNg', 'SUr', 'tay', 'taw', 'tap', 'saBAja', 'vevI', 'daRqa', 'pakz', 'nI', 'raha', 'kuMs', 'Siw', 'SraNg', 'nF', 'hamm', 'SraNk', 'nU', 'Sil', 'Siz', 'kuMS', 'vezw', 'sUca', 'wik', 'pUrR', 'kaTa', 'vAh', 'tumP', 'sfj', 'mU', 'tump', 'pust', 'Si', 'tumb', 'knUy', 'nIv', 'sfB', 'tark', 'veT', 'lABa', 'snih', 'guRq', 'kzmAy', 'roq', 'guRa', 'veR', 'sUd', 'vep', 'must', 'bfh', 'guRW', 'veh', 'jaz', 'guP', 'guD', 'guq', 'guj', 'guh', 'gur', 'gup', 'gud', 'qip', 'Pakk', 'SI', 'GrA', 'svid', 'kamp', 'DvaMs', 'rasa', 'prez', 'QOk', 'SmIl', 'SvaW', 'kzaR', 'caz', 'caR', 'Bram', 'kzal', 'kzam', 'cay', 'cad', 'car', 'cap', 'cat', 'caw', 'cak', 'cah', 'can', 'cam', 'cal', 'Bez', 'BraR', 'kzar', 'BAz', 'SvaBr', 'UrRu', 'BAs', 'mluYc', 'vakz', 'BAm', 'mas', 'pfc', 'pfq', 'svara', 'mav', 'may', 'mad', 'Urj', 'snu', 'laNK', 'sfmB', 'laNG', 'mah', 'mal', 'svard', 'maz', 'maW', 'maT', 'snA', 'sf', 'pfR', 'f', 'si', 'so', 'kurd', 'pfT', 'laNg', 'maK', 'maR', 'cuww', 'jiz', 'pUz', 'dyu', 'pUl', 'pUj', 'kfRv', 'stana', 'Jaz', 'pUr', 'Svit', 'stena', 'kuRa', 'kuRq', 'KAd', 'kuRW', 'bfMh', 'paRq', 'rakz', 'kram', 'tantr', 'ej', 'rUpa', 'CaYj', 'kand', 'BAja', 'Svind', 'krap', 'tUR', 'tUr', 'Kel', 'paza', 'eD', 'eW', 'kraT', 'dfMh', 'ez', 'yuD', 'Dukz', 'carv', 'tam', 'punT', 'carb', 'carc', 'yuC', 'saYj', 'yup', 'yut', 'yuj', 'turv', 'Dfz', 'mArg', 'kzaYj', 'tfd', 'muYc', 'ukz', 'mArj', 'de', 'kAS', 'tfh', 'df', 'du', 'dI', 'DUp', 'DUr', 'DUs', 'Sucy', 'lumb', 'dA', 'tfz', 'dE', 'kAs', 'tfR', 'dF', 'dU', 'huq', 'Brakz', 'hul', 'Kurd', 'Irkzy', 'GiRR', 'vAta', 'sah', 'san', 'sam', 'sal', 'sac', 'sag', 'pru', 'ant', 'sas', 'sap', 'and', 'kliS', 'saw', 'kusm', 'saR', 'duHKa', 'saG', 'raRv', 'klid', 'sraNk', 'dakz', 'dIp', 'dram', 'niYj', 'traNk', 'DrE', 'hmal', 'taYc', 'sTuq', 'ruRw', 'Gaww', 'bAq', 'bAh', 'ruRW', 'paMs', 'bAD', 'garva', 'SaRq', 'gep', 'gev', 'BaRq', 'gez', 'vaRW', 'svAd', 'Dru', 'stoma', 'vaRw', 'sTA', 'vaRq', 'manT', 'ji', 'vraj', 'mand', 'sparD', 'jF', 'trOk', 'vraR', 'kfS', 'stup', 'hvf', 'stuc', 'spand', 'marb', 'marc', 'siv', 'DrANkz', 'Buv', 'pruz', 'Buj', 'marv', 'naK', 'stuB', 'cft', 'daridrA', 'takz', 'krand', 'cyut', 'paS', 'mfq', 'paT', 'mfj', 'SunD', 'kzur', 'kzud', 'mfd', 'cul', 'kzuB', 'paw', 'pad', 'samb', 'mfR', 'mfS', 'pac', 'kzuD', 'mfD', 'SloR', 'pan', 'srek', 'SlaT', 'miYj', 'Iz', 'ujJ', 'jE', 'nah', 'Ir', 'Ih', 'Ij', 'juNg', 'Sulk', 'Iq', 'Sulb', 'Scyut', 'uYC', 'rUz', 'huRq', 'Bal', 'hinv', 'Baj', 'pER', 'stim', 'amb', 'stip', 'druR', 'saMst', 'stiG', 'psA', 'nu', 'jakz', 'kfpa', 'gruc', 'sAmb', 'sAma', 'Kuj', 'BraMs', 'dinv', 'BraMS', 'oR', 'oK', 'gumP', 'mF', 'cuqq', 'kAYc', 'sru', 'yat', 'heW', 'kFt', 'garh', 'garb', 'nAs', 'gard', 'garv', 'loc', 'loq', 'lok', 'heq', 'nAT', 'garD', 'juq', 'SUra', 'yaj', 'kzRu', 'SUrp', 'sarv', 'juz', 'sAntv', 'DrAK', 'aq', 'ag', 'ah', 'ak', 'aj', 'am', 'an', 'as', 'kruS', 'aw', 'at', 'av', 'ay', 'ad', 'SumB', 'tsar', 'kruq', 'tviz', 'aR', 'aS', 'az', 'tfMh', 'ru', 'tAy', 'vAS', 'parRa', 'mask', 'vf', 'u', 'caYc', 'kvaR', 'SiNG', 'krIq', 'SIB', 'cukk', 'kumB', 'kvaT', 'kumb', 'SIk', 'mnA', 'kundr', 'SIl', 'kuts', 'taq', 'SalB', 'sPAy', 'Cidra', 'daMS', 'anDa', 'fmP', 'suh', 'GUr', 'daMs', 'mUtra', 'valk', 'Pull', 'valh', 'valg', 'Ceda', 'maha', 'valB', 'kleS', 'Tuq', 'Cand', 'vic', 'cAy', 'raNK', 'vij', 'raNG', 'vil', 'vis', 'viw', 'vid', 'viC', 'pAra', 'raNg', 'viz', 'viT', 'viD', 'glas', 'glah', 'So', 'gfD', 'vel', 'hlas', 'gfj', 'gfh', 'nind', 'SF', 'kaMs', 'mall', 'hlag', 'syand', 'SE', 'laYj', 'jYap', 'vAYC', 'grAma', 'muYj', 'vfkz', 'vruq', 'wval', 'pay', 'trE', 'praT', 'Samb', 'praC', 'styE', 'pras', 'Cid', 'panT', 'mfz', 'Baw', 'Bas', 'cel', 'piRq', 'mruc', 'tuRq', 'yu', 'iNK', 'Baz', 'kzev', 'yA', 'iNg', 'BaR', 'KaYj', 'gaYj', 'puRq', 'puRw', 'hary', 'waNk', 'yUz', 'SvaRW', 'IS', 'pul', 'bast', 'kunT', 'puq', 'jIv', 'Una', 'puw', 'niMs', 'pur', 'vfz', 'puT', 'puz', 'jez', 'yantr', 'mIl', 'suKa', 'vell', 'kaRW', 'mIv', 'kaRq', 'DI', 'parb', 'spfS', 'DA', 'parp', 'DF', 'DU', 'kruYc', 'Di', 'baMh', 'dfmP', 'De', 'Df', 'Du', 'karv', 'liK', 'karb', 'klind', 'liS', 'karj', 'galh', 'taNg', 'Kid', 'sPUrj', 'mfga', 'riRv', 'lih', 'drek', 'Kiw', 'lip', 'galB', 'buNg', 'kac', 'kab', 'kag', 'Sikz', 'kak', 'kan', 'kam', 'kal', 'kas', 'BrUR', 'kF', 'kaw', 'hUq', 'kaK', 'ki', 'kaR', 'kaS', 'kaz', 'kf', 'ku', 'kaW', 'drAh', 'piMs', 'drAq', 'aRW', 'varRa', 'lUz', 'kaqq', 'Diz', 'hiw', 'gaveza', 'nivAsa', 'fYj', 'hil', 'skamB', 'BU', 'svaYj', 'sev', 'arv', 'ard', 'arb', 'barb', 'maRq', 'arh', 'barh', 'arj', 'ark', 'sek', 'Brasj', 'maRW', 'jYA', 'knas', 'satra', 'sKal', 'sKad', 'lasj', 'pF', 'pU', 'stE', 'pA', 'pE', 'stF', 'pI', 'daG', 'dad', 'day', 'Card', 'pf', 'SyE', 'das', 'dah', 'dal', 'dam', 'stf', 'pi', 'stu', 'tev', 'gad', 'vand', 'aMsa', 'puMs', 'gam', 'gal', 'gaj', 'gaq', 'vyaya', 'taNk', 'SfD', 'granT', 'Dvf', 'rih', 'vaBr', 'ric', 'riz', 'riS', 'riP', 'SlAK', 'SlAG', 'SoR', 'Karb', 'raR', 'vye', 'Bfq', 'Bfj', 'mreq', 'bukk', 'cuw', 'cur', 'cud', 'mavy', 'cuq', 'BfS', 'kzmIl', 'snas', 'guYj', 'bil', 'lAG', 'Bakz', 'kzu', 'kzi', 'biw', 'Dakk', 'kzE', 'kzip', 'proT', 'pez', 'pev', 'kaq', 'pes', 'pel', 'larb', 'kziR', 'ruj', 'ruh', 'ruc', 'sriv', 'goma', 'rud', 'hiRq', 'rup', 'ruw', 'aMh', 'uNK', 'Barv', 'ruD', 'sAD', 'ruz', 'ruS', 'ruW', 'hizk', 'spaS', 'Byas', 'kzvid', 'taMs', 'arTa', 'luRW', 'uz', 'uK', 'uC', 'uB', 'cil', 'cit', 'uh', 'ciw', 'kuha', 'syam', 'uc', 'naB', 'kfz', 'lozw', 'naS', 'yuNg', 'paYc', 'druh', 'kfp', 'kft', 'BlAS', 'nal', 'nas', 'naw', 'kfq', 'nad', 'nay', 'SIla', 'Dvana', 'pIl', 'pIq', 'jUr', 'pIv', 'svf', 'gu', 'sUrkzy', 'kzowa', 'kUw', 'Sriz', 'kUl', 'kUj', 'gF', 'ganD', 'kUR', 'caha', 'gA', 'jaMs', 'KyA', 'yOw', 'vlI', 'raca', 'saMketa', 'jval', 'jfmB', 'hiMs', 'vela', 'jvar', 'kaNk', 'lep', 'DyE', 'dIDI', 'katra', 'vANkz', 'lAK', 'tim', 'til', 'tik', 'tij', 'Dinv', 'tip', 'lAj', 'cill', 'Blakz', 'Gur', 'aBr', 'Guw', 'damB', 'sUrkz', 'GuR', 'Guz', 'rUkza', 'jAgf', 'siD', 'siB', 'cUrR', 'lamb', 'gurv', 'nard', 'maBr', 'aNk', 'gurd', 'aNg', 'sic', 'sil', 'raYj', 'dfB', 'F', 'klam', 'purv', 'dfh', 'klaT', 'taRq', 'siw', 'bind', 'dfp', 'trand', 'lA', 'jiri', 'hras', 'lI', 'maNk', 'garj', 'glez', 'hrag', 'SuRW', 'gfYj', 'maNK', 'glev', 'glep', 'maNG', 'Cad', 'SaR', 'qap', 'Cam', 'SranT', 'Saz', 'SaW', 'Sak', 'Sam', 'Sal', 'Caz', 'Kaww', 'Sad', 'BaYj', 'Sas', 'Sap', 'Sav', 'rez', 'reB', 'skand', 'citra', 'rep', 'rev', 'svan', 'svap', 'rek', 'svad', 'GaRw', 'vah', 'sU', 'lunT', 'DvaYj', 'dfS', 'jinv', 'man', 'cyu', 'BAma', 'Bind', 'Ku', 'KE', 'arc', 'nft', 'kuww', 'miC', 'drA', 'su', 'miz', 'Pal', 'mih', 'mil', 'mid', 'dru', 'PaR', 'rAG', 'rAK', 'maMh', 'Sliz', 'rAD', 'sramB', 'skund', 'rAj', 'urv', 'rAs', 'pyE', 'Svac', 'Sval', 'Svas', 'mUl', 'jaB', 'mUz', 'kuYc', 'jaw', 'jas', 'BfMS', 'jan', 'jal', 'jam', 'jaj', 'fP', 'fz', 'fD', 'fC', 'kANkz', 'gras', 'grah', 'fc', 'lU', 'fj', 'luW', 'mfkz', 'luB', 'luw', 'karta', 'cuRq', 'luq', 'cuRw', 'kel', 'Sri', 'ramP', 'Sru', 'ramB', 'kep', 'SrA', 'SrE', 'kland', 'KuRq', 'vrI', 'ramb', 'ci', 'ac', 'yaB', 'sarj', 'sPul', 'nIl', 'sPuq', 'DmA', 'yas', 'kIw', 'yam', 'kIl', 'sPuw', 'sPur', 'Irzy', 'till', 'kUwa', 'vyaT', 've', 'aNka', 'vyaD', 'kruD', 'SOw', 'vA', 'vE', 'vI', 'vyay', 'vF', 'vyac', 'cint', 'balh', 'dAs', 'dAn', 'DvaR', 'caRq', 'i', 'dAS', 'riNg', 'gAh', 'Dvan', 'Dvaj', 'piC', 'BA', 'sAra', 'BI', 'SaS', 'dev', 'Cfd', 'BF', 'saMgrAma', 'cucy', 'lakz', 'gluc', 'sku', 'jarj', 'tej', 'aqq', 'tep', 'Bf', 'Kewa', 'mruYc', 'suww', 'DAv', 'Suc', 'Sun', 'vaYc', 'sPiww', 'murv', 'SuB', 'tvaNg', 'murC', 'SuW', 'Suz', 'SuD', 'Uy', 'cUr', 'vraSc', 'tIra', 'krI', 'Uh', 'cUz', 'Uz', 'naNK', 'vaK', 'vaR', 'mrad', 'tUz', 'cIk', 'cIv', 'katT', 'wIk', 'vaz', 'vaS', 'kzamp', 'lAYC', 'vaj', 'cIB', 'kzIv', 'Ball', 'van', 'vam', 'vac', 'smiw', 'vad', 'vay', 'lAYj', 'kzIb', 'vas', 'vap', 'kzIj', 'bus', 'hf', 'cakz', 'kmar', 'buD', 'cakk', 'hA', 'laRq', 'ind', 'hval', 'inv', 'pis', 'piw', 'wal', 'JarJ', 'inD', 'mlE', 'gfha', 'piz', 'piS', 'vIra', 'brUs', 'traMs', 'ubj', 'tfkz', 'hnu', 'sasj']
	
	Error = []
	x = 0
	errors = 0
	fish = 0	
	count_num = [0,0,0]
	
	yes = []
	no = []
	not_sure = []
	verb_nodes = []

	ground = []
	count_0 = 0
	count_1 = 0
	report = 0

	gold_string = ""
	num_gold = 0
	false_ground = 0

	for key in dic:
		for each in dic[key]:
			result = [0,0,0,0]
			temp = 0
			check = 100
			if len(each.split(" "))>2:
				fish += 1
				continue
			elif len(each.split(" "))==2:
				source = each.split(" ")[0]
			else:
				source = each
			derived = key
			vowel_count = 0
			if two_vowels:
				for char in source:
					if char in l_vow or char in s_vow:
						vowel_count += 1
				if vowel_count == 2:
					result[2] = 1
			else:
				result[2] = 0
			
			if last_second != "":
				try:
					if source[-2] == last_second:
						result[3] = 1
					else:
						result[3] = 0
				except IndexError:
					result[3] = 0
	
			else:
				result[3] = 0
			if len(source)<=2:
				continue
			while(temp<len(source)):
				if source[temp] in s_vow:
					if source[temp] == "a":
						if derived[temp] == "A":
							check = 1
							break
						else:
							check = 0
							break
					if source[temp] == "e" or source[temp] == "i" or source[temp] == "I":
						if derived[temp] == "E":
							check = 1
							break
						else:
							check = 0
							break
					if source[temp] == "u" or source[temp] =="o" or source[temp] == "U":
						if derived[temp] == "O":
							check = 1
							break
						else:
							check = 0
							break
					if source[temp] == "f":
						if derived[temp:temp+2] == "Ar":
							check = 1
							break
						else:
							check = 0
							break
				elif source[temp] in l_vow:
					if derived[temp]==source[temp]:
						check = -1
					else:
						check = 0
					break
				temp += 1
				if temp>=len(source):
					break
			if type(vruddhi) == bool:
				if check == 1:
					if vruddhi:
						ans = 1
					else:
						ans = 0
				elif check == 0:
					if vruddhi:
						ans = 0
					else:
						ans = 1
				elif check ==-1:
					ans = -1
				elif check == 100:
					errors+=1
					Error.append(x)
					check = -1
			else:
				ans = check			

			if str(source)[len(source)-1] in ends_with:
				result[1] = 1
			else:
				result[1] = 0
				ans = 0
			
			lis = sample.main()
			report_check = 0
			for each1 in lis:
				if source.startswith(each1):
					if source[-1] == "a":
						if source[len(each1):len(source)-1] in verbs:
							report_check = 1
							break

			if report_check==1:
				if len(each.split(" "))!=2:
					gold_string += "N"+str(count+x)+'\t'+"L1"+'\t'+"1.0\n"
					temp_dic = {}
					temp_dic[key] = [each,["gold"]]
					node_dict[x+count] = temp_dic
					num_gold += 1
					x+=1
					continue

			if len(each.split(" "))>1:
				if int(each.split(" ")[1]) is 0:
					count_0 += 1
				elif int(each.split(" ")[1]) is 1:
					if ans == 0:
						false_ground+=1
						continue
					count_1 += 1
				else:
					print "WTF"
				seeds_string += "N"+str(count+x)+'\t'+"L"+str(int(each.split(" ")[1])+1)+'\t'+"1.0\n"
			elif ans != 2:
				if vruddhi == True and check == 0:
					seeds_string += "N"+str(count+x)+'\t'+"L1"+'\t'+"1.0\n"
					count_0 += 1
				if vruddhi == False and check == 1:
					seeds_string += "N"+str(count+x)+'\t'+"L1"+'\t'+"1.0\n"
					count_0 += 1
			
			result[0] = 1
			temp_node_list = []
			temp_node_list.append("N"+str(count+x))
			temp_node_list.append(result)
	
			if ans is 1:
				yes.append(temp_node_list)
			elif ans is 0:
				no.append(temp_node_list)
			elif ans is -1:
				not_sure.append(temp_node_list)
			elif ans is 2:
				verb_nodes.append(temp_node_list)
			temp_dic = {}
			temp_dic[key] = [each,result]
			node_dict[x+count] = temp_dic
			x+=1

	setG = dict()

	data = gold_string.split("\n")
	#print data
	for each in data:
		if len(each.split("\t"))<2:
			continue
		node = each.split("\t")[0]
		label = each.split("\t")[1]
		setG[node] = label
	#print "setG",setG

	setS = {}
###	Generate set for seeds
	
	data = seeds_string.split("\n")
	for each in data:
		if len(each.split("\t"))<2:
			continue
		node = each.split("\t")[0]
		label = each.split("\t")[1]
		#U[node] = label
		if node not in setG:
			setS[node] = label

###	
	edgeVSG = 0
	edgeVSUL = 0
	for i in range(len(yes)):
		for j in range(i+1,len(yes)):
			weight = 0
			for k in range(4):
				if yes[i][1][k] == 1 and yes[j][1][k] == 1:
					weight += 1
			weight = float(weight)/float(total)
			string += yes[i][0]+'\t'+yes[j][0]+'\t'+str(weight)+"\n"
			if yes[i][0] in setG and yes[j][0] in setS:
				edgeVSG += 1
			elif yes[i][0] in setS and yes[j][0] in setG:
				edgeVSG += 1

			# vruddhi unlabeled and seeds
			if yes[i][0] not in setG and yes[i][0] not in setS and yes[j][0] in setS:
				edgeVSUL += 1
			elif yes[i][0] in setS and yes[j][0] not in setG and yes[j][0] not in setS:
				edgeVSUL += 1

	#print "setS",setS
	#time.sleep(1)
	#print "Vruddhi edges between Gold and Seeds : ",edgeVSG,"\n"
	edgenVSG = 0
	edgenVSUL = 0

	for i in range(len(no)):
		for j in range(i+1,len(no)):
			weight = 0
			for k in range(4):
				if no[i][1][k] == 1 and no[j][1][k] == 1:
					weight += 1
			weight = float(weight)/float(total)
			string += no[i][0]+'\t'+no[j][0]+'\t'+str(weight)+"\n"

			if no[i][0] in setG and no[j][0] in setS:
				edgenVSG += 1
			elif no[i][0] in setS and no[j][0] in setG:
				edgenVSG += 1

			if no[i][0] not in setG and no[i][0] not in setS and no[j][0] in setS:
				edgenVSUL += 1
			elif no[i][0] in setS and no[j][0] not in setG and no[j][0] not in setS:
				edgenVSUL += 1
	
	for i in range(len(no)):
		for j in range(i+1,len(verb_nodes)):
			weight = 0
			for k in range(4):
				if no[i][1][k] == 1 and verb_nodes[j][1][k] == 1:
					weight += 1
			weight = float(weight)/float(total)
			string += no[i][0]+'\t'+verb_nodes[j][0]+'\t'+str(weight)+"\n"
			if no[i][0] in setG and verb_nodes[j][0] in setS:
				edgenVSG += 1
			elif no[i][0] in setS and verb_nodes[j][0] in setG:
				edgenVSG += 1

			if no[i][0] not in setG and no[i][0] not in setS and verb_nodes[j][0] in setS:
				edgenVSUL += 1
			elif no[i][0] in setS and verb_nodes[j][0] not in setG and verb_nodes[j][0] not in setS:
				edgenVSUL += 1
					
	#print "non Vruddhi edges between Gold and Seeds : ",edgenVSG,"\n"
	#time.sleep(1)
	edgeCSG = 0 	# confused nodes
	edgeCSUL = 0

	for i in range(len(not_sure)):
		for j in range(i+1,len(not_sure)):
			weight = 0
			for k in range(4):
				if not_sure[i][1][k] == 1 and not_sure[j][1][k] == 1:
					weight += 1
			weight = float(weight)/float(total)
			string += not_sure[i][0]+'\t'+not_sure[j][0]+'\t'+str(weight)+"\n"
			
			if not_sure[i][0] in setG and not_sure[j][0] in setS:
				edgeCSG += 1
			elif not_sure[i][0] in setS and not_sure[j][0] in setG:
				edgeCSG += 1

			if not_sure[i][0] not in setG and not_sure[i][0] not in setS and not_sure[j][0] in setS:
				edgeCSUL += 1
			elif not_sure[i][0] in setS and not_sure[j][0] not in setG and not_sure[j][0] not in setS:
				edgeCSUL += 1

	for i in range(len(not_sure)):
		for j in range(len(yes)):
			weight = 0
			for k in range(4):
				if not_sure[i][1][k] == 1 and yes[j][1][k] == 1:
					weight += 1
			weight = float(weight)/(2*float(total))
			string += not_sure[i][0]+'\t'+yes[j][0]+'\t'+str(weight)+"\n"

			if not_sure[i][0] in setG and yes[j][0] in setS:
				edgeCSG += 1
			elif not_sure[i][0] in setS and yes[j][0] in setG:
				edgeCSG += 1

			if not_sure[i][0] not in setG and not_sure[i][0] not in setS and yes[j][0] in setS:
				edgeCSUL += 1
			elif not_sure[i][0] in setS and yes[j][0] not in setG and yes[j][0] not in setS:
				edgeCSUL += 1


		for j in range(len(no)):
			weight = 0
			for k in range(4):
				if not_sure[i][1][k] == 1 and no[j][1][k] == 1:
					weight += 1
			weight = float(weight)/(2*float(total))
			if weight<0:
				print "**** ERROR ****"
			string += not_sure[i][0]+'\t'+no[j][0]+'\t'+str(weight)+"\n"

			if not_sure[i][0] in setG and no[j][0] in setS:
				edgeCSG += 1
			elif not_sure[i][0] in setS and no[j][0] in setG:
				edgeCSG += 1

			if not_sure[i][0] not in setG and not_sure[i][0] not in setS and no[j][0] in setS:
				edgeCSUL += 1
			elif not_sure[i][0] in setS and no[j][0] not in setG and no[j][0] not in setS:
				edgeCSUL += 1

	#print "confused edges between Gold and Seeds : ",edgeCSG,"\n"
	#time.sleep(1)

	num_vruddhi = 0
	not_vruddhi = 0
	if vruddhi == True or type(vruddhi)!=bool:
		num_vruddhi = len(yes)
	elif vruddhi == False:
		num_vruddhi = len(no)
	if vruddhi == True or type(vruddhi)!=bool:
		not_vruddhi = len(no)
	elif vruddhi == False:
		not_vruddhi = len(yes)
	not_sure_vruddhi = len(not_sure)
	count += x
	count_list = ["part"+str(index),count_0,count_1,count-1,num_vruddhi,not_vruddhi,not_sure_vruddhi,len(string.split("\n")),num_gold,false_ground]
	
	return edgeVSG,edgeVSUL,edgenVSG,edgenVSUL,edgeCSG,edgeCSUL,len(string.split("\n"))		

def main(n,vruddhi,ends_with,two_vowels,last_second,total,count_list):
	count = 1
	node_dict = defaultdict(lambda : defaultdict(lambda : str))
	input_dict = defaultdict(lambda : defaultdict(lambda : list()))
	with open("part"+str(n)+"/"+"part"+str(n)+"_algo_file.txt") as f:
		input_dict = json.loads(f.read())
	for key in input_dict:
		edgeVSG,edgeVSUL,edgenVSG,edgenVSUL,edgeCSG,edgeCSUL,numEdge = combinations(n,node_dict,input_dict[key],count,vruddhi,ends_with,two_vowels,last_second,total,count_list)

	print "part",n,"done"
	return edgeVSG,edgeVSUL,edgenVSG,edgenVSUL,edgeCSG,edgeCSUL,numEdge			


def main_new():
	count_list = []

	return main(2,False,["a"],False,"",2,count_list)

#main_new()
