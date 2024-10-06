import requests
import sys

if len(sys.argv) < 2:
    print("Missing command-line argument")
    sys.exit(1)

try:
    quantity = float(sys.argv[1])

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = response.json()
    price = response["bpi"]["USD"]["rate_float"]

    usd = quantity * price
    print(f"${usd:,.4f}")

except ValueError:
    print("Command-line argument is not a number ")
    sys.exit(1)
except requests.RequestException:
    ...