class Transaction():
    def __init__(self, amount, receiver, previous_transaction_hash=None, type="transfer"):
        self.previous_transaction_hash = previous_transaction_hash
        self.amount = amount
        self.receiver = receiver
        self.type = type

    def sign_transaction(self, signature):
        self.signature = signature

    def __str__(self):
        return f'\nTransaction ID: {self.receiver} \t Previous Transaction hash: {self.previous_transaction_hash}\nAmount: {self.amount} \t Type: {self.type}\n---------------------------'
