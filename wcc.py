# Passphrase Word Count Program
def get_started():  # Function that prompts user for input
    print("")  # Augments user visibility, asthetics
    print("   --- Type \"q\" to quit program ---")  # User Manual


get_started()
pwd = input("Enter Passphrase: ")  # Prompt for passphrase
x = ''
while pwd != "q":  # Initialize Loop with option to quit

    print("pwd   : ", pwd)  # Prints pwd
    print("length: ", len(pwd))  # Prints pwd length

    if x == '':  # sets initial standard for passphrase and checks input for match
        # usefull for typing practice of passphrase to improve comfortand accuracy
        x = pwd
    elif x == pwd:
        print('TRUE')
    else:
        print('FALSE')

    get_started()
    pwd = input("Enter Passphrase: ")  # Prompt for passphrase
