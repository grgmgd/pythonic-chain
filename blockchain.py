from utils import object_hash, printer
from bcolors import bcolors


class Blockchain():
    """ Class represents the blockchain using an array 
        of type Block. Each block consists of a number
        of transactions initially = 10
    """

    def __init__(self, blocksize=10):
        """
        Initializes the blockchain

        Parameters
        ----------
        blocksize : int
            Number of transactions inside a block (default is 10)
        """

        self.blocksize = blocksize
        self.chain = []

    def append_block(self, transactions):
        previous_hash = None if len(
            self.chain) == 0 else object_hash(self.chain[-1])
        block = Block(len(self.chain), previous_hash, transactions)
        self.chain.append(block)
        printer(self)

    def __str__(self):
        return f'{"".join(map(str, self.chain))}'


class Block():
    def __init__(self, index, previous_hash, transactions):
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.index = index
        self.id = self.__hash__()

    def sign(self, signature):
        self.signature = signature

    def __str__(self, under_construction=False):
        return f'\n{bcolors.OKBLUE}Block No.: {self.index}\tPrevious block hash: {self.previous_hash} {bcolors.ENDC}\n{bcolors.WARNING if under_construction else ""}{ "".join(map(str, self.transactions)) }{bcolors.ENDC if under_construction else ""}'
