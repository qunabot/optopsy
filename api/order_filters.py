class OrderFilter:
    def init(self, chains):
        self.chains = chains

    def custom_filter(self, func):
        pass

    def at_the_money(self):
        pass

    def days_to_expiration(self, min_days, max_days):
        pass

    def delta(self, min_delta, max_delta):
        pass

    def delta_abs(self, min_delta, max_delta):
        pass

    def expiration_date(self, year, month, day=1):
        pass

    def gamma(self, min_gamma, max_gamma):
        pass

    def gamma_abs(self, min_gamma, max_gamma):
        pass

    def implied_volatility(self, min_vol, max_vol):
        pass

    def in_the_money_pct(self, min_itm, max_itm):
        pass

    def option_series_weekly(self):
        pass

    def option_series_monthly(self):
        pass

    def out_of_money_pct(self, min_otm, max_otm):
        pass

    def pct_diff_between_strikes(self, min_pct, max_pct):
        pass

    def pct_dist_from_underlying(self, min_dist, max_dist):
        pass

    def risk_reward(self, min_reward, max_reward):
        pass

    def theta(self, min_theta, max_theta):
        pass

    def theta_abs(self, min_theta, max_theta):
        pass

    def vega(self, min_theta, max_theta):
        pass

    def vega_abs(self, min_theta, max_theta):
        pass
