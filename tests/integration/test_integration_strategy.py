import pytest
import optopsy as op


class SampleStrategy(op.Strategy):
    """Create a simple strategy to buy SPX calls within 31 days to expiration at 30 delta"""

    def on_init(self):
        self.name = "Sample Strategy"

    def entry_handler(self):
        long_calls = self.get_instrument("SPX").call_option()

        # open a call position with 31 days to expiration at 30 delta
        long_calls.select_by().days_to_expiration(30, 31).delta(0.30, 0.40)
        long_calls.size_by().quantity(1)

        # when multiple positions match the criteria, rank by cost basis
        long_calls.rank_by().rank_min().cost_basis()
        long_calls.buy("MyLongCallID")

    def exit_handler(self):
        # self.select_position_by_id(id="MyLongCallID").exit_dte(7)
        pass


@pytest.mark.usefixtures("full_data_set")
def test_strategy(full_data_set):
    op.Backtest(SampleStrategy, full_data_set).run()
