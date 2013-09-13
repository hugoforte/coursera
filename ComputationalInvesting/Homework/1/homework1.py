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
	vol = 0
	daily_ret = 1
	sharpe = 2
	cum_ret = 3
	return(vol, daily_ret, sharpe, cum_ret)

# >>> import collections
# >>> point = collections.namedtuple('Point', ['x', 'y'])
# >>> p = point(1, y=2)
# >>> p.x, p.y
# (1, 2)
# >>> p[0], p[1]
# (1, 2)