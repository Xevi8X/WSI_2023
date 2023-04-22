import yfinance as yf
import datetime as dt
import sys


def collect_data(resource_name, period_in_years=30, interval="1d"):
    resource = yf.Ticker(resource_name)
    today = dt.date.today()
    period_in_days = period_in_years * 365
    start = today - dt.timedelta(days=period_in_days)

    historical_data = resource.history(start=start, end=today, interval=interval)

    filename = f"datasets/{resource_name}.csv"
    historical_data.to_csv(filename, mode="w+", columns=['Open', 'High', 'Low', 'Close', 'Volume'])


if __name__ == '__main__':
    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        collect_data(resource_name=arg)

