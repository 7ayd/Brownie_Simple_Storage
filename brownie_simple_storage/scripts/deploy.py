from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    # These are all different ways to select the account and pass the private key in. The best one apparently is the config
    account = get_account()
    # account = accounts.load("zayd-code-account")
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # account = accounts.add(config["wallets"]["from_key"])

    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()

    print(stored_value)

    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_store_value = simple_storage.retrieve()
    print(updated_store_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
