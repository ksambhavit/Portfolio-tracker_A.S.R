from model import Asset, Portfolio
from view import CLIView

class PortfolioController:
    def __init__(self):
        self.portfolio = Portfolio()
        self.view = CLIView()

    def add_asset(self):
        self.view.display_message("\nEnter asset details:")
        ticker = input("Ticker (e.g., AAPL): ").strip().upper()
        sector = input("Sector: ").strip()
        asset_class = input("Asset Class: ").strip()
        try:
            quantity = float(input("Quantity: ").strip())
            purchase_price = float(input("Purchase Price: ").strip())
        except ValueError:
            self.view.display_message("Invalid number entered. Please try again.")
            return
        asset = Asset(ticker, sector, asset_class, quantity, purchase_price)
        self.portfolio.add_asset(asset)
        self.view.display_message(f"Asset {ticker} added to portfolio.")

    def view_portfolio(self):
        details = self.portfolio.get_portfolio_details()
        if not details:
            self.view.display_message("No assets in portfolio.")
            return
        self.view.display_portfolio(details)
        total_value = self.portfolio.get_total_portfolio_value()
        self.view.display_message(f"\nTotal Portfolio Value: {total_value:.2f}")

        # Display weights by asset
        weights = self.portfolio.get_asset_weights()
        self.view.display_message("\nAsset Weights:")
        for ticker, weight in weights.items():
            self.view.display_message(f"{ticker}: {weight*100:.2f}%")

        # Displaying by asset class
        weights_class = self.portfolio.get_weights_by_asset_class()
        self.view.display_message("\nWeights by Asset Class:")
        for asset_class, weight in weights_class.items():
            self.view.display_message(f"{asset_class}: {weight*100:.2f}%")

        # Displaying by sector
        weights_sector = self.portfolio.get_weights_by_sector()
        self.view.display_message("\nWeights by Sector:")
        for sector, weight in weights_sector.items():
            self.view.display_message(f"{sector}: {weight*100:.2f}%")

    def show_price_graph(self):
        ticker_input = input("Enter ticker for graph (or comma separated for multiple): ").strip()
        tickers = [t.strip().upper() for t in ticker_input.split(",")]
        if len(tickers) == 1:
            self.view.plot_asset_history(tickers[0])
        else:
            self.view.plot_combined_assets(tickers)

    def run(self):
        while True:
            self.view.display_message("\nPortfolio Tracker Menu:")
            self.view.display_message("1. Add Asset")
            self.view.display_message("2. View Portfolio")
            self.view.display_message("3. Show Price Graph")
            self.view.display_message("4. Exit")
            choice = input("Select an option: ").strip()
            if choice == '1':
                self.add_asset()
            elif choice == '2':
                self.view_portfolio()
            elif choice == '3':
                self.show_price_graph()
            elif choice == '4':
                self.view.display_message("Exiting Portfolio Tracker. Goodbye!")
                break
            else:
                self.view.display_message("Invalid option. Please try again.")


__all__ = ["PortfolioController"]
