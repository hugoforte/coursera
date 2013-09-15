import random
import unittest
import datetime as dt
import QSTK.qstkutil.qsdateutil as du
import homework1

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_simulate_return_four_values(self):
        try:
            vol, daily_ret, sharpe, cum_ret = homework1.simulate('1/1/1', '2/2/2', ['GOOG','AAPL','GLD','XOM'], [0.2,0.3,0.4,0.1])
        except ValueError:
            print("Four return values expected!")
            self.assertEquals(0, 1)

        self.assertEquals(1, 1)

    def test_send_in_real_data(self):
        tickers = ["AAPL", "GLD", "GOOG", "$SPX"]
        startDate = dt.datetime(2006, 1, 1)
        endDate = dt.datetime(2010, 12, 31)
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
            adjustedCloseValues = homework1.getAdjustedCloseValuesForTicker(startDate, endDate, [ticker])
            self.assertEquals(len(adjustedCloseValues),252)



                    

if __name__ == '__main__':
    unittest.main()