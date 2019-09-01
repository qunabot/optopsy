class PortfolioManager:
    """
    This class groups porfolio properties and provides an 
    interface to access its properties
    """

    def __init__(self, security_manager, transaction_manager):
        self._security_manager = security_manager
        self._transaction_manager = transaction_manager

        self._margin_model = DefaultMarginCallModel()
