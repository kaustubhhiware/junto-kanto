import io,json
import csv
import os
import time
from prettytable import PrettyTable

#python 2
# join 2 csv (see def) for merger
# also compute av.score across parts into a csv

def listFromcsv(filename):

    d = dict()
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            if row==0:
                continue
            d[row[0]] = (row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
    return d

def dicttFromcsv(filename):

    with open(filename, mode='r') as infile:
        reader = csv.reader(infile)
        d = dict()
        for row in reader:
            d[row[0]]=(row[2],row[3])
    return d

def merger(i,Av):
    """
        pick up results/periphery/part(i)_gold.csv
        and results_git/step3_part_(i)_results.csv
        and add predict , goldlabel in first
        Compute results and add to Av
    """
    d = listFromcsv('results/periphery/part'+str(i)+'_gold.csv')
    d2 = dicttFromcsv('results_git/step3_part_'+str(i)+'_results.csv')

    # d2 = dicttFromcsv('results/step3_part_'+str(i)+'_results.csv')
    # results_git is the older results folder
    # this might have to be changed

    #print d2
    L=list()
    L.append(("Node(Unlabel)","GoldLabel","Predicted","L1Score","L2Score","#1st nb L1","#1st nb L2","#2nd nb L1","#2nd nb L2","#3rd nb L1","#3rd nb L2",))
    for each in d:
        if each in d2:
            L.append((each,d2[each][0],d2[each][1],d[each][0],d[each][1],d[each][2],d[each][3],d[each][4],d[each][5],d[each][6],d[each][7]))


    # It would have been easier to write in the form of array
    # but since this code is going to be read by other people as well
    # extensively variables are used
    gL1pL1_L1score = 0
    gL1pL1_L2score = 0
    gL2pL1_L1score = 0
    gL2pL1_L2score = 0
    gL1pL2_L1score = 0
    gL1pL2_L2score = 0
    gL2pL2_L1score = 0
    gL2pL2_L2score = 0

    gL1pL1_num = 0
    gL2pL1_num = 0
    gL1pL2_num = 0
    gL2pL2_num = 0

    for each in L:
        if(each[1]=="L1" and each[2]=="L1"):
            gL1pL1_L1score += float(each[3])
            gL1pL1_L2score += float(each[4])
            gL1pL1_num += 1
        elif(each[1]=="L1" and each[2]=="L2"):
            gL1pL2_L1score += float(each[3])
            gL1pL2_L2score += float(each[4])
            gL1pL2_num += 1
        elif(each[1]=="L2" and each[2]=="L1"):
            gL2pL1_L1score += float(each[3])
            gL2pL1_L2score += float(each[4])
            gL2pL1_num += 1
        elif(each[1]=="L2" and each[2]=="L2"):
            gL2pL2_L1score += float(each[3])
            gL2pL2_L2score += float(each[4])
            gL2pL2_num += 1

    # average out values
    if gL1pL1_num!=0:
        gL1pL1_L1score = int((gL1pL1_L1score / gL1pL1_num)*1000)/1000.0
        gL1pL1_L2score = int((gL1pL1_L2score / gL1pL1_num)*1000)/1000.0
    if gL1pL2_num!=0:
        gL1pL2_L1score = int((gL1pL2_L1score / gL1pL2_num)*1000)/1000.0
        gL1pL2_L2score = int((gL1pL2_L2score / gL1pL2_num)*1000)/1000.0
    if gL2pL1_num!=0:
        gL2pL1_L1score = int((gL2pL1_L1score / gL2pL1_num)*1000)/1000.0
        gL2pL1_L2score = int((gL2pL1_L2score / gL2pL1_num)*1000)/1000.0
    if gL2pL2_num!=0:
        gL2pL2_L1score = int((gL2pL2_L1score / gL2pL2_num)*1000)/1000.0
        gL2pL2_L2score = int((gL2pL2_L2score / gL2pL2_num)*1000)/1000.0

    Av.append((i,gL1pL1_L1score,gL1pL1_L2score,gL1pL2_L1score,gL1pL2_L2score,gL2pL1_L1score,gL2pL1_L2score,gL2pL2_L1score,gL2pL2_L2score))
    #print L
    outfile = "results/periphery/part"+str(i)+"_gold_predict.csv"
    if os.path.isfile(outfile):
        os.system("rm "+outfile)
    os.system("touch "+outfile)
    with open(outfile,'wb') as csvfile:
        writer = csv.writer(csvfile , delimiter = ',')
        for eachrow in L :
            writer.writerow(eachrow)


if __name__=="__main__":
    imp_part = (2,15,23,26,29)

    # initialise list for printing across all parts
    Av = list()
    Av.append(("Gold,Predict","L1,L1","L1,L1","L1,L2","L1,L2","L2,L1","L2,L1","L2,L2","L2,L2"))
    Av.append(("Part#","L1score","L2score","L1score","L2score","L1score","L2score","L1score","L2score"))
    for i in imp_part:
        print "Merged for part",i
        merger(i,Av)

    print "All parts done!Compiling results into csv..."
    #print Av
    outfile = "results/periphery_scores.csv"
    with open(outfile,'wb') as csvfile:
        writer = csv.writer(csvfile , delimiter = ',')
        for eachrow in Av :
            writer.writerow(eachrow)
