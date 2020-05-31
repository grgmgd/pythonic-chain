import uuid


class ScroogeCoin():
    def __init__(self, wallet_id):
        self.wallet_id = wallet_id
        self.id = uuid.uuid1()

    def __str__(self):
        return f'\nWallet ID: {self.wallet_id.__hash__()}\tcoin id: {self.id}'
