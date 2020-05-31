from bcolors import bcolors
from utils import OUTPUT_PATH
from scrooge import Scrooge
from wallet import Wallet
import keyboard
import random
import time
from os import _exit

NUMBER_OF_WALLETS = 20
MIN_TRANSFET_AMOUNT = 1
MAX_TRANSFER_AMOUNT = 10

if __name__ == '__main__':

    open(OUTPUT_PATH, 'w').close()

    wallets = [Wallet() for _ in range(NUMBER_OF_WALLETS)]
    scrooge = Scrooge(wallets)

    def on_space_press(_):
        print(bcolors.OKGREEN, "Blockchain log saved to:",
              OUTPUT_PATH, bcolors.ENDC)
        print(bcolors.WARNING, "Terminating simulation...", bcolors.ENDC)
        _exit(0)

    keyboard.on_press_key("space", on_space_press)

    while(True):
        user_a = random.randint(0, NUMBER_OF_WALLETS - 1)
        user_b = random.randint(0, NUMBER_OF_WALLETS - 1)
        transfer_amount = random.randint(
            MIN_TRANSFET_AMOUNT, MAX_TRANSFER_AMOUNT)

        wallets[user_a].create_transaction(
            transfer_amount, wallets[user_b], scrooge)
        time.sleep(2)
