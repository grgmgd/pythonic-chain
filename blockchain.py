from utils import object_hash


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
        print(block)

    def str(self):
        return "blockchain"


class Block():
    def __init__(self, index, previous_hash, transactions):
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.index = index

    def __str__(self):
        return f'Block No.: {self.index}\tPrevious block hash: {self.previous_hash} \n{ "".join(map(str, self.transactions)) } '
