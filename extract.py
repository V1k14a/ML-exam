# tools/extract.py
import yfinance as yf


def get_stock_price(ticker: str) -> str:
    """Fetch the current stock price for a given ticker symbol using yfinance."""
    try:
        print(f"--- TOOL: Fetching price for {ticker.upper()} via yfinance ---")

        # Fetch the stock data
        stock = yf.Ticker(ticker.upper())

        # Get the real-time quote (regularMarketPrice is the reliable key)
        price = stock.info.get('regularMarketPrice')

        if price:
            # Format to 2 decimal places for a cleaner look
            formatted_price = f"{price:.2f}"
            return f"The current stock price for {ticker.upper()} is ${formatted_price}"
        else:
            # Fallback if the specific key is missing (e.g., if the ticker is invalid)
            return f"Tool failed: Could not find price data for {ticker.upper()}. Ticker may be incorrect."

    except Exception as e:
        return f"ERROR fetching price: An error occurred while using yfinance: {e}"