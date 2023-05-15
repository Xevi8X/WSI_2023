import yfinance as yf
import datetime as dt
import sys
import os


def collect_data(resource_name, period_in_years=30, interval="1d"):
    resource = yf.Ticker(resource_name)
    today = dt.date.today()
    period_in_days = period_in_years * 365
    start = today - dt.timedelta(days=period_in_days)

    historical_data = resource.history(start=start, end=today, interval=interval)

    filename = f"datasets/{resource_name}.csv"
    historical_data.to_csv(filename, mode="w+", columns=['Open', 'High', 'Low', 'Close', 'Volume'])

def collect_data2(resource_name, start, end, interval="1d") -> str:
    resource = yf.Ticker(resource_name)

    historical_data = resource.history(start=start, end=end, interval=interval)

    filename = f"./data/{resource_name}_{start}_{end}.csv" 
    historical_data.to_csv(filename, mode="w+", columns=['Open', 'High', 'Low', 'Close', 'Volume'])
    return filename

def collect_data3(resource_name, start, end, interval="1d") -> str:
    resource = yf.Ticker(resource_name)

    historical_data = resource.history(start=start, end=end, interval=interval)

    filename = f"./data/{resource_name}_{start}_{end}.csv" 
    historical_data.to_csv(filename, mode="w+", columns=['Open', 'High', 'Low', 'Close', 'Volume'])
    return filename,historical_data


def prepare_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


if __name__ == '__main__':
    prepare_dir('datasets')
    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        collect_data(resource_name=arg)

