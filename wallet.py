from utils import generate_keys, signer, object_hash
from transaction import Transaction


class Wallet():
    """ A ScroogeCoin user
    """

    def __init__(self):
        self.__private_key, self.public_key = generate_keys()
        self.id = self.public_key

    def create_transaction(self, amount, receiver, scrooge):
        owned_coins = self.get_balance(scrooge.blockchain)
        if len(owned_coins) < amount:
            print("Can't make transaction, not enough balance")
            return

        transfer_coins = owned_coins[:amount]
        transaction = Transaction(transfer_coins, amount, receiver)
        hashed_transaction = object_hash(transaction)
        signature = signer(self.__private_key, hashed_transaction)
        transaction.sign_transaction(signature)

        scrooge.handle_transaction(transaction, self.public_key)

    def get_balance(self, blockchain):
        coins = []
        for block in blockchain.chain:
            for transaction in block.transactions:
                if(transaction.receiver == self.id):
                    coins = [*coins, *transaction.coins]
        return coins
