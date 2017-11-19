#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 11:56:28 2017

@author: fredoleary
"""
import urllib.request
import demjson

OPTION_URL = "https://sandbox.tradier.com/v1/markets/options/chains"

def get_option(symbol, expiration):
    """
    Get the option values for various strike prices for the given expiration date
    symbol: "INTC', "MSFT'...
    expiration: Of the form YYY-MM-DD. E.g 2017-11-17
    """
    url = OPTION_URL + "?symbol=" + symbol + "&expiration=" + expiration
    try:
        req = urllib.request.Request(url)
        req.add_header("Accept", "application/json")
        req.add_header("Authorization", "Bearer FH98drEqHDafbIJDkGW71Ati3hRY")

        response = urllib.request.urlopen(req)
        result = response.read()
        str_result = result.decode("utf-8")
        options = demjson.decode(str_result)
        return options
    except urllib.error.HTTPError as err:
        print(err.code)
        return None

def options_to_lists(options, expire):
    """
    Convert the options collection lists ready for charting
    options: options collection as from get_option
    Dictionay of paired lists. eg call_stock_strike, call_option_bid
    """

    results = None
    if options["options"] is not None:
        results = {}
        results["call_stock_strike"] = []
        results["call_option_bid"] = []
        results["call_option_ask"] = []
        results["put_stock_strike"] = []
        results["put_option_bid"] = []
        results["put_option_ask"] = []
        results["expire"] = expire
        for option in options["options"]["option"]:
            if option["option_type"] == "call":
                results["call_stock_strike"].append(option["strike"])
                results["call_option_bid"].append(option["bid"])
                results["call_option_ask"].append(option["ask"])
            else:
                results["put_stock_strike"].append(option["strike"])
                results["put_option_bid"].append(option["bid"])
                results["put_option_ask"].append(option["ask"])
        results["call_stock_strike"], results["call_option_bid"], results["call_option_ask"] = \
            zip(*sorted(zip(results["call_stock_strike"], results["call_option_bid"], results["call_option_ask"])))
        results["put_stock_strike"], results["put_option_bid"], results["put_option_ask"] = \
            zip(*sorted(zip(results["put_stock_strike"], results["put_option_bid"], results["put_option_ask"])))

    return results
