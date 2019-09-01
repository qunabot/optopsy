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

import queue

from optopsy.core.strategy import Strategy
from optopsy.data.options.cboe_data import CboeOptionData


class Backtest:
    """
    This class should be used as an entry point for backtest, it will setup
    all the nessesary components for the backtest and initialize and run
    the strategy_runner class that contains the user's strategy.
    """

    def __init__(self, strategy=None, title=None):
        if self.strategy is None:
            raise Exception("Must specify strategy for backtest!")

        self.strategy = strategy
        self.title = title

        self.subscription_manager = SubscriptionManager()
        self.brokerage = DefaultBrokerage()

        self.security_manager = SecurityManager()
        self.transaction_manager = TransactionManager()
        self.portolio_manager = PortfolioManager(
            self.security_manager, self.transaction_manager
        )

        self.schedule_manager = ScheduleManager()

    def add_options(self, source, interval, **options):
        for symbol, data in options.items():
            self.option_provider.subscribe(symbol, data, interval)
        self.option_provider.update_iterator()

    def add_equities(self, source, interval, **equities):
        for symbol, data in equities.items():
            self.equity_provider.subscribe(symbol, data)

    def run(self):
        """
        Here we will take our data and supply a slice of option
        chain per trading day to the strategy to act upon.
        """
        pass
