"""
This module is responsible for compiling all data feeds in order and passing them into
the backtesting engine's event queue.

"""


class SubscriptionManager:
    """
    The subscription manager contains a list of all data feeds we're subscribed to
    and the properties of each feed.
    """
