# Passphrase Word Count Program
def get_started():  # Function that prompts user for input
    print("")  # Augments user visibility, asthetics
    print("   --- \"0\" to return to previous menu ---")  # User Manual


def Passphrase_Accuracy_Counter():
    get_started()
    pwd = input(" Enter Passphrase $: ")  # Prompt for passphrase
    x = ''
    while pwd != "0":  # Initialize Loop with option to quit

        print(" pwd      : ", pwd)  # Prints pwd
        print(" length   : ", len(pwd))  # Prints pwd length

        if x == '':  # sets initial standard for passphrase and checks input for match
            # usefull for typing practice of passphrase to improve comfortand accuracy
            print(' identical:  TRUE')
            x = pwd
        elif x == pwd:
            print(' identical:  TRUE')
        else:
            print(' identical:  FALSE')

        get_started()
        pwd = input(" Enter Passphrase $: ")  # Prompt for passphrase
