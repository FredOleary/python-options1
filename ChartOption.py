#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 09:43:55 2017

@author: fredoleary
"""

import WebOption
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

 # pylint: disable=R0902
class ChartOption():
    """
    Chart put/call ask/bid prices for the symbol over the series specified
    """
    def __init__(self, symbol, series):
        self.symbol = symbol
        self.expire_range = series
        self.results = []
        self.button_text = []
        self.button_visible = []
        self.line_plots = []
        self.check = None
        self.color_delta = .8/len(self.expire_range)

    def get_option_prices(self):
        self.results = []

        for expire in self.expire_range:
            result = WebOption.get_option(self.symbol, expire)
            self.results.append(WebOption.options_to_lists(result, expire))

    def func(self, label):
        for line in self.line_plots:
            if line["expire"] == label:
                line["line"].set_visible(not line["line"].get_visible())
        plt.draw()

    def make_chart(self):
        color_base = 0.0

        plt.figure(figsize=(13, 5))
        plt.subplots_adjust(left=0.3)
        rax = plt.axes([0.05, 0.4, 0.2, 0.25])
        for result in self.results:
            if result is not None:
                self.button_text.append(result["expire"])
                self.button_visible.append(True)

        self.check = CheckButtons(rax, self.button_text, self.button_visible)
        self.check.on_clicked(self.func)



        for result in self.results:
            if result is not None:
                plt.subplot(1, 2, 1)
                plt.title("Call Ask/Bid for " + self.symbol)
                line = plt.plot(result["call_stock_strike"], result["call_option_ask"], \
                    color=(1.0, color_base, color_base), label="Ask " + result["expire"])
                self.line_plots.append({"expire":result["expire"], "line":line[0]})
                line = plt.plot(result["call_stock_strike"], result["call_option_bid"], \
                    color=(color_base, 1.0, color_base), label="Bid " + result["expire"])
                self.line_plots.append({"expire":result["expire"], "line":line[0]})
                plt.legend(loc='upper right', frameon=False)

                plt.subplot(1, 2, 2)
                plt.title("Put Ask/Bid for " + self.symbol)
                line = plt.plot(result["put_stock_strike"], result["put_option_ask"], \
                    color=(1.0, color_base, color_base), label="Ask " + result["expire"])
                self.line_plots.append({"expire":result["expire"], "line":line[0]})
                line = plt.plot(result["put_stock_strike"], result["put_option_bid"], \
                    color=(color_base, 1.0, color_base), label="bid " + result["expire"])
                self.line_plots.append({"expire":result["expire"], "line":line[0]})
                plt.legend(loc='upper left', frameon=False)

                color_base += self.color_delta

        plt.show()
