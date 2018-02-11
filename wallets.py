#!usr/bin/python
import time
from coinbase.wallet.client import Client

# Input API info
client = Client('API_KEY','API_SECRET')

wallets = client.get_accounts()

for account in wallets.data:
    balance = account.balance
    print "%s: %s %s" % (account.name, balance.amount, balance.currency)
