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

from optopsy.api.strategy import Strategy


class Backtest(object):
    def __init__(self, datas=None, strategy=None):
        self.datas = datas
        self.strategy = strategy

    def load_data(self, **datas):
        if isinstance(datas, dict):
            self.datas = datas

    def add_strategy(self, strategy):
        if isinstance(strategy, Strategy):
            self.strategy = strategy

    def run(self):
        pass

    def optimze(self, **kwargs):
        pass
