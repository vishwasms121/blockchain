from web3 import Web3
from decouple import config

infuraUrl= config('INFURA_URL')
contractAddress = Web3.toChecksumAddress(config('CONTRACT_ADDRESS'))
ownerAddress = Web3.toChecksumAddress(config('OWNER_ADDRESS'))
privateKey = config('SUPER_SECRET_PRIVATE_KEY')

abi='[{"inputs":[{"internalType":"string","name":"name_","type":"string"},{"internalType":"string","name":"symbol_","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]'

web3 = Web3(Web3.HTTPProvider(infuraUrl))

# gets the balance of the provided account
def balanceOf(account):
   web3 = Web3(Web3.HTTPProvider(infuraUrl))
   res = web3.isConnected()
   if res:
       contract_instance = web3.eth.contract(address=contractAddress,abi=abi)
       bal = contract_instance.functions.balanceOf(account).call()
   return bal

def decimals():
   web3 = Web3(Web3.HTTPProvider(infuraUrl))
   res = web3.isConnected()
   if res:
       contract_instance = web3.eth.contract(address=contractAddress,abi=abi)
       decimals = contract_instance.functions.decimals().call()
   return decimals

def symbol():
   web3 = Web3(Web3.HTTPProvider(infuraUrl))
   res = web3.isConnected()
   if res:
       contract_instance = web3.eth.contract(address=contractAddress,abi=abi)
       symbol = contract_instance.functions.symbol().call()
   return symbol
   
#  check balance function works
bal = balanceOf(ownerAddress)
print("balance of my owner address in " + symbol() + " is: " + str(bal))

# check decimals works
print("number of decimals in my " + symbol() + " token is: " + str(decimals()))

if web3.isConnected():
    print('CONNECTED TO WEB3!!!!')
    contract_instance = web3.eth.contract(address=contractAddress,abi=abi)
    # decimals = 10 ** 18 hard coding!!  NOOOOO
    targetAccount = web3.toChecksumAddress("0xac4FafdA6A3A6B48b4cDC2a896acf8D104C81d6C")
    decimals = 10 ** decimals()
    bal = balanceOf(targetAccount)
    targetBalance = bal / decimals
    transferValue = 1000 * decimals
    if targetBalance >=1000:
        transferValue = 1 * decimals

    print("about to transfer " + str(transferValue/decimals) + " " + symbol() + " to " + targetAccount)
    # create a tx calling the transfer function in my token contract
    nonce = web3.eth.getTransactionCount(ownerAddress)

    transaction = contract_instance.functions.transfer(
       targetAccount, transferValue).buildTransaction({
        'gas': 200000,
        'gasPrice': web3.toWei('100', 'gwei'),
        'from': ownerAddress,
        'nonce': nonce,
        'chainId': 5 #goerli chain id
    })

    #  sign the tx
    signed_tx = web3.eth.account.sign_transaction(transaction, privateKey)

    #  submit the tx
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print('tx hash: ' + tx_hash.hex())

    web3.eth.waitForTransactionReceipt(tx_hash)
    print('tx mined')




