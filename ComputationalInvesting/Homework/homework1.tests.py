import random
import unittest
import datetime as dt
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
        allocations = ["AAPL", "GLD", "GOOG", "$SPX"]
        vol, daily_ret, sharpe, cum_ret = homework1.simulate('1/1/1', '2/2/2', ['GOOG','AAPL','GLD','XOM'], [0.2,0.3,0.4,0.1])        

        self.assertEquals(1, 1)

if __name__ == '__main__':
    unittest.main()