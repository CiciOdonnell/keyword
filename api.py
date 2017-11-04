#!/usr/bin/env python

import requests
import json

# Call:
#  curl -X GET 'https://www.googleapis.com/pagespeedonline/v2/runPagespeed?url=https://www.google.com'
#
# and parse the JSON for the specific fields.
