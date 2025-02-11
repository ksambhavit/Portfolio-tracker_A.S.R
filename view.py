import matplotlib.pyplot as plt
from tabulate import tabulate
import yfinance as yf

class CLIView:
    def display_message(self, message):
        print(message)

    def display_portfolio(self, portfolio_details):
        headers = [
            "Ticker", "Sector", "Asset Class", "Quantity",
            "Purchase Price", "Transaction Value", "Current Value"
        ]
        print(tabulate(portfolio_details, headers=headers, floatfmt=".2f"))

    def plot_asset_history(self, ticker):
        try:
            data = yf.Ticker(ticker).history(period="1y")
            if data.empty:
                self.display_message(f"No historical data available for {ticker}")
                return
            plt.figure(figsize=(10, 5))
            plt.plot(data.index, data['Close'])
            plt.title(f'Historical Price of {ticker}')
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.grid(True)
            plt.show()
        except Exception as e:
            self.display_message(f"Error plotting data for {ticker}: {e}")

    def plot_combined_assets(self, tickers):
        plt.figure(figsize=(10, 5))
        for ticker in tickers:
            try:
                data = yf.Ticker(ticker).history(period="1y")
                if data.empty:
                    self.display_message(f"No historical data available for {ticker}")
                    continue
                plt.plot(data.index, data['Close'], label=ticker)
            except Exception as e:
                self.display_message(f"Error plotting data for {ticker}: {e}")
        plt.title('Historical Prices Comparison')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid(True)
        plt.show()
