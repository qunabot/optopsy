"""
This is a sample strategy used for integration tests
"""

import os
import pandas as pd
import optopsy as op
from datetime import datetime


class SampleStrategy(op.Strategy):
    def on_init(self):
        self.set_cash(10000.0)
        self.set_brokerage(op.Brokerage.THINKORSWIM)

        self.start_date = datetime(2018, 1, 1)
        self.end_date = datetime(2018, 12, 31)

        self.calendar.every(op.DayOfWeek.Thursday, self.open_trade)

    def open_trade(self):
        self.buy(
            (
                self.get_instrument("SPX")
                .verticals.call_spread()
                .select_by(scale=False)
                .days_to_expiration(min_days=40, max_days=47)
                .abs_deltas(leg1=0.30, leg2=0.50)
            )
        )

        self.buy(
            (
                self.get_instrument("VXX")
                .singles.calls()
                .select_by(scale=False)
                .days_to_expiration(min_days=40, max_days=47)
                .abs_deltas(leg1=0.20)
            )
        )

    def on_data(self, data):
        """
        Define your trading logic here, each new data point
        will be attached to the data variable.

        Arguments:
            data: Dict object keyed by symbols added with add_option method
        """


def run_strategy():
    # create our inport dataframes
    curr_file = os.path.abspath(os.path.dirname(__file__))
    spx = pd.read_pickle(os.path.join(curr_file, "spx.csv"))
    vxx = pd.read_pickle(os.path.join(curr_file, "vxx.csv"))

    # create a new backtest instance
    backtest = op.Backtest()

    # load the datafeeds from our dataframes
    backtest.load_data(SPX=spx, VXX=vxx)
    backtest.add_strategy(SampleStrategy)
    backtest.run().plot()


if __name__ == "__main__":
    run_strategy()
