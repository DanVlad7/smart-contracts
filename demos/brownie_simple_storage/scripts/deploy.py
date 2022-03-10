from asynchat import simple_producer
from brownie import accounts, SimpleStorage, network, config

import os


def delpoy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)

    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_value = simple_storage.retrieve()
    print(updated_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    delpoy_simple_storage()
