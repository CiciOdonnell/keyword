#!/usr/bin/env python
print 'hello world'

import csv
with open("keyword.csv") as csvfile:
   reader = csv.DictReader(csvfile)
   for row in reader:
     print(row['cluster'], row['keyword'])

