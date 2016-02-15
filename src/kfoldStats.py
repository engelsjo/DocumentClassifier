"""
Find the max and average effectiveness rate from a file of many trials.
"""

import sys

percents = []

with open(sys.argv[1], 'rb') as fileHandler:
    for line in fileHandler:
        # remove last two characters (% )
        string = line[:-2]
        # convert to number
        num = int(string)
        # add to list of percents
        percents.append(num)
    # find the max and avg
    print "Max: ", max(percents)
    print "Avg: ", sum(percents) / len(percents)
