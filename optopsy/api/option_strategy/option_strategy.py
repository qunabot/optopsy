from optopsy.enums import OptionType


class OptionStrategy:
    def __init__(self, symbol):
        self.symbol = symbol
        self.strategy_name = None

    def call_option(self):
        self.strategy_name = "Single Call Option"
        self.legs = [(OptionType.CALL, 1)]
        return self

    def put_option(self):
        self.strategy_name = "Single Put Option"
        self.legs = [(OptionType.PUT, 1)]
        return self

    def iron_condor(self):
        self.strategy_name = "Iron Condor"
        self.legs = [(OptionType.PUT, 1), (OptionType.CALL, -1), (OptionType.PUT, -1), (OptionType.CALL, 1)]
        return self

    def unbalanced_iron_condor(self):
        pass

    def call_butterfly(self):
        pass

    def put_butterfly(self):
        pass

    def iron_butterfly(self):
        pass

    def unbalanced_call_butterfly(self):
        pass

    def unbalanced_put_butterfly(self):
        pass
