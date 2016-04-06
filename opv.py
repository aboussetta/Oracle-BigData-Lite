"""
@author: Hamsavardhini
"""
import csv
import urllib
from collections import defaultdict
import config

columns = defaultdict(list) # each value in each column is appended to a list

with open(config.vertexFile) as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value
            columns[k].append(v) # append the value into the appropriate list based on column name k

VertexList = set((columns['Target'] + columns['End'])) #Single list for all the names to create vertex

output_file = open('opv.csv', 'w')
#To get rid default the line terminator is '\r\n'
w = csv.writer(output_file, lineterminator='\n')
w.writerow(["vertex_ID","key_name","value_type","key_value","value","value"]) #CSV Header
incrementer = 1
for vertex in VertexList:
    w.writerow([incrementer,"name",1,urllib.quote(str(vertex)),"",""])
    incrementer += 1