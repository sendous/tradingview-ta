import requests
import csv

exchange_id = "binance"
target_currency = "usdt"

url = f"https://api.coingecko.com/api/v3/exchanges/{exchange_id}/tickers?target_currency={target_currency}"

response = requests.get(url)

if response.status_code == 200:
    tickers = response.json()["tickers"]
    coins = set()
    for ticker in tickers:
        coins.add(ticker["base"].upper() + 'USDT')
    print(coins)

    # Write coins set to a CSV file
    with open('coins.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Coins"])
        for coin in coins:
            writer.writerow([coin])

else:
    print("Error:", response.status_code)
