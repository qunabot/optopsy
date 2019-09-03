from optopsy.orders.order_filters.order_filter_scope import OrderFilterScope


class OrderFilterScope2(OrderFilterScope):
    def __init__(self,
        is_same_expiration_for_all_legs=True,
        is_same_strike_for_all_legs=False,
        scale_by_quantity=False,
    ):
        pass

    def days_between_expiration(self, min_days, max_days):
        pass

    def dist_between_strikes(self, min, max):
        pass

    def pct_dist_between_strikes(self, min, max):
        pass