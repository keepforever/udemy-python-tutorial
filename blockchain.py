# Instantiate blockchain global vars/components
MINING_REWARD = 10
genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Max'
#python understands participants to be of type SET
participants = {'Max', 'Satan', 'Jesus'}

# Function to get last blockchain value
def hash_block(block):
    """ performs hash function and returns a string """
    return '-'.join([str(block[key]) for key in block])

def get_balance(participant):
    # Strat, find trans where participant is the 
    # sender and recipient, sum to find total. 
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    # reads: 'We're getting the amount for a given tx for all txs 
    # where participant is the sender. Since the trans are part of the blocks
    # and we have a list of blocks, we go through all the block in the blockchain"
    # we get one array for every block, but only blocks where participant is
    # the sender will have values.  Others will be empty.
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    print('TX_SENDER: ', tx_sender)
    total_amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            total_amount_sent += tx[0]
    # now for what participant sent; (-) trans. 
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    total_amount_recieved = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            total_amount_recieved += tx[0]
    balance = total_amount_recieved - total_amount_sent
    return balance
def get_last_blockchain_value():
    """ BC: Returns last value in the blockchain """
    # check if blockchain is empty
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def verify_transaction(tran):
    """verify sender has enough funds"""
    # transaction = {
    #     'sender': sender,
    #     'recipient': recipient,
    #     'amount': amount
    # }
    sender_balance = get_balance(tran['sender'])
    return sender_balance >= tran['amount']
     


def mine_block():
    """ add all open transactions to the blockchain """
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    # Add transaction where participant who minded gets a reward
    reward_transaction =  {
    # MINING is like the bank, or total coins for distribution.
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    copied_open_transactions = open_transactions[:]
    copied_open_transactions.append(reward_transaction)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': copied_open_transactions
    }
    blockchain.append(block)
    # need to reset open_transactions after mining
    # we return true from this function then use if statement 
    # to reset 
    return True


def add_transaction(recipient, sender=owner, amount=1.0):
    """ adds a transaction to open_transactions List"""
    # create new trans w/local var, type of Dictionary
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(recipient)
        participants.add(sender)
        return True
    return False


def get_transaction_value():
    """Returns input of user"""
    tx_recipient = input('To: ')
    tx_amount = float(input('Amount: '))
    # use a tuple (alt, could use dictionary)
    return (tx_recipient, tx_amount)


def get_user_choice():
    """
    Returns decision of user to add another transaction or print 
    the blockchain values.
    """
    return input("Enter Your Choice: ")


def print_blockchain_elements():
    # bring for loop inside while loop
    for block in blockchain:
        print('block[index] = ', block['index'])
        print(block)
def print_participants():
    print("Participants:")
    for participant in participants:
        print(participant)


def verify_chain():
    """ compare stored hash in given block with recalculated hash 
    of the previous block"""
    for (index, block) in enumerate(blockchain):
        # print("block['previous_hash']", '\n', block['previous_hash'],'\n')
        # print("hash_block(blockchain[index - 1])", '\n', hash_block(blockchain[index - 1]))
        if index == 0:
            # skip over genesis_block
            # print('skipped genisis block')
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            # blockchain has been corrupted
            # print('xxx index', index)
            return False
        # no failures, blockchain integrity confirmed
    return True


# Using waiting_for_input to control the while loop as alt to 'break'
waiting_for_input = True
while waiting_for_input:
    print("Please choose: ")
    print("   1: Add Transaction")
    print("   2: Mine a new block")
    print("   3: Output the blockchain blocks")
    print("   4: Print participants")
    print("   h: Manipulate blockchain")
    print("   q: Quit")
    user_choice = get_user_choice()
    if user_choice == '1':
        # recall get_transaction_value returns a TUPLE
        tx_data = get_transaction_value()
        # use TUPLE unpacking(similar to js destructuring)
        # note that the order matters, first to first
        recipient, amount = tx_data
        if add_transaction(recipient, amount=amount):
            print('SUCCESS: Transaction added!')
        else: 
            print('FAILED: Insufficient funds!')
    elif user_choice == '2':
        if mine_block():
            print("resetting open_transactios")
            open_transactions = []
            print('OPEN TRANS: ', open_transactions)
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print_participants()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{
                    'sender': 'Satan',
                    'recipient': 'Brian',
                    'amount': 6.66
                }]
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print("Invalid choice!")
    if not verify_chain():
        print("WARNING: Blockchain INVALID!")
        break
    print('GET BALANCE OF MAX', get_balance('Max'))
else:
    print("User left.")
print("Done!")
