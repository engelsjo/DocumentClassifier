#!/usr/bin/python
from stemming.porter2 import stem
import numpy as np
import sys
import datetime as dt

# given a csv, generate a numpy array of lists 
def read_csv_to_matrix(csv_file):
    data_dict = {}
    #data_list = []
    with open(csv_file,'rb') as myfile:
        for line in myfile:
            list_line = line.strip('\n"\r"').split(',')
            #data_list.append(list_line)
            #if list_line[1] in ("0", "1"):
            data_dict[stem(list_line[3])] = list_line[1]
            print list_line   
    return data_dict
    #return np.array(data_list)

filename = "../Data/twitterData.csv"

myList = read_csv_to_matrix(filename)

#print myList

