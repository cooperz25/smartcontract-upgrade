from scripts import helper, upgrade
from brownie import ProxyAdmin, TransparentUpgradeableProxy, Box, BoxV2, Contract


def main():
    acc = helper.getAccount()
    deploy(Box, acc)


def deploy(contractTemplate, acc):

    # deploy
    proxyAdmin = ProxyAdmin.deploy({"from": acc})
    box = Box.deploy({"from": acc})
    proxy = TransparentUpgradeableProxy.deploy(
        box, proxyAdmin, helper.encodeFunctionData(), {"from": acc}
    )

    box = Contract.from_abi("Box", proxy, Box.abi)
    box.setNumber(5, {"from": acc}).wait(1)
    print(f"value after set {box.getNumber()}")

    upgrade.main()
