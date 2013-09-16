'''
Homework 1

Created on January, 24, 2013

@author: Hugo Forte
@contact: hugo@hugoforte.com
@summary: Homework 1 - figures out the best sharpe ratio allocation for holding 4 tickers for one year.
'''

# QSTK Imports
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da
import collections

# Third Party Imports
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def simulate(startDate, endDate, tickers, allocations):
    tradingDays = getTradingDays(startDate, endDate)
    numberOfTradingDays = len(tradingDays)
    # Keys to be read from the data, it is good to read everything in one go.
    keys = ['close']
    dataObject = da.DataAccess('Yahoo')
    data = dataObject.get_data(tradingDays, tickers, keys)

    # assuming there is at least one ticker
    finalNormalizedData = np.zeros(numberOfTradingDays)
    for x in range(0, 4):
        # get the data for the ticker
        normalizedData = data[0].values[:,x]
        # normalize the data
        normalizedData = normalizedData / normalizedData[0]
        # allocate the appropriate percentage
        normalizedData = normalizedData * allocations[x]
        # add the normalizedData to the finalized array
        finalNormalizedData = finalNormalizedData + normalizedData

    vol = 0
    daily_ret = 1
    sharpe = 2
    cum_ret = finalNormalizedData[numberOfTradingDays - 1]

    return(vol, daily_ret, sharpe, cum_ret)

def getTradingDays(startDate, endDate):
    timeofday = dt.timedelta(hours=16)

    # Get a list of trading days between the start and the end.
    tradingDays = du.getNYSEdays(startDate, endDate, timeofday)
    return tradingDays

def getAdjustedCloseValuesForTickers(startDate, endDate, tickers):
    tradingDays = getTradingDays(startDate, endDate)
    # Keys to be read from the data, it is good to read everything in one go.
    keys = ['close']
    dataObject = da.DataAccess('Yahoo')
    data = dataObject.get_data(tradingDays, tickers, keys)

    return data[0].values[0:len(tradingDays),0]

def getNormalizedCloseValuesForTickers(startDate, endDate, tickers):
    adjustedClose = getAdjustedCloseValuesForTickers(startDate, endDate, tickers)
    adjustedClose = adjustedClose / adjustedClose[0]
    return adjustedClose


