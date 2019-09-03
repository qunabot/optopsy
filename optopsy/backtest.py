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
import logging


class Backtest:
    def __init__(self, strategy, data):
        self.data = data
        self.strategies = [strategy]

    def add_strategy(self, strategy):
        self.strategies.append(strategy)

    def __run_strategy(self, strategy):
        # initialize the strategy
        strategy = strategy()

        # call entry_handler of the strategy to generate orders
        strategy.entry_handler()

        self.simulate_orders(strategy.orders)

        # call exit_handler of the strategy to handle exit logic
        strategy.exit_handler()

        return strategy

    def run(self, **params):
        self.simulated_orders = list(map(self.__run_strategy, self.strategies))

    def run_optimizer(self, strategy, **params):
        pass

    def simulate_orders(self, orders):
        # we will process all the orders of the strategy against backtest data
        logging.info("Running backtest...")
