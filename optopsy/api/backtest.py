#     Optopsy - Python Backtesting library for options trading strategies
#     Copyright (C) 2018  Michael Chu

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

from optopsy.core.strategy import Strategy
import itertools
import pandas as pd


class Backtest(object):
    def __init__(self, datas=None, strategy=None):
        self.datas = datas
        self.strategy = strategy

    def _do_checks(self, data):
        required = {
            "underlying_symbol": "object",
            "quote_date": "datetime64[ns]",
            "expiration": "datetime64[ns]",
            "strike": ("float64", "int64"),
            "option_type": "object",
            "bid": "float64",
            "ask": "float64",
            "underlying_price": "float64",
            "delta": "float64",
        }

        if not all(col in data.columns.values for col in list(required.keys())):
            raise ValueError("Required columns missing!")

        data_types = data.dtypes.astype(str).to_dict()

        for key, val in required.items():
            if (key == "strike" and str(data_types[key]) not in val) or (
                key != "strike" and data_types[key] != val
            ):
                raise ValueError("Incorrect datatypes detected!")

    def _get_trade_dates(self):
        # get the unique dates across all datas
        dates = [
            pd.Series(data.quote_date.unique()).tolist() for data in self.datas.values()
        ]
        merged_dates = list(itertools.chain.from_iterable(dates))
        return sorted(set(merged_dates))

    def load_data(self, **datas):
        if isinstance(datas, dict):
            # check dataframes to make sure they have same columns
            for frame in datas.values():
                self._do_checks(frame)

            self.datas = datas

    def add_strategy(self, strategy):
        if isinstance(strategy, Strategy):
            self.strategy = strategy

    def run(self):
        """
        Here we will take our data and supply a slice of option
        chain per trading day to the strategy to act upon.
        """

        # go through each key in self.datas and retreive the data
        # column into a list of lists.
        trade_dates = self._get_trade_dates()

    def optimze(self, **kwargs):
        pass
