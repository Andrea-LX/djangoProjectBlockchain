from web3 import Web3


def sendTransaction(message):
    w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/30fe37edd3c1446cbbc390a51d41a2c2'))
    address = '0x6cd5C9D7250Fb60CfA795F1Cc00cD76a0DD483be'
    privateKey = '0xdae662ff16532af2b92789ceb05548e030da967bc0de4fed4d97e8f225d8f80c'
    nonce = w3.eth.getTransactionCount(address)
    gasPrice = w3.eth.gasPrice
    value = w3.toWei(0, 'ether')
    signedTx = w3.eth.account.signTransaction(dict(
        nonce=nonce,
        gasPrice=gasPrice,
        gas=100000,
        to='0x0000000000000000000000000000000000000000',
        value=value,
        data=message.encode('utf-8')
        ), privateKey)
    tx = w3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId = w3.toHex(tx)
    return txId