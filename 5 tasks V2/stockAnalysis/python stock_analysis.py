
import yfinance as yf
import matplotlib.pyplot as plt

# Download stock data
stock_data = yf.download('AAPL', start='2020-01-01', end='2023-01-01')

# Calculate Moving Averages
stock_data['SMA_50'] = stock_data['Close'].rolling(window=50).mean()
stock_data['SMA_200'] = stock_data['Close'].rolling(window=200).mean()

# Plot stock price and moving averages
plt.figure(figsize=(10,6))
plt.plot(stock_data['Close'], label='Close Price', color='blue')
plt.plot(stock_data['SMA_50'], label='50-Day SMA', color='orange')
plt.plot(stock_data['SMA_200'], label='200-Day SMA', color='green')
plt.title('Apple Stock Price with Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()

# Save the figure as a PNG file
plt.savefig('apple_stock_analysis.png')

# Show the plot
plt.show()
