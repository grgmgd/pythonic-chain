# Pythonic chain 🐍⛓️

A python implementation of a modified version of **ScroogeCoin**. Scrooge publishes an append only ledger that is a blockchain. Each block contains 10 transactions verified and appended only by Scrooge.

## Files 🗄️

| File name                            | Description                                                                                                         |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| [**network.py**](network.py)         | Simulation of a network of transactions, initialized to 100 wallets (user) every user has 10 coins in their wallet. |
| [**scrooge.py**](scrooge.py)         | Scrooge entity, initializes the blockchain and the genesis blocks.                                                  |
| [**scroogecoin.py**](scroogecoin.py) | Class implementation of a ScroogeCoin.                                                                              |
| [**blockchain.py**](blockchain.py)   | Contains the blockchain and the block classes.                                                                      |
| [**transaction.py**](transaction.py) | Class implementation of a transaction.                                                                              |
| [**wallet.py**](wallet.py)           | Class implementation of a ScroogeCoin user.                                                                         |

## Running the simulation 🏃‍♂️

**Make sure you're running the network simulation giving root access**

    sudo python network.py

### Alternatively, if you have pipenv

    sudo pipenv install
    sudo pipenv run python network.py

## Generating you're own simulation ⛏️

You need to initialize 2 entities before we can start the simulation
**Initialize a wallet that is a ScroogeCoin user.**
Each wallet initialized has a public and a private key based on DSA

    wallet_a = Wallet()
    wallet_b = Wallet()

**Initialize Scrooge**
Scrooge expects an array of wallets

    scrooge = Scrooge([wallet])

**Generate a Transaction**

    amount = 2
    wallet_a.create_transaction(amount, wallet_b, scrooge)

**Access the blockchain**

    print(scrooge.blockchain)

## Output format 💾

### Transaction

Each transaction is printed as follows; contains the previous transaction hash, the amount of coins to transfer, type of the transaction and the coins.

    Previous Transaction hash: b'\xc6\x03|\xeb\x80\xf4w\x14Z\xd1\xacx_E*_4\xa5;\x01\xe7\x15\x13.\xb0|\x06\xb2^\x8c\x8ci'
    Amount: 2 	 Type: create

    Coins:
    Wallet ID: 8788704057372	coin id: 6a2efc36-a2ff-11ea-9294-89074a3a0714
    Wallet ID: 8788704057372	coin id: 6a2efc37-a2ff-11ea-9294-89074a3a0714

### Block

A block is printed as follows; contains the block number, previous block has and an array of transactions (10) as described above. _This output is limited to one transaction._

    Block No.: 1    Previous block hash: b'\x7f\xfd\xfdz\xa7\xe1\x9b\x0b\xebma\xf6\xe3\xf7\xfdm\x9a\x9c\xe9\x8e_JT(\x8b\xb0kA\xa1\xa16f'

    Previous Transaction hash: b'\xc6\x03|\xeb\x80\xf4w\x14Z\xd1\xacx_E*_4\xa5;\x01\xe7\x15\x13.\xb0|\x06\xb2^\x8c\x8ci'
    Amount: 2 	 Type: create

    Coins:
    Wallet ID: 8788704057372	coin id: 6a2efc36-a2ff-11ea-9294-89074a3a0714
    Wallet ID: 8788704057372	coin id: 6a2efc37-a2ff-11ea-9294-89074a3a0714
    ....

### Blockchain

The blockchain is printed as an array of block as described above.

## Log 📜

If you chose to run the simulation from **network.py** the log of the generated simulation will be saved to **./output/log.txt**. Beware that restarting the simulation clears the log.
