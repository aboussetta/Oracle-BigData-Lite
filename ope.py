"""
@author: Hamsavardhini
"""
import csv
import urllib
from collections import defaultdict
import config

columns = defaultdict(list)

def get_ID(name):
    with open('opv_withspaces.csv') as f:
        reader = csv.DictReader(f) # read rows into a dictionary format
        for row in reader: # read a row as {column1: value1, column2: value2,...}
            if row['key_value'] == name:
                return row['vertex_ID']

incrementer = 1
predicatesList = []
output_file = open('ope.csv', 'w')
w = csv.writer(output_file, lineterminator='\n')
for line in open(config.EdgeFile):
    predicatesList = line.split(',')
    w.writerow([incrementer,get_ID(predicatesList[0]),get_ID(predicatesList[1]),urllib.quote(predicatesList[2].strip()),"","1","","",""])
    incrementer += 1
print incrementer
