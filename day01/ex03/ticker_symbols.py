import sys


def check_dist(comp, stocks, arg):
    for key, value in comp.items():
        if value.lower() == arg.lower():
            print(key, stocks[value])
            return True


def stock_prices():
    if len(sys.argv) != 2:
        return
    arg = sys.argv[1].lower()
    companies = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    stocks = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    if not check_dist(companies, stocks, arg):
        print("Unknown ticker")


if __name__ == '__main__':
    stock_prices()