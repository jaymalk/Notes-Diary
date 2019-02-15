"""
Function for entry to the log files
"""

import hashlib
import getpass
from subprocess import run

def print_interface(pss):
    "Printing the interface display for options (formatted)"
    try:
        run(['openssl', 'des', '-d', '-in', './.ifl/dl', '-out', '.d', '-pass', 'pass:'+pss])
        run(['clear'])
        run(['cat', '.d'])
        run(['rm', '-f', '.d'])
    except Exception():
        print('Problem with display...')

def pursue(option, pss):
    "Pusuing the desired work with the program"
    try:
        #ensure_strictness
        if option not in [0, 1, 2, 3, 4]:
            print('User not complying with rules. Exiting.')
            exit(0)
        #decrypt_executable
        run(['openssl', 'des', '-d', '-in', './.ifl/cf', '-out', '.cf', '-pass', 'pass:'+pss])
        #run_desirable
        if option == 0:
            run(['.cf', '0'])
        elif option == 1:
            run(['.cf', '1'])
        elif option == 2:
            run(['.cf', '2'])
        elif option == 3:
            run(['.cf', '3'])
        else:
            run(['.cf', '4'])
        #remove_decrypted_file
        run(['rm', '-f', '.cf'])
    except Exception():
        print('Problem with executable.')

def main():
    "Main function to get entry pass and check for entry"
    salt = ''   #pre-salt
    # initial salt just to test functioning
    # salt = 'd02c4c4cde7ae76252540d116a40f23af97c5d29941bfb1b2fdab0874906ab82b8a9f715dbb64fd5c56e7783c6820a6135d6d33467aae9a2e3dccb4b6b0278788cbad96aced40b3838dd9f07f6ef577230056e1cab7a61d256fc8edd970d14f5f52b5e449a2303c031a0c3a1109360bfbb3aec0fdcdbc2974890f805c585d43224d27c169c2c881eb09a065116f2aa5cc785e1ed2950e3e36b1e2ca01f299a54'
    #salt_creation
    for i in range(10):
        #new_string_at_each_step
        pswd = getpass.getpass(prompt="Enter salt no. "+str(i)+" : ", stream=None)
        if pswd == 'restart':
            main()
        elif pswd == 'exit':
            exit(0)
        #adding_value_to_hash
        salt += hashlib.md5(pswd.encode('UTF-8')).hexdigest()
    #getting_final_password
    pswd = getpass.getpass(prompt='Enter Password : ', stream=None)
    #hashing_to_get_entry
    pswd += salt
    entry = hashlib.md5(pswd.encode('UTF-8')).hexdigest()
    #confirming password
    if entry == '0cc4e27f1c3796abab8344f964fbb132':
        #password_matches : it_is_rajbir_malik
        print('Welcome Rajbir\nStarting the reading process.\n')
        #now_print_the_option_interface
        print_interface(salt)
        #get_options
        try:
            option = int(input("\n   ... "))
        except Exception():
            print('Error in input. You are not trustable. Exiting...')
            exit(0)
        pursue(option, salt)
        exit(0)


if __name__ == '__main__':
    main()
