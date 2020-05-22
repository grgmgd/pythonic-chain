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

    def append_block(self, block):
        str(block)
        # self.chain.append(block)
        pass


class Block():
    def __init__(self, previous_hash, transactions):
        self.previous_hash = previous_hash
        self.transactions = transactions

    def __str__(self):
        print(self)
        return "foo"
