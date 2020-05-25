import uuid


class ScroogeCoin():
    def __init__(self, value, wallet_id):
        self.value = value
        self.wallet_id = wallet_id
        self.coin_id = uuid.uuid1()

    def __str__(self):
        return f'\nvalue: {self.value}\tcoin id: {self.coin_id}'
