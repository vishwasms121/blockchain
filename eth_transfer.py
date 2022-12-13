from web3 import Web3
from decouple import config

infuraUrl= config('INFURA_URL')
# contractAddress = Web3.toChecksumAddress(config('CONTRACT_ADDRESS'))
ownerAddress = Web3.toChecksumAddress(config('OWNER_ADDRESS'))
privateKey = config('SUPER_SECRET_PRIVATE_KEY')

abi='[{"inputs":[{"internalType":"string","name":"name_","type":"string"},{"internalType":"string","name":"symbol_","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]'

web3 = Web3(Web3.HTTPProvider(infuraUrl))

if web3.isConnected():
    print('CONNECTED TO WEB3!!!!')
    amountInEther = "0.1"
    # targetAddress = Web3.toChecksumAddress("0xac4FafdA6A3A6B48b4cDC2a896acf8D104C81d6C")
    # targetAccount= Web3.toChecksumAddress("0xC1a7977959992982CbaAc3Cb5df4d97aaB3aCc53")
    targetAccount = Web3.toChecksumAddress("0x9Dc94C63D3e437C4Abff038418230f045f72ad31")

    nonce = web3.eth.getTransactionCount(ownerAddress)
    print("nonce (tx count) is " + str(nonce))

    gasPrice = web3.toWei('100', 'gwei')
    value = web3.toWei(amountInEther, 'ether')

    # build the tx
    tx = {
        'nonce': nonce,
        'to': targetAccount,
        'value': value,
        'gas': 2000000,
        'gasPrice': gasPrice,
        'chainId': 5
    }

    #  sign the tx
    signed_tx = web3.eth.account.sign_transaction(tx, privateKey)

    #  submit the tx
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print('tx hash: ' + tx_hash.hex())

    web3.eth.waitForTransactionReceipt(tx_hash)
    print('tx mined')

 



 

    


