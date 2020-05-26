from utils import generate_keys, object_hash, signer, verifier
from blockchain import Blockchain
from transaction import Transaction
from scroogecoin import ScroogeCoin


class Scrooge():
    def __init__(self, wallets):
        self.__private_key, self.public_key = generate_keys()
        self.blockchain = Blockchain()
        self.wallets = wallets
        self.transactions_cache = []
        self.genesis()

    def verify_transaction(self, transaction, sender_pk):
        hashed_transaction = object_hash(transaction)
        truthy = verifier(sender_pk, transaction.signature, hashed_transaction)
        return truthy

    def is_double_spending(self, transaction):
        for cached_transaction in self.transactions_cache:
            for cached_coin in cached_transaction.coins:
                for coin in transaction.coins:
                    if(coin.id == cached_coin.id):
                        return True
        return False

    def handle_transaction(self, transaction, sender_pk):
        # TODO: verfiy both signatures and double spending attacks
        # if they both pass append the transaction to the transaction array
        # then to the blockchain once they reach 10 transactions
        verified = self.verify_transaction(transaction, sender_pk)
        double_spending = self.is_double_spending(transaction)
        if not verified or double_spending:
            print(
                "Can't process transaction, wallet not verified or you're trying to double spend")
            return

        self.transactions_cache.append(transaction)
        self.check_for_new_block()

    def create_coins(self, amount, wallet_id):
        return [ScroogeCoin(wallet_id) for _ in range(amount)]

    def genesis(self):
        previous_transaction_hash = None
        for wallet in self.wallets:
            coins = self.create_coins(10, wallet.id)
            transaction = Transaction(
                coins, wallet.id, type="create", previous_transaction_hash=previous_transaction_hash)
            hashed_transaction = object_hash(transaction)
            previous_transaction_hash = hashed_transaction.__hash__()
            signature = signer(self.__private_key, hashed_transaction)
            transaction.sign_transaction(signature)
            self.transactions_cache.append(transaction)
            self.check_for_new_block()

    def check_for_new_block(self):
        if len(self.transactions_cache) == 10:
            self.blockchain.append_block(self.transactions_cache)
            self.transactions_cache = []
