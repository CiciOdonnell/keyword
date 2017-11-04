#!/usr/bin/env python

import requests
import json

# Silence the annoying warnings
from requests.packages.urllib3.exceptions import InsecurePlatformWarning, InsecureRequestWarning, SNIMissingWarning
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(SNIMissingWarning)

# Call:
#  curl -X GET 'https://www.googleapis.com/pagespeedonline/v2/runPagespeed?url=https://www.google.com'
#
# and parse the JSON for the specific fields.

r_pagespeed = requests.get('https://www.googleapis.com/pagespeedonline/v2/runPagespeed?url=https://www.google.com')

#print will only show the status code:200=good
print r_pagespeed

#print with json suffix will print the results to terminal
#print r_pagespeed.json()

#Now parse the json
#"ruleGroups": {
#  "SPEED": {
#   "score": 100
#  }
# },

#save results to an object called "data"
#object is only saved in memory, disappers when script is complete
data=r_pagespeed.json()

#print data['ruleGroups']['SPEED']['score']
rule_groups = data['ruleGroups']
speed = rule_groups['SPEED']
score = speed['score']
print score


