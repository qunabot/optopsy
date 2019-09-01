class OptionChainIterator:
    """
    This class acts as an iterator over a pandas dataframe object
    that provides a slice of data for current iteration date
    """

    def __init__(self, option_chain):
        self.option_chain = option_chain
        self.dates = iter(self.trade_dates())

    def trade_dates(self):
        # get the unique dates across all symbols
        dates = [
            pd.Series(chain.quote_date.unique()).tolist()
            for chain in self.option_chain.values()
        ]
        merged_dates = list(itertools.chain.from_iterable(dates))
        return sorted(set(merged_dates))

    def __next__():
        curr_date = self.dates.next()
        output = {}

        for symbol, chain in self.option_chain:
            output[symbol] = chain[chain["quote_date"] == curr_date]

        return curr_date, output
