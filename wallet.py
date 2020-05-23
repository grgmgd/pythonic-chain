from utils import generate_keys
from transaction import Transaction


class Wallet():
    """ A ScroogeCoin user
    """

    def __init__(self):
        self.__private_key, self.public_key = generate_keys()
        self.id = self.public_key.__hash__()

    def create_transaction(self, coins, receiver, blockchain):
        balance = self.get_balance(blockchain)
        transaction = Transaction(coins, receiver)
        # signed_transaction =

    def get_balance(self, blockchain):
        balance = 0
        for block in blockchain:
            for transaction in block.transactions:
                if(transaction.receiver == self.public_key):
                    # TODO: append to coins array
                    print("my coins")
        return balance
