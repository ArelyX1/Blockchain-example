from web3 import Web3
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
tx = {
    'to': '0xC37822E552f9C86232AFaec369973D4b796C84d3',
    'value': Web3.toWei(100, 'ether'),
    'gas': 21000,
    'gasPrice': Web3.toWei(1, 'gwei'),
    'nonce': w3.eth.getTransactionCount('0xf39fd6e51aad88f6f4ce6ab8827279cfffb92266'),
    'chainId': 1337
}
signed_tx = w3.eth.account.signTransaction(tx, private_key)
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(f"Transacción enviada: {tx_hash.hex()}")
