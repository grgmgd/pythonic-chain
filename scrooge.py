from utils import generate_keys, object_hash, signer, verifier, printer
from blockchain import Blockchain, Block
from transaction import Transaction
from scroogecoin import ScroogeCoin
from bcolors import bcolors


VERIFICATION_ERROR_MESSAGE = "Can't process transaction, wallet not verified or you're trying to double spend"
UNDER_CONSTRUCTION_MESSAGE = "Under constrcution block transaction"


class Scrooge():
    def __init__(self, wallets):
        self.__private_key, self.public_key = generate_keys()
        self.blockchain = Blockchain()
        self.wallets = wallets
        self.transactions_cache = []
        self.last_transaction = None
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

    def before_block_append(self, genesis):
        if not genesis:
            for transaction in self.transactions_cache:
                hashed_transaction = object_hash(self.last_transaction)
                previous_transaction_hash = hashed_transaction
                transaction.previous_transaction_hash = previous_transaction_hash

                transaction.used_coins = [*transaction.coins]
                transaction.coins = self.create_coins(
                    len(transaction.coins), transaction.receiver)
                self.last_transaction = transaction

        self.blockchain.append_block(self.transactions_cache)
        self.after_block_append()

    def after_block_append(self):
        last_block = self.blockchain.chain[-1]
        hashed_block = object_hash(last_block)
        signature = signer(self.__private_key, hashed_block)
        last_block.sign(signature)

    def handle_transaction(self, transaction, sender_pk):
        verified = self.verify_transaction(transaction, sender_pk)
        double_spending = self.is_double_spending(transaction)
        if not verified or double_spending:
            printer(bcolors.FAIL, bcolors.BOLD, bcolors.UNDERLINE,
                    VERIFICATION_ERROR_MESSAGE, bcolors.ENDC, bcolors.ENDC, bcolors.ENDC)
            printer(bcolors.FAIL, transaction, bcolors.ENDC)
            return

        self.transactions_cache.append(transaction)
        temp_block = Block(-1, None, self.transactions_cache)
        printer(bcolors.WARNING, bcolors.BOLD, bcolors.UNDERLINE,
                UNDER_CONSTRUCTION_MESSAGE, bcolors.ENDC, bcolors.ENDC, bcolors.ENDC)
        printer(bcolors.WARNING, temp_block.__str__(True), bcolors.ENDC)
        self.check_for_new_block()

    def create_coins(self, amount, wallet_id):
        coins = []
        for _ in range(amount):
            coin = ScroogeCoin(wallet_id)
            hashed_coin = object_hash(coin)
            signature = signer(self.__private_key, hashed_coin)
            coin.sign(signature)

            coins.append(coin)

        return coins

    def genesis(self):
        previous_transaction_hash = None
        for wallet in self.wallets:
            coins = self.create_coins(10, wallet.id)
            transaction = Transaction(
                coins, wallet.id, type="create", previous_transaction_hash=previous_transaction_hash)
            hashed_transaction = object_hash(transaction)
            previous_transaction_hash = hashed_transaction
            signature = signer(self.__private_key, hashed_transaction)
            transaction.sign_transaction(signature)
            self.transactions_cache.append(transaction)
            self.last_transaction = transaction
            self.check_for_new_block(True)

    def check_for_new_block(self, genesis=False):
        if len(self.transactions_cache) == 10:
            self.before_block_append(genesis)
            self.transactions_cache = []
