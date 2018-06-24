# Instantiate blockchain global vars/components
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


def get_last_blockchain_value():
    """ BC: Returns last value in the blockchain """
    # check if blockchain is empty
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def mine_block():
    """ add all open transactions to the blockchain """
    last_block = blockchain[-1]
    # List Comprehension strat to make list by looping thru Keys
    # in the last_block. Note: only possible to join a list of strings.
    hashed_block = hash_block(last_block)
    # Simple hash function
    # for loop of dictionary loops through KEYS.
    # for key in last_block:
    #     value = last_block[key]
    #     hashed_block += str(value)
    # print('HASHED_BLOCK: ', hashed_block)

    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)
    #need to reset open_transactions after mining
    #we return true from this function then use if statement 
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
    open_transactions.append(transaction)
    participants.add(recipient)
    participants.add(sender)


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
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
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
else:
    print("User left.")
print("Done!")
