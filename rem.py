import os

filer = raw_input("What file to remove ? ")
what = "rm -f "+filer
os.system(what)