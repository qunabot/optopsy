from optopsy.orders.order_filters.order_filter_scope import OrderFilterScope


class OrderFilterScope4(OrderFilterScope):
    def __init__(self,
        is_same_expiration_for_all_legs=True,
        is_same_strike_for_all_legs=False,
        scale_by_quantity=False
    ):
        pass

    def dist_between_higher_long_and_short_strikes(self, min, max):
        pass

    def dist_between_lower_long_and_short_strikes(self, min, max):
        pass

    def dist_between_long_and_short_strikes(self, min, max):
        pass

    def dist_between_strikes(self, min, max):
        pass

    def pct_dist_between_strikes(self, min, max):
        pass