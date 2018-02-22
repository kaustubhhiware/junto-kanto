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

for i in range(1,4):
	for each in imp_parts:
		result_gen.analyzeForStep(i,each)