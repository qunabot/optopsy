import optopsy as op
import os
import pandas as pd
from datetime import datetime

"""
This is a sample strategy used for integration tests
"""


def filepath():
    curr_file = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(curr_file, "test_data/data_full.csv")


spxw = pd.read_csv(
    filepath(), parse_dates=["expiration", "quote_date"], infer_datetime_format=True
)



class SampleStrategy(op.Strategy):
    def on_init(self):
        self.set_cash(10000.0)
        self.set_brokerage(op.Brokerage.THINKORSWIM)

        self.start_date = datetime(2018, 1, 1)
        self.end_date = datetime(2018, 2, 28)

        self.scheduler.on(self.date_rules.every(DayOfWeek.Thursday, self.open_trade))

    def open_trade(self):
        self.buy(
            (
                self.get_instrument("SPXW")
                .verticals.call_spread()
                .select_by(scale=False)
                .days_to_expiration(min_days=40, max_days=47)
                .abs_deltas(leg1=0.30, leg2=0.50)
            )
        )

    def on_data(self, data):
        """
        Define your trading logic here, each new data point
        will be attached to the data variable.

        Arguments:
            data: Dict object keyed by symbols added with add_option method
        """


def test_sample_strategy():
    backtest = op.Backtest()
    backtest.add_strategy(SampleStrategy)
    backtest.load_instrument_data(SPXW=spxw)
    backtest.run()

    assert False
