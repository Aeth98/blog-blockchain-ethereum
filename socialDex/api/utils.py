from web3 import Web3

def sendTransaction(message):
    w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/41bba0812b6f48e8aadddf89f5224055'))
    address = '0x7F8eE74e2B83d848e0550669e0b97f4C1b21FedA'
    privateKey = '0xc4bb8b99f73ece1cc75440534e3d33ebb7b6ee2b8b5931191c9cb0d6c2ad9071'
    nonce = w3.eth.getTransactionCount(address)
    gasPrice = w3.eth.gasPrice
    value = w3.toWei(0,'ether')
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