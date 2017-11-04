#!/usr/bin/env python
print 'hello world'

import csv

with open("keyword.csv") as csvfile:
   reader = csv.DictReader(csvfile)
   for row in reader:
     if row['keyword'] == "" : #if empty, continue to next line
       continue
     print(row['cluster'], row['keyword'])

with open("database.csv") as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    if not row['keyword']:
      continue
    print(row['keyword'], row['volume'])

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
         print(keyword_row['cluster'], keyword_row['keyword'],database_row['volume'])

 


