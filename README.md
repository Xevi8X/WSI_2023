# WSI_2023

## Obtaining data

Run `data_colector.py` with resources name you want to obtain as consecutive arguments
in order to collect stock data from the past 30 years (or less if there is no data available).
Data is stored as `csv` files in `datasets/` directory.

e.g. ``python .\data_collector.py meta si=f aapl gc=f``.