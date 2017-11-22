#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 09:43:55 2017

@author: fredoleary
Tradier options proider:
    
url:            https://sandbox.tradier.com/v1/
application:    Mesh B2 B E Services App
Access token:   FH98drEqHDafbIJDkGW71Ati3hRY
"""

import datetime

# Monday = 0, tuesday =1, wednesday = 2... friday = 4
current_time = datetime.datetime.now()
current_time = datetime.datetime( 2017, 11, 26)
today = current_time.weekday()
if today > 4:
    next = 4 - today +7
else:
    next = 4 - today

print( next)

for delta in range(10):
    next_time = current_time +  datetime.timedelta(days=next)  
    print(next_time, next_time.weekday())
    next += 7
    