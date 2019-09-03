from datetime import datetime
import os
import pytest
import pandas as pd
import optopsy as op
from optopsy.helpers import inspect


def filepath():
    curr_file = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(curr_file, "../test_data/data_full.csv")


data = pd.read_csv(
    filepath(), parse_dates=["expiration", "quote_date"], infer_datetime_format=True
)


class SampleCallStrategy(Strategy):
    # Create a simple strategy to buy SPX calls within 31 days to expiration at 30 delta

    def on_init(self):
        spx = self.get_instrument("SPX")

    def entry_handler():
        long_calls = spx.singles().call()

        # open a call position with 31 days to expiration at 30 delta
        # returns an OrderFilter object
        filters = long_calls.select_by().days_to_expiration(30, 31).delta(0.30, 0.40)

        # open one contract sizing
        # returns an OrderSize Object
        size = long_calls.size_by().quantity(1)

        # when multiple positions match the criteria, rank by cost basis
        # returns an OrderRank Object
        rank = long_calls.rank_by().min().cost_basis()

        # buy the long calls, returns an Order Object
        self.buy("MyLongCallID", filters, size, rank)

    def exit_handler():
        self.sell(select_position(id="MyLongCallID").exit_dte(7))


def test_long_call():
    results = op.backtest(SampleCallStrategy, data).run()
    assert results.total_profit() == 9330.0
