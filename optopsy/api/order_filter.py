#     Optopsy - Python Backtesting library for options trading strategies
#     Copyright (C) 2018  Michael Chu

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.


class OrderFilter:
    def __init__(self, order_legs):
        self.order_legs = order_legs

    def days_to_expiration(self, min_days, max_days):
        pass

    def abs_delta(self, min_delta, max_delta):
        pass

    def delta(self, min_delta, max_delta):
        pass

    def distance_between_strikes(self, min, max):
        pass

    def expiration_date(self, date):
        pass

    def percentage_distance_from_underlying(self, min, max):
        pass

    def price(self, min, max):
        pass

    def at_the_money(self):
        pass

    def in_the_money_percentage(self, min, max):
        pass

    def out_of_the_money_percentage(self, min, max):
        pass
