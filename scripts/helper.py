from ast import arg
from brownie import (
    accounts,
    network,
    config,
    Contract,
    ProxyAdmin,
    TransparentUpgradeableProxy,
)

import eth_utils


DEV_NETWORK = ["development", "gananche-local"]
MAINNET_FORK = ["mainnet-fork-dev", "mainnet-fork-dev2"]


def getAccount(index=None, networkId=None):
    if network.show_active() in DEV_NETWORK or network.show_active() in MAINNET_FORK:
        if index:
            return accounts[index]
        if networkId:
            return accounts.load(networkId)
        return accounts[0]

    # default
    return accounts.add(config["wallets"]["key"])


def encodeFunctionData(initializer=None, *args):
    if len(args) <= 0 or not initializer:
        return eth_utils.to_bytes(hexstr="0x")
    else:
        return initializer.encode_input(args)
