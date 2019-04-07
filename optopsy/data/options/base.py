"""
This module is the base class providing an interface for all subsequent
inherited option data providers.

The goal of this object is to output a set of events for each
data point and places them into the backtest's queue object.
"""
from abc import ABC, abstractmethod


class OptionDataProvider(ABC):
    """
    This class acts as the base class for all subsequent inherited
    option data provider objects.

    """

    def __init__(self, queue):
        self.queue = queue
        self.iterator = None
        self.option_chains = {}
        self.active = True

    @abstractmethod
    def stream_next(self):
        raise NotImplementedError("Must implement stream_next() method!")

    @abstractmethod
    def validate_source(self):
        raise NotImplementedError("Must implement data validate_source() method!")

    def is_empty(self):
        return self.option_chains is None

    def subscribe(self, symbol, chains):
        self.validate_data(chains)
        self.option_chains[symbol] = chains

    def update_iterator(self):
        self.iterator = OptionChainIterator(self.option_chains)

