import pandas as pd
from abc import ABCMeta, abstractmethod
from datetime import datetime
from optopsy.strategies.option_chain import OptionChain
from optopsy.api.enum import Brokerage, OrderAction
from optopsy.api.scheduler import Scheduler


class Strategy:
    """Strategy is an abstract base class providing an interface for
    all subsequent (inherited) trading strategies.

    The goal of a (derived) Strategy object is to output a list of trades,
    which has the form of a time series indexed pandas DataFrame.
    """

    __metaclass__ = ABCMeta

    def __init__(self, option_chains):
        self._option_chains = option_chains
        self._trades = None
        self.initial_cash = 10000
        self.broker = Brokerage.THINKORSWIM
        self.start_date = None
        self.end_date = None
        self.scheduler = Scheduler()
        self.on_init()

    def add_trades(self, options):
        self.trades = pd.concat([self._option_chains, options])

    def get_instrument(self, symbol):
        return OptionChain(symbol, self._broker)

    def buy(self, order):
        self._broker.send_order(order, OrderAction.BUY)

    def sell(self, order):
        self._broker.send_order(order, OrderAction.SELL)

    @property
    def start_date(self):
        return self.start_date

    @start_date.setter
    def start_date(self, value):
        self.start_date = value

    @property
    def end_date(self):
        return self.end_date

    @end_date.setter
    def end_date(self, value):
        self.end_date = value

    @property
    def initial_cash(self):
        return self.initial_cash

    @initial_cash.setter
    def initial_cash(self, value):
        self.initial_cash = value

    @property
    def brokerage(self):
        return self.brokerage

    @brokerage.setter
    def brokerage(self, value):
        self.brokerage = value

    @abstractmethod
    def on_init(self):
        raise NotImplementedError("Should implement on_init()!")

    @abstractmethod
    def on_data(self, data):
        """An implementation is required to return the DataFrame of trades
        with the entry conditions applied"""
        raise NotImplementedError("Should implement on_data()!")
