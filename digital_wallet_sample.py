import requests


# Function to check balance of a wallet
def check_balance(address):
    url = f"https://api.blockcypher.com/v1/btc/main/addrs/{address}/balance"
    response = requests.get(url)
    if response.status_code == 200:
        balance = response.json()['balance']
        print(f"Balance of {address}: {balance} satoshis")
    else:
        print("Error checking balance")


def view_history(address):
    url = f"https://api.blockcypher.com/v1/btc/main/addrs/{address}/full"
    response = requests.get(url)
    if response.status_code == 200:
        print('response got')
        history = response.json()['txs']
        for tx in history:
            print(f"Transaction hash: {tx['hash']}")
            print(f"Amount: {tx['total']} satoshis")
            print(f"Confirmations: {tx['confirmations']}\n")
    else:
        print("Error viewing transaction history")


# Function to create multiple addresses within a wallet
def create_address():
    url = "https://api.blockcypher.com/v1/btc/main/addrs"
    response = requests.post(url)
    if response.status_code == 201:
        address = response.json()['address']
        print(f"New address created: {address}")
    else:
        print("Error creating new address")



address = "1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2"
address_2 = '1KJVDY1mvPRU2iEYKJWsn8NMMCn5Bf55Zy'
check_balance(address_2)
view_history(address_2)
# create_address()
