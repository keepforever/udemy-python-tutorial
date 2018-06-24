# Keyword argument example allows us to declair vars in any order
# or ommit and revert to devalut vals.
def keyword_args_example(name, age):
    print("hello " + name + "aged " + age)
# keyword_args_example(age="33", name="Brian")


# Define blockchain variable as an empty list
blockchain = []

# Function to get last blockchain value


def get_last_blockchain_value():
    """ BC: Returns last value in the blockchain """
    #check if blockchain is empty
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
    """ 
    Appends new value to the list of existing values in the blockchain

    Arguments
        tranaction_amount: the amount that should be added.
        last_transaction: the previous blockchain transaction. (default: [1])  
    """
    if last_transaction == None: 
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """
    Returns the input of the user (a new transaction_amount)
    """
    return float(input('Your transaction amount please: '))

def get_user_choice():
    """
    Returns decision of user to add another transaction or print 
    the blockchain values.
    """
    return input("Enter Your Choice: ")

def print_blockchain_elements():
    # bring for loop inside while loop
    for block in blockchain:
        print(block)

def verify_chain():
    """
    checks to make sure the first element of the current block is
    equal to the previous block. 
    """
    #helper vars
    block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else: 
            is_valid = False
            break
    return is_valid
#Using waiting_for_input to control the while loop as alt to 'break'
waiting_for_input = True
while waiting_for_input:
    print("Please choose: ")
    print("   1: Add a transactio value")
    print("   2: Output the blockchain blocks")
    print("   h: Manipulate blockchain")
    print("   q: Quit")
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1: 
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else: 
        print("Invalid choice!")
    if not verify_chain():
        print("Gasp! \nThe blockchain is invalid!")
        break
else: 
    print("User left.")
print("Done!")
        
############### OLD CODE #################
#
# for block in blockchain:
#         if block_index == 0:
#             block_index += 1
#             continue
#             #continue skips to next iteration in for loop
#         elif block[0] == blockchain[block_index - 1]:
#             is_valid = True
#         else:
#             is_valid = False
#             break
#             #increment block_index to check each block
#         block_index += 1    