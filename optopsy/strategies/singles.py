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

from optopsy.api.enum import OrderStrategy, LegAction, OptionType
from optopsy.api.order import Order
from optopsy.api.leg import Leg


class Single(Order):
    """
    This class represents a vertical option strategy
    """

    def __init__(self, symbol):
        super().__init__(symbol)

    def call_option(self):
        """
        Create a call option
        """
        self.order_strategy = OrderStrategy.CALL_OPTION
        self.order_legs = [Leg(OptionType.CALL, LegAction.BUY)]
        return self

    def put_option(self):
        """
        Create a put option
        """
        self.strategy = OrderStrategy.PUT_OPTION
        self.order_legs = [Leg(OptionType.PUT, LegAction.BUY)]
        return self
