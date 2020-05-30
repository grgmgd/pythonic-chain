import keyboard
from scrooge import Scrooge
from wallet import Wallet

if __name__ == '__main__':
    wallets = [Wallet() for _ in range(20)]
    scrooge = Scrooge(wallets)

    for person in range(0, 20, 2):
        wallets[person].create_transaction(10, wallets[person+1], scrooge)

    # while(True):
    #     print("hey there")
    #     if keyboard.is_pressed('space'):
    #         print("saving blockchain...")
    #         print("blockchain saved!")
    #         print("terminating")
    #         break
