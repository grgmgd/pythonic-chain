class Transaction():
    def __init__(self, coins, receiver, used_coins=[], previous_transaction_hash=None, type="transfer"):
        self.coins = coins
        self.previous_transaction_hash = previous_transaction_hash
        self.receiver = receiver
        self.type = type
        self.used_coins = []
        self.id = self.__str__().__hash__()

    def sign_transaction(self, signature):
        self.signature = signature

    def __str__(self):
        return f'\nPrevious Transaction hash: {self.previous_transaction_hash}\nAmount: {len(self.coins)} \t Type: {self.type}\n\nCoins: {"".join(map(str, self.coins))}\n{"="*80}'
