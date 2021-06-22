from web3 import Web3
w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/41bba0812b6f48e8aadddf89f5224055'))
account = w3.eth.account.create()
privateKey = account.privateKey.hex()
address = account.address
print (f"indirizzo : {address}\nchiave privata: {privateKey}")
