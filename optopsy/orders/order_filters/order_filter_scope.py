import datetime


class OrderFilterScope:
    def __init__(self):
        self.custom_funcs = []
        self.settings = {}

    def custom_filter(self, func):
        self.custom_funcs.append(func)
        return self

    def at_the_money(self):
        self.settings["atm"] = True
        return self

    def days_to_expiration(self, min_days, max_days):
        self.settings["dte"] = (min_days, max_days)
        return self

    def delta(self, min_delta, max_delta):
        self.settings["delta"] = (min_delta, max_delta)
        return self

    def delta_abs(self, min_delta, max_delta):
        self.settings["delta_abs"] = (min_delta, max_delta)
        return self

    def expiration_date(self, year, month, day=1):
        self.settings["exp_date"] = datetime.datetime(year, month, day)
        return self

    def gamma(self, min_gamma, max_gamma):
        self.settings["gamma"] = (min_gamma, max_gamma)
        return self

    def gamma_abs(self, min_gamma, max_gamma):
        self.settings["gamma_abs"] = (min_gamma, max_gamma)
        return self

    def implied_volatility(self, min_vol, max_vol):
        self.settings["iv"] = (min_vol, max_vol)
        return self

    def in_the_money_pct(self, min_itm, max_itm):
        self.settings["itm"] = (min_itm, max_itm)
        return self

    def option_series_weekly(self):
        self.settings["series"] = "weekly"
        return self

    def option_series_monthly(self):
        self.settings["series"] = "monthly"
        return self

    def out_of_money_pct(self, min_otm, max_otm):
        self.settings["otm"] = (min_otm, max_otm)
        return self

    def pct_diff_between_strikes(self, min_pct, max_pct):
        self.settings["pct_diff_btw_strikes"] = (min_pct, max_pct)
        return self

    def pct_dist_from_underlying(self, min_dist, max_dist):
        self.settings["pct_dist_from_underlying"] = (min_dist, max_dist)
        return self

    def risk_reward(self, min_reward, max_reward):
        self.settings["risk_rewared"] = (min_reward, max_reward)
        return self

    def theta(self, min_theta, max_theta):
        self.settings["theta"] = (min_theta, max_theta)
        return self

    def theta_abs(self, min_theta, max_theta):
        self.settings["theta_abs"] = (min_theta, max_theta)
        return self

    def vega(self, min_vega, max_vega):
        self.settings["veta"] = (min_vega, max_vega)
        return self

    def vega_abs(self, min_vega, max_vega):
        self.settings["veta_abs"] = (min_vega, max_vega)
        return self
