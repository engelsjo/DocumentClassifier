#!/usr/bin/python
from stemming.porter2 import stem
import numpy as np
import sys
import datetime as dt
import re
import preprocess_sentiment as ps

# given a csv, generate a numpy array of lists 
def read_csv_to_matrix(csv_file):
    data_dict = {}
    #data_list = []
    with open(csv_file,'rb') as myfile:
        for line in myfile:
            list_line = line.strip('.:;\n"\r"').split(',')
            #print list_line
            if len(list_line) == 3:
                text = stem(list_line[2])            
                text = ps.processAll(text)
                print "POSITIVE "+text.strip(' ')

            #if list_line[1] == "1":
            #    print "POSITIVE "+text
            #elif list_line[1] == "0":
            #    print "NEGATIVE "+text

if ( len(sys.argv) != 2 ):
        print 'program parameters incorrect'
        print 'usage: ./prog.py filename '
        print 'example dataset: sample_SET2_P01.csv' 
        sys.exit(2)    
else:
    filename = sys.argv[1]
#filename = "../../twitterData.csv"

read_csv_to_matrix(filename)

#print myList

