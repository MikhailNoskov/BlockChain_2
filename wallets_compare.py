import requests

API_KEY = "CG-dxxJLw2iMf4pyEjnGuuQLZEn"

# Wallets list
wallets = [
    "Coinbase", "Binance", "Trezor", "Ledger", "Exodus"
]


# Function to compare features of digital wallets
def compare_features(wallets):
    for wallet in wallets:
        url = f"https://pro-api.coingecko.com/api/v3/coins/{wallet.lower()}?localization=en"
        response = requests.get(url)
        print(response.status_code)
        if response.status_code == 200:
            features = response.json()['description']['en']
            print(f"{wallet} features: {features}\n")
        else:
            print(f"Error retrieving {wallet} features")


# Function to rank digital wallets based on user reviews and ratings
def rank_wallets(wallets):
    url = "https://pro-api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page = 10&page = 1&sparkline = false"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rankings = {}
        for wallet in wallets:
            for item in data:
                if wallet.lower() in item['name'].lower():
                    rankings[wallet] = item['market_cap_rank']
        sorted_rankings = sorted(rankings.items(), key=lambda x: x[1])
        print("Digital wallet rankings based on market cap:")
        for rank, wallet in enumerate(sorted_rankings, start=1):
            print(f"{rank}. {wallet[0]}")
    else:
        print("Error retrieving digital wallet rankings")


compare_features(wallets)
rank_wallets(wallets)