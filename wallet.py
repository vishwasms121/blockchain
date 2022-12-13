# we're going to do some deterministic wallet stuff here

# requirements
# pip install hdwallet
# https://github.com/meherett/python-hdwallet
from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet
from hdwallet.derivations import BIP44Derivation
from hdwallet.utils import generate_mnemonic
from typing import Optional
from decouple import config

mnemonic = config('SEED_PHRASE')

myWallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency=EthereumMainnet)

myWallet.from_mnemonic(
    mnemonic=mnemonic, language="english", passphrase=""
)

myWallet.clean_derivation()

path = "m/44'/60'/0'/0/0"

myWallet.from_path(path=path)

print("wallet address = " + myWallet.address())
print("private key:  " + myWallet.private_key())



