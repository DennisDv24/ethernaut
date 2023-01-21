from brownie import (
    network, accounts, config
)

LOCAL_ENVS = ['development', 'ganache']

def connect_to_challenge():
    network.disconnect()
    network.connect('goerli')

def get_acc(wallet_name = None):
    if network.show_active() in LOCAL_ENVS: 
        return accounts[0]
    if wallet_name:
        return accounts.add(config['wallets'][wallet_name])
    return accounts.add(config['wallets']['from_key'])

