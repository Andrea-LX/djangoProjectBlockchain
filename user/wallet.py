from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://ropsten.infura.io/v3/30fe37edd3c1446cbbc390a51d41a2c2"))
account = w3.eth.account.create()
privateKey = account.privateKey.hex()
address = account.address

print(address+' e '+privateKey)