from brownie import ProxyAdmin, TransparentUpgradeableProxy, Box, BoxV2, Contract
from scripts import helper


def main():
    acc = helper.getAccount()

    proxyAdmin = ProxyAdmin[-1]
    proxy = TransparentUpgradeableProxy[-1]
    boxV2 = BoxV2.deploy({"from": acc})

    upgrade(acc, proxy, boxV2, proxyAdmin)
    boxV2AfterUpgrade = Contract.from_abi("BoxV2", proxy, BoxV2.abi)
    boxV2AfterUpgrade.increase({"from": acc})
    print(f"after upgrade {boxV2AfterUpgrade.getNumber()}")


def upgrade(acc, proxy, newImplementation, proxyAdmin=None, initializer=None, *args):
    if proxyAdmin:
        if initializer:
            encodedFunctionData = helper.encodeFunctionData(initializer, args)
            proxyAdmin.upgradeAndCall(
                proxy, newImplementation, encodedFunctionData, {"from": acc}
            )
        else:
            proxyAdmin.upgrade(proxy, newImplementation, {"from": acc})
    else:
        if initializer:
            encodedFunctionData = helper.encodeFunctionData(initializer, args)
            proxy.upgradeToAndCall(
                newImplementation, encodedFunctionData, {"from": acc}
            )
        else:
            proxy.upgradeTo(newImplementation, {"from": acc})
