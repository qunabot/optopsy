"""
The goal of this class is to generate bar events for option
chain data from CBOE source.

The event object will contain the event itself and the data
associated with the event.

The data object will contain multiple symbols if subscribed.
"""

from optopsy.core.data.option_chains.base import OptionDataProvider
from optopsy.core.data.option_chains.iterator import OptionChainIterator


class CboeOptionData(OptionDataProvider):
    def __init__(self, queue):
        super().__init__(queue)

    def validate_source(self):
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

        if not all(col in self.data.columns.values for col in list(required.keys())):
            raise ValueError("Required columns missing!")

        data_types = self.data.dtypes.astype(str).to_dict()

        for key, val in required.items():
            if (key == "strike" and str(data_types[key]) not in val) or (
                    key != "strike" and data_types[key] != val
            ):
                raise ValueError("Incorrect datatypes detected!")

    def stream_next(self):
        try:
            return next(self.iterator)
        except StopIteration:
            self.active = False
            return

