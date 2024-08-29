import requests
import sys
import json

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument!")
  #  elif not isinstance(sys.argv[1], float):
   #     sys.exit("")
    else:
        try:
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            o = response.json()
            amount = float(sys.argv[1]) * o["bpi"]["USD"]["rate_float"]
            print(f"${amount:,.4f}")

        except requests.RequestException:
            pass
except ValueError:
    sys.exit("Command-line argument is not a number")