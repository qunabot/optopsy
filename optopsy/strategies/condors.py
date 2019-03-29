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

from optopsy.api.order import Order
from optopsy.api.enum import OrderStrategy, OptionType, LegAction
from optopsy.api.leg import Leg


class Condor(Order):
    """
    This class represents a vertical option strategy
    """

    def __init__(self, symbol):
        super().__init__(symbol)

    def call_condor(self):
        """
        Create a call condor
        """
        self.order_strategy = OrderStrategy.CALL_CONDOR
        self.order_legs = [
            Leg(OptionType.CALL, LegAction.BUY),
            Leg(OptionType.CALL, LegAction.SELL),
            Leg(OptionType.CALL, LegAction.SELL),
            Leg(OptionType.CALL, LegAction.BUY),
        ]
        return self

    def put_condor(self):
        """
        Create a put condor
        """
        self.order_strategy = OrderStrategy.PUT_CONDOR
        self.order_legs = [
            Leg(OptionType.PUT, LegAction.BUY),
            Leg(OptionType.PUT, LegAction.SELL),
            Leg(OptionType.PUT, LegAction.SELL),
            Leg(OptionType.PUT, LegAction.BUY),
        ]
        return self
