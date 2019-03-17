import os
import pandas as pd
import optopsy as op
from datetime import datetime

class SampleStrategy(op.Strategy):
    """
    This is a sample strategy used to illustrate a sample usecase of
    optopsy, simulating a portolio of option strategies
    """

    def on_init(self):
        """
        Define any initialization logic here
        """
        self.set_cash(10000.0)
        self.set_brokerage(op.Brokerage.ThinkOrSwim, fill="market")

        self.set_start_date(2018, 1, 1)
        self.set_end_date(2018, 12, 31)

        self.calendar.every(op.DayOfWeek.Thursday, self.open_trade)

    def open_trade(self):
        """
        Rules to open a new trade
        """

    def on_data(self, data):
        """
        Define your trading logic here, each new data point
        will be attached to the data variable.

        Arguments:
            data: Dict object keyed by symbols added with add_option method
        """


def run_strategy():
    """
    To use your data with this library,
    convert your data set into a pandas DataFrame with
    the following list of standard column names:

    underlying_symbol
    quote_date
    expiration
    strike
    option_type
    bid
    ask
    underlying_price
    delta

    """

    # create our inport dataframes
    curr_file = os.path.abspath(os.path.dirname(__file__))
    spx = pd.read_pickle(os.path.join(curr_file, "spx.csv"))
    vxx = pd.read_pickle(os.path.join(curr_file, "vxx.csv"))

    # create a new backtest instance
    backtest = op.Backtest()

    # load the datafeeds from our dataframes
    backtest.load_data({"SPX": spx, "VXX": vxx})
    backtest.run().plot()


if __name__ == "__main__":
    run_strategy()
