from optopsy.api.order_rank import OrderRank
from optopsy.api.order_size import OrderSize
from optopsy.api.order_filter_scope import OrderFilterScope
from optopsy.api.order_filter_scope2 import OrderFilterScope2
from optopsy.api.order_filter_scope3 import OrderFilterScope3
from optopsy.api.order_filter_scope4 import OrderFilterScope4
from optopsy.api.order_rank import OrderRank
from optopsy.api.order_size import OrderSize
from optopsy.api.option_strategy import OptionStrategy
from optopsy.enums import OrderType


class OrderFilter(OptionStrategy):
    def __init__(self, symbol):
        self.symbol = symbol
        self.order_id = None
        self.comment = None
        self.settings = {}
        self.legs = []

        self.side = None

    def select_by(self, scale_by_quantity=False):
        if len(self.legs) == 1:
            return OrderFilterScope()
        elif len(self.legs) == 2:
            return OrderFilterScope2()
        elif len(self.legs) == 3:
            return OrderFilterScope3()
        elif len(self.legs) == 4:
            return OrderFilterScope4()
        else:
            raise ValueError("Invalid Number of legs for this order!")

    def rank_by(self):
        return OrderRank()

    def size_by(self):
        return OrderSize()

    def buy(self, order_id=None, comment=None):
        self._gen_order(order_id, comment, OrderType.BUY)
        return self

    def sell(self, order_id=None, comment=None):
        self._gen_order(order_id, comment, OrderType.SELL)
        return self

    def _gen_order(self, order_id, comment, side):
        self.comment = comment
        self.side = side

        if order_id is None:
            self.order_id = randint(10000, 99999)
        else:
            self.order_id = order_id