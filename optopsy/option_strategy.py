from optopsy.enums import OptionType


class OptionStrategy:
    def __init__(self, symbol):
        self.symbol = symbol
        self.strategy_name = None

    def call_option(self):
        self.strategy_name = "Single Call Option"
        self.legs.append((OptionType.CALL, 1))
        return self

    def put_option(self):
        self.strategy_name = "Single Put Option"
        self.legs.append((OptionType.PUT, 1))
        return self

    def iron_condor(self):
        pass

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
