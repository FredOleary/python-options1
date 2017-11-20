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

import WebOption
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

expire_range = ["2017-11-24", "2017-12-01", "2017-12-08", "2017-12-15", "2017-12-22"]
#expire_range = ["2017-11-24", "2017-12-01"]
results = []
symbol = "INTC"

for expire in expire_range:
    result = WebOption.get_option( symbol, expire)
    results.append( WebOption.options_to_lists(result, expire))

color_delta = .8/len(expire_range)
color_base = 0.0

plt.figure(figsize=(10,5))
plt.subplots_adjust(left=0.3)
rax = plt.axes([0.05, 0.4, 0.2, 0.25])
button_text = []
button_visible = []
line_plots = []
for expire in expire_range:
    button_text.append(expire)
    button_visible.append(True)

check = CheckButtons(rax, button_text, button_visible)

def func(label):
    for line in line_plots:
        if( line["expire"] == label):
            line["line"].set_visible(not line["line"].get_visible())
    plt.draw()

check.on_clicked(func)

for result in results:
    if result is not None:
        plt.subplot(1,2,1)
        plt.title( "Call Ask/Bid for " + symbol)
        line = plt.plot(result["call_stock_strike"], result["call_option_ask"], color=(1.0, color_base, color_base), label="Ask " + result["expire"])
        line_plots.append( {"expire":result["expire"], "line":line[0]})
        line = plt.plot(result["call_stock_strike"], result["call_option_bid"], color=(color_base, 1.0, color_base), label="Bid " + result["expire"])
        line_plots.append( {"expire":result["expire"], "line":line[0]})
        plt.legend(loc='upper right', frameon=False)
    
        plt.subplot(1,2,2)
        plt.title( "Put Ask/Bid for " + symbol)
        line = plt.plot(result["put_stock_strike"], result["put_option_ask"], color=(1.0, color_base, color_base), label="Ask " + result["expire"])
        line_plots.append( {"expire":result["expire"], "line":line[0]})
        line = plt.plot(result["put_stock_strike"], result["put_option_bid"], color=(color_base, 1.0, color_base), label="bid " + result["expire"])
        line_plots.append( {"expire":result["expire"], "line":line[0]})
        plt.legend(loc='upper left', frameon=False)
        
    color_base += color_delta

plt.show()
    

       

# Headers


