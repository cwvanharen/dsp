
from sys import argv
import csv

script, filename = argv

def read_data(data):
    '''Open csv file, read it and return a dictionary'''
    
    with open(data, 'rb') as football_csv:
        football = csv.reader(football_csv)
        fbdict = dict()
        for thing in football:
            fbdict[thing[0]] = thing[1:] 
    del fbdict['Team']
    
    return fbdict   

def get_min_score_difference(parsed_data):
    '''Takes dictionary and returns the team with smallest absolute goal difference'''
    
    dif = []
    for team, values in parsed_data.iteritems():
        dif.append((team, abs(int(values[4]) - int(values[5]))))
    minimum = min(dif, key=lambda dif: dif[1])
    
    return minimum[0]
 
    
min_dif = get_min_score_difference(read_data(filename))
print min_dif
