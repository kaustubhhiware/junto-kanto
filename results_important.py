import os
import time
from collections import defaultdict
from collections import OrderedDict
import json
import io
import random
import csv
import datetime
from prettytable import PrettyTable
import time
import result_gen

imp_parts = (2,15,23,26,29)

start = datetime.datetime.now()
print "\n Start result gen at ", start.strftime("%d-%m-%Y %H:%M:%S")+"\n"

for each in imp_parts:
	result_gen.analyzeForStep(3,each)

end = datetime.datetime.now()
print " Complete result gen at ", end.strftime("%d-%m-%Y %H:%M:%S")+"\n"