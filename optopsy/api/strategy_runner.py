class StrategyRunner:
    def __init__(self):
        """
        All backtest strategies should extend / inherit the StrategyRunnerT class.
        This class sets up the test environment in which a backtest will be run.
        This class provides several helper functions that will allow you to
        define your desired trading strategies.

        You will need to implement the handleData() function. The handleData() function
        is the function where you define your trading logic. This function will be called
        repeatedly, once with each timestep / tick of the data.

        The initialize() function is optional and can be used to initialize any class variables.
        This function is invoked only once, before the handleData() function is invoked.

        """
        pass

    def get_context(self):
        """
        View/Update the backtest settings, such as initial balance, margining type, slippage
        """

    def get_instrument(self, symbol):
        """
        Get security/instrument by its symbol
        """

    def get_option(self, symbol):
        """
        Get option by its symbol
        """
