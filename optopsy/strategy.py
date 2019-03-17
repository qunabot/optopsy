from abc import ABCMeta, abstractmethod
import pandas as pd


class Strategy():
    """Strategy is an abstract base class providing an interface for
    all subsequent (inherited) trading strategies.

    The goal of a (derived) Strategy object is to output a list of trades,
    which has the form of a time series indexed pandas DataFrame.
    """
    __metaclass__ = ABCMeta

    def __init__(self, option_chains):
        self.option_chains = option_chains
        self.trades = None
        self.on_init()

    def add_trades(self, options):
        self.trades = pd.concat([self.option_chains, options])

    @abstractmethod
    def on_init(self):
        raise NotImplementedError("Should implement on_init()!")

    def on_data(self, data):
        """An implementation is required to return the DataFrame of trades
        with the entry conditions applied"""
        raise NotImplementedError("Should implement on_data()!")

    def set_start_date(self, year, month, day):
        pass

    def set_end_date(self, year, month, day):
        pass

