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

from optopsy.api.enum import LegAction


class Leg:
    def __init__(self, option_type, leg_action):
        self.option_type = option_type
        self.leg_action = leg_action

    def reverse(self):
        if self.leg_action == LegAction.BUY:
            self.leg_action = LegAction.SELL
        else:
            self.leg_action == LegAction.BUY
