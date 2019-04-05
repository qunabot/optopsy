class DateRule:
    def __init__(self):
        pass

    def on(self, dates=None, year=year, month=month, day=day):
        """
        Specifies an event should fire on a specific date
        """

    def every(self, days):
        """
        Specifies an event should fire on specific days of the week
        """

    def every_day(self, symbol=None):
        """
        Specifies an event should very everyday the specified symbol is trading
        """

    def month_start(self, symbol=None):
        """
        Specifies an event should fire on the first tradable day for the
        specified symbol of each month
        """

    def month_end(self, symbol=None):
        """
        Specifies an event should fire on the last tradable day for the
        specified symbol of each month
        """

    def week_start(self, symbol=None):
        """
        Specifies an event should fire on the first tradable day for the
        specified symbol of each week
        """

    def week_end(self, symbol=None):
        """
        Specifies an event should fire on the last tradable day for the
        specified symbol of each week
        """
