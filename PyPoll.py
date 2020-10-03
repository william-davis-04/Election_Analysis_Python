import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources', 'election_results.csv')
#open the election results and read the file. 
with open(file_to_load) as election_data:
    
    #To do: read an anaylze the data here.
    file_reader = csv.reader(election_data)
    #Read and print the header row.
    headers = next(file_reader)
    print(headers)
