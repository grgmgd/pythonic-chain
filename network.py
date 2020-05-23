import keyboard
from scrooge import Scrooge
from wallet import Wallet

if __name__ == '__main__':
    wallets = [Wallet() for _ in range(20)]
    Scrooge(wallets)

    # while(True):
    #     print("hey there")
    #     if keyboard.is_pressed('space'):
    #         print("saving blockchain...")
    #         print("blockchain saved!")
    #         print("terminating")
    #         break
