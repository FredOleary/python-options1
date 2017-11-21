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
    
PARSER = argparse.ArgumentParser()
PARSER.add_argument("-t", "--ticker", help="Ticker to chart, (MSFT, AAPL..., Default=AAPL)", dest="ticker", default="AAPL")
ARGS = PARSER.parse_args()

chart1 = chart.ChartOption( ARGS.ticker, ["2017-11-24", "2017-12-01", "2017-12-08", "2017-12-15", "2017-12-22"])
print(ARGS.ticker)
chart1.get_option_prices()

chart1.make_chart()

