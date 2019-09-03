import pytest


class SampleStrategy(Strategy):
    # Create a simple strategy to buy SPX calls within 31 days to expiration at 30 delta

    def on_init(self):
        spx = self.get_instrument("SPX")

    def entry_handler():
        long_calls = spx.singles().call()

        # open a call position with 31 days to expiration at 30 delta
        # returns an OrderFilter object
        filters = long_calls.select_by().days_to_expiration(30, 31).delta(0.30, 0.40)

        # open one contract sizing returns an OrderSize Object
        size = long_calls.size_by().quantity(1)

        # when multiple positions match the criteria, rank by cost basis
        # returns an OrderRank Object
        rank = long_calls.rank_by().rank_min().cost_basis()

        # buy the long calls, returns an Order Object
        self.buy("MyLongCallID", filters, size, rank)

    def exit_handler():
        self.sell(select_position(id="MyLongCallID").exit_dte(7))


@pytest.mark.usefixtures("full_data_set")
def test_strategy(full_data_set):
    results = op.backtest(SampleStrategy, full_data_set).run()
    assert results.total_profit() == 9330.0
