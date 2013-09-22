import random
import unittest
import datetime as dt
import QSTK.qstkutil.qsdateutil as du
import homework2 as homework1

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_sending_real_data_into_simulate_does_not_cause_exception(self):
        tickers = ["AAPL", "GLD", "GOOG", "$SPX"]
        startDate = dt.datetime(2011, 1, 1)
        endDate = dt.datetime(2011, 12, 31)
        allocations = [0.4, 0.4, 0.0, 0.2]
        vol, daily_ret, sharpe, cum_ret = homework1.simulate(startDate, endDate, tickers, allocations)        

        self.assertEquals(1, 1)

    def test_getNYSEDays_from_library(self):

        startDate = dt.datetime(2012, 2, 10)
        endDate = dt.datetime(2012, 2, 24)
        timeofday = dt.timedelta(hours=16)
        tradingDays = du.getNYSEdays(startDate, endDate, timeofday)

        self.assertEquals(len(tradingDays),9)

    def test_getNYSEDays_from_homework(self):
        startDate = dt.datetime(2011, 1, 1)
        endDate = dt.datetime(2011, 12, 31)

        # Get a list of trading days between the start and the end.
        tradingDays = homework1.getTradingDays(startDate, endDate)

        self.assertEquals(len(tradingDays),252)

    def test_get_adjusted_closing_values_for_equities(self):
        startDate = dt.datetime(2011, 1, 1)
        endDate = dt.datetime(2011, 12, 31)
        tickers = ["AAPL", "GLD", "GOOG", "$SPX"]

        for ticker in tickers:
            adjustedCloseValues = homework1.getAdjustedCloseValuesForTickers(startDate, endDate, [ticker])
            self.assertEquals(len(adjustedCloseValues),252)

    def test_get_normalized_close(self):
        startDate = dt.datetime(2011, 1, 1)
        endDate = dt.datetime(2011, 12, 31)
        ticker = ["AAPL"]
        normalizedCloseValues = homework1.getNormalizedCloseValuesForTickers(startDate, endDate, ticker)
        self.assertEquals(len(normalizedCloseValues),252)
        self.assertEquals(1, normalizedCloseValues[0])    

    def test_get_expected_cumulative_return(self):
        tickers = ['AAPL', 'GLD', 'GOOG', 'XOM']
        startDate = dt.datetime(2011, 1, 1)
        endDate = dt.datetime(2011, 12, 31)
        allocations = [0.4, 0.4, 0.0, 0.2]
        vol, daily_ret, sharpe, cum_ret = homework1.simulate(startDate, endDate, tickers, allocations)  

        self.assertAlmostEqual(cum_ret, 1.16487261965)
    
    
    def test_get_expected_daily_return(self):
        tickers = ['AAPL', 'GLD', 'GOOG', 'XOM']
        startDate = dt.datetime(2011, 1, 1)
        endDate = dt.datetime(2011, 12, 31)
        allocations = [0.4, 0.4, 0.0, 0.2]
        vol, daily_ret, sharpe, cum_ret = homework1.simulate(startDate, endDate, tickers, allocations)  

        self.assertAlmostEqual(daily_ret, 0.000657261102001)

    def test_get_expected_volatility(self):
        tickers = ['AAPL', 'GLD', 'GOOG', 'XOM']
        startDate = dt.datetime(2011, 1, 1)
        endDate = dt.datetime(2011, 12, 31)
        allocations = [0.4, 0.4, 0.0, 0.2]
        vol, daily_ret, sharpe, cum_ret = homework1.simulate(startDate, endDate, tickers, allocations)  
        
        self.assertAlmostEqual(vol, 0.0101467067654)

    def test_get_expected_sharpe_ratio(self):
        tickers = ['AAPL', 'GLD', 'GOOG', 'XOM']
        startDate = dt.datetime(2011, 1, 1)
        endDate = dt.datetime(2011, 12, 31)
        allocations = [0.4, 0.4, 0.0, 0.2]
        vol, daily_ret, sharpe, cum_ret = homework1.simulate(startDate, endDate, tickers, allocations)  
        
        self.assertAlmostEqual(sharpe, 1.02828403099)


    def test_full_simulate(self):
        tickers = ['AXP', 'HPQ', 'IBM', 'HNZ']
        startDate = dt.datetime(2010, 1, 1)
        endDate = dt.datetime(2010, 12, 31)
        allocations = [0.0, 0.0, 0.0, 1.0]
        vol, daily_ret, sharpe, cum_ret = homework1.simulate(startDate, endDate, tickers, allocations)  
        
        self.assertAlmostEqual(sharpe, 1.29889334008)
        self.assertAlmostEqual(vol, 0.00924299255937)
        self.assertAlmostEqual(daily_ret, 0.000756285585593)
        self.assertAlmostEqual(cum_ret, 1.1960583568)

    def test_get_all_allocations(self):
        allocations = homework1.getAllPossibleAllocations();
        self.assertEqual(len(allocations), 286)

    def test_find_best_allocation(self):
        tickers =  ['BRCM', 'TXN', 'AMD', 'ADI'] 
        startDate = dt.datetime(2011, 1, 1)
        endDate = dt.datetime(2011, 12, 31)
        allocation = homework1.find_best_allocation(startDate, endDate, tickers)  
        
        self.assertEquals(allocation, [0,0,0,1])

if __name__ == '__main__':
    unittest.main()