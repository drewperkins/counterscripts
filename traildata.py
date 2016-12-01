# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 20:02:52 2016

@author: Drew
"""

import json
import matplotlib.pyplot as plt
from dateutil import parser



with open('/Users/Drew/Downloads/trail.json') as f:
    data = f.read()
    json_data = json.loads(data)

counts = []
timestamps = []
counter1 = json_data['CounterData']['TrailCounter_1']
for k,v in counter1.items():
    timestamps.append(parser.parse(v['ts']))
    counts.append(v['Count'])

plt.plot(timestamps, counts, 'ro')
plt.ylabel('some numbers')
plt.show()
