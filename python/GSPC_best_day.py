import yfinance as yf
from datetime import datetime

start_date = datetime(datetime.now().year, 1, 1).strftime('%Y-%m-%d')
end_date = datetime.now().strftime('%Y-%m-%d')

sp500_data = yf.download('^GSPC', start=start_date, end=end_date)

max_close = sp500_data['Close'].max()
max_close_date = sp500_data['Close'].idxmax()

print(f"The highest closing price for the S&P 500 this year was ${max_close:.2f} on {max_close_date.strftime('%Y-%m-%d')}")
