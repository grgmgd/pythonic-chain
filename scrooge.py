from utils import generate_keys, object_hash, signer, verifier
from blockchain import Blockchain
from transaction import Transaction


class Scrooge():
    def __init__(self, wallets):
        self.__private_key, self.public_key = generate_keys()
        self.blockchain = Blockchain()
        self.wallets = wallets
        self.genesis()

    def genesis(self):
        transactions = []
        previous_transaction_hash = None
        for wallet in self.wallets:
            transaction = Transaction(
                10, wallet.id, type="create", previous_transaction_hash=previous_transaction_hash)
            hashed_transaction = object_hash(transaction)
            previous_transaction_hash = hashed_transaction.__hash__()
            signature = signer(self.__private_key, hashed_transaction)
            transaction.sign_transaction(signature)
            transactions.append(transaction)

            if(len(transactions) == 10):
                self.blockchain.append_block(transactions)
                transactions = []
