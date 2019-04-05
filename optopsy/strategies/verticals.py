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

from optopsy.core.order import Order
from optopsy.core.leg import Leg
from optopsy.core.types import OrderStrategy, OptionType, LegAction


class Vertical(Order):
    """
    This class represents a vertical option strategy
    """

    def __init__(self, symbol):
        super().__init__(symbol)

    def call_spread(self):
        """
        Create a call spread
        """
        self.order_strategy = OrderStrategy.VERTICAL_CALL_SPREAD
        self.order_legs = [
            Leg(OptionType.CALL, LegAction.BUY),
            Leg(OptionType.CALL, LegAction.SELL),
        ]
        return self

    def put_spread(self):
        """
        Create a put spread
        """
        self.order_strategy = OrderStrategy.VERTICAL_PUT_SPREAD
        self.order_legs = [
            Leg(OptionType.PUT, LegAction.BUY),
            Leg(OptionType.PUT, LegAction.SELL),
        ]
        return self
