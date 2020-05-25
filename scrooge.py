from utils import generate_keys, object_hash, signer, verifier
from blockchain import Blockchain
from transaction import Transaction
from scroogecoin import ScroogeCoin


class Scrooge():
    def __init__(self, wallets):
        self.__private_key, self.public_key = generate_keys()
        self.blockchain = Blockchain()
        self.wallets = wallets
        self.genesis()

    def verify_transaction(self, transaction, sender_pk):
        hashed_transaction = object_hash(transaction)
        truthy = verifier(sender_pk, transaction.signature, hashed_transaction)
        return truthy

    def handle_transaction(self, transaction, sender_pk):
        # TODO: verfiy both signatures and double spending attacks
        # if they both pass append the transaction to the transaction array
        # then to the blockchain once they reach 10 transactions
        verified = self.verify_transaction(transaction, sender_pk)
        print(transaction)

    def create_coins(self, amount, wallet_id):
        return [ScroogeCoin(1, wallet_id) for _ in range(amount)]

    def genesis(self):
        transactions = []
        previous_transaction_hash = None
        for wallet in self.wallets:
            coins = self.create_coins(10, wallet.id)
            transaction = Transaction(coins,
                                      10, wallet.id, type="create", previous_transaction_hash=previous_transaction_hash)
            hashed_transaction = object_hash(transaction)
            previous_transaction_hash = hashed_transaction.__hash__()
            signature = signer(self.__private_key, hashed_transaction)
            transaction.sign_transaction(signature)
            transactions.append(transaction)

            if(len(transactions) == 10):
                self.blockchain.append_block(transactions)
                transactions = []
