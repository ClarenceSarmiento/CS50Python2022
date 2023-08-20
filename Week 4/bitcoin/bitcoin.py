import sys
import requests

def bitcoin_price(quantity):
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        price = response["bpi"]["USD"]["rate_float"]
        result = quantity * price
        return result
    except requests.RequestException:
        return None

def main():
    if len(sys.argv) == 2:
        try:
            quantity = float(sys.argv[1])
            total = bitcoin_price(quantity)
            print(f"${total:,.4f}")
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")

main()