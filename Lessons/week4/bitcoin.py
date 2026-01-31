import json
import requests
import sys

# User provied command line argument - how many bitcoins we want calculated

if len(sys.argv) != 2:
    sys.exit("Missing command line argument")
else:
    try:
        number_of_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")


key = "a8b66250fa6f19edae1a2608bdd2418b9046edbc6edc14be2f15bdd96687cc8c"

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=" + key)
except requests.RequestException:
    sys.exit("Invalid request")

# print(json.dumps(response.json(), indent=2))

bitcoin_info = response.json()
price = float(bitcoin_info["data"]["priceUsd"]) * number_of_bitcoins

print(f"${price:,.4f}")