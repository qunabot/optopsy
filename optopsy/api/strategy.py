import logging

from optopsy.api.order_filter import OrderFilter


class Strategy:
    def __init__(self):
        self.on_init()
        self.orders = []

    def get_instrument(self, symbol):
        """
        Create a new order with this instrument
        """
        new_order = OrderFilter(symbol)
        self.orders.append(new_order)
        return self.orders[-1]

    def select_position_by_id(self, id):
        pass

    def on_init(self):
        """
        This method handles custom strategy initialization logic as defined by user
        """
        pass

    def entry_handler(self):
        """
        Must implement this method in custom strategy
        This method handles custom position entry logic as defined by user
        """
        pass

    def exit_handler(self):
        """
        Must implement this method in custom strategy
        This method handles custom position exit logic as defined by user
        """
        pass
