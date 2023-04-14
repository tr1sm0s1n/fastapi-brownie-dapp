from brownie import Cert, accounts
from brownie.network import gas_price
from brownie.network.gas.strategies import LinearScalingStrategy
import json

gas_strategy = LinearScalingStrategy("10 gwei", "30 gwei", 1.1)
gas_price(gas_strategy)


def main():
    cert = Cert.deploy({'from': accounts[0], "gas_price": gas_strategy})

    details = {
        "deployer": accounts[0].address,
        "contract": cert.address,
    }

    print(f"Account: {details['deployer']} deployed contract: {details['contract']}")

    json_object = json.dumps(details, indent=2)

    with open("details.json", "w") as outfile:
        outfile.write(json_object)
        print('Details are saved!!')
