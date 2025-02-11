import yfinance as yf

class Asset:
    def __init__(self, ticker, sector, asset_class, quantity, purchase_price):
        self.ticker = ticker.upper()
        self.sector = sector
        self.asset_class = asset_class
        self.quantity = quantity
        self.purchase_price = purchase_price

    def get_current_price(self):
        try:
            data = yf.Ticker(self.ticker)
            hist = data.history(period="1d")
            if hist.empty:
                return 0.0
            return hist['Close'].iloc[-1]
        except Exception as e:
            print(f"Error retrieving current price for {self.ticker}: {e}")
            return 0.0

    def get_transaction_value(self):
        return self.quantity * self.purchase_price

    def get_current_value(self):
        return self.quantity * self.get_current_price()

class Portfolio:
    def __init__(self):
        self.assets = []

    def add_asset(self, asset):
        self.assets.append(asset)

    def get_total_portfolio_value(self):
        return sum(asset.get_current_value() for asset in self.assets)

    def get_portfolio_details(self):
        details = []
        for asset in self.assets:
            current_price = asset.get_current_price()
            transaction_value = asset.get_transaction_value()
            current_value = asset.get_current_value()
            details.append([
                asset.ticker,
                asset.sector,
                asset.asset_class,
                asset.quantity,
                asset.purchase_price,
                transaction_value,
                current_value
            ])
        return details

    def get_asset_weights(self):
        total_value = self.get_total_portfolio_value()
        weights = {}
        for asset in self.assets:
            weights[asset.ticker] = (asset.get_current_value() / total_value) if total_value else 0
        return weights

    def get_weights_by_asset_class(self):
        total_value = self.get_total_portfolio_value()
        asset_class_totals = {}
        for asset in self.assets:
            asset_class_totals.setdefault(asset.asset_class, 0)
            asset_class_totals[asset.asset_class] += asset.get_current_value()
        return {k: v / total_value for k, v in asset_class_totals.items()} if total_value else {}

    def get_weights_by_sector(self):
        total_value = self.get_total_portfolio_value()
        sector_totals = {}
        for asset in self.assets:
            sector_totals.setdefault(asset.sector, 0)
            sector_totals[asset.sector] += asset.get_current_value()
        return {k: v / total_value for k, v in sector_totals.items()} if total_value else {}
