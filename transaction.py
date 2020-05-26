class Transaction():
    def __init__(self, coins, receiver, previous_transaction_hash=None, type="transfer"):
        self.coins = coins
        self.previous_transaction_hash = previous_transaction_hash
        self.receiver = receiver
        self.type = type

    def sign_transaction(self, signature):
        self.signature = signature

    def __str__(self):
        return f'\nTransaction ID: {self.receiver.__hash__()} \t Previous Transaction hash: {self.previous_transaction_hash}\nAmount: {len(self.coins)} \t Type: {self.type}\n\nCoins: {"".join(map(str, self.coins))}\n---------------------------'
