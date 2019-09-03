from optopsy.enums import OrderType

from random import randint


class OrderFilter:
    def __init__(
        self,
        order_id,
        is_same_expiration_for_all_legs=True,
        is_same_strike_for_all_legs=False,
        scale_by_quantity=False,
    ):
        self.order_id = order_id
        self.is_same_expiration_for_all_legs = is_same_expiration_for_all_legs
        self.is_same_strike_for_all_legs = is_same_strike_for_all_legs
        self.scale_by_quantity = scale_by_quantity

        self.legs = []

    def select_by(self, scale_by_quantity=False):
        pass

    def rank_by(self):
        pass

    def size_by(self):
        pass

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
