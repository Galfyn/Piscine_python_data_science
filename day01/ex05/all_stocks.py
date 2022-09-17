import sys


def print_companies(comp, stocks, word):
    for key, value in comp.items():
        if key.lower() == word.lower():
            print(f"{key} stock price is {stocks[value]}")
            return True
    return False


def print_ticker(comp, word):
    for key, value in comp.items():
        if value == word.upper():
            print(f"{word} is a ticker symbol for {key}")
            return True
    return False


def all_stocks():
    if len(sys.argv) != 2:
        return
    arg = sys.argv[1].replace(' ', '').split(',')
    print(arg)
    if sys.argv[1].find(",,") != -1:
        print('')
        return

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
    for word in arg:
        if not print_companies(companies, stocks, word) and not print_ticker(companies, word):
            print(f"{word} is an unknown company or an unknown ticker symbol")


if __name__ == '__main__':
    all_stocks()
