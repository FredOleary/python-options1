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
import argparse
import ChartOption as chart
import datetime

def get_time_series(length):
    series = []
    # Monday = 0, tuesday =1, wednesday = 2... friday = 4
    current_time = datetime.datetime.now()
#    current_time = datetime.datetime( 2017, 11, 26)
    today = current_time.weekday()
    if today > 4:
        next = 4 - today +7
    else:
        next = 4 - today
    
    for delta in range(length):
        next_time = current_time +  datetime.timedelta(days=next)  
        series.append(next_time.strftime("%Y-%m-%d"))
        next += 7
    return series
    
PARSER = argparse.ArgumentParser()
PARSER.add_argument("-t", "--ticker", help="Ticker to chart, (MSFT, AAPL..., Default=AAPL)", dest="ticker", default="AAPL")
ARGS = PARSER.parse_args()

series = get_time_series(10)
print(series)
chart1 = chart.ChartOption( ARGS.ticker, series)
print(ARGS.ticker)
chart1.get_option_prices()

chart1.make_chart()

