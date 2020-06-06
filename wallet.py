from utils import generate_keys, signer, object_hash, printer
from transaction import Transaction
from bcolors import bcolors

BALANCE_ERROR_MESSAGE = "Can't make transaction, not enough balance"


class Wallet():
    """ A ScroogeCoin user
    """

    def __init__(self):
        self.__private_key, self.public_key = generate_keys()
        self.id = self.public_key

    def create_transaction(self, amount, receiver, scrooge):
        owned_coins = self.get_balance(scrooge.blockchain)
        transfer_coins = owned_coins[:amount]

        if len(owned_coins) < amount:
            transaction = Transaction(
                transfer_coins, receiver.public_key)
            printer(bcolors.FAIL, bcolors.BOLD, bcolors.UNDERLINE,
                    BALANCE_ERROR_MESSAGE, bcolors.ENDC, bcolors.ENDC, bcolors.ENDC)
            printer(bcolors.FAIL, transaction, bcolors.ENDC)

        transfer_coins = owned_coins[:amount]
        transaction = Transaction(transfer_coins, receiver.public_key)
        hashed_transaction = object_hash(transaction)
        signature = signer(self.__private_key, hashed_transaction)
        transaction.sign_transaction(signature)

        scrooge.handle_transaction(transaction, self.public_key)

    def get_balance(self, blockchain):
        coins = []
        for block in blockchain.chain:
            for transaction in block.transactions:
                for coin in transaction.coins:
                    if(coin.wallet_id == self.id):
                        coins.append(coin)
                for coin in transaction.used_coins:
                    if(coin.wallet_id == self.id):
                        coins.remove(coin)
        return coins
