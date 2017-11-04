#!/usr/bin/env python #unix magic here to call python program to run this script
print 'hello world' #first python script

#once imported, does not need to be called again
#any command starting with 'csv.' is a command from the csv library
import csv

#print the keyword.csv file
with open("keyword.csv") as csvfile: #give the csv file a handle, like csvfile
   reader = csv.DictReader(csvfile) #tell python how to read it
   for row in reader:
     if row['keyword'] == "" : #if empty, continue to next line
       continue
     print(row['cluster'], row['keyword']) #now print the columns called cluster and row

#same as above
with open("database.csv") as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    if not row['keyword']:
      continue
    print(row['keyword'], row['volume'])

#combine the two files, then write them to csv
with open('keyword_output.csv', 'w') as keyword_csvfile: #first tell python we want to write something and what it will look like
  columnnames = ['cluster', 'keyword', 'volume']
  writer = csv.DictWriter(keyword_csvfile, columnnames)
  writer.writeheader()

#now add the script that returns the output we want to write to csv
  with open("keyword.csv") as keyword_file:
   with open("database.csv") as database_file:
    keyword_object=csv.DictReader(keyword_file)
    database_object=csv.DictReader(database_file)
    for keyword_row in keyword_object:
      if keyword_row['keyword'] == "":
        continue
      for database_row in database_object:
        if database_row['keyword'] == "":
         continue
        if keyword_row['keyword'] == database_row['keyword']:
        #print(keyword_row['cluster'], keyword_row['keyword'],database_row['volume'])
         writer.writerow({'cluster': keyword_row['cluster'], 'keyword': keyword_row['keyword'], 'volume':database_row['volume']})
 
#instead of printing to the terminal we write it to file
