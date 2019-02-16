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
        c = False
        #ensure_strictness
        if option not in [0, 1, 2, 3, 4]:
            print('User not complying with rules. Exiting.')
            return True
        #decrypt_executable
        run(['openssl', 'des', '-d', '-in', './.ifl/cf', '-out', '.main', '-pass', 'pass:'+pss])
        run(['chmod', '777', '.main'])
        #run_desirable
        if option == 0:
            run(['./.main', '0', pss])
        elif option == 1:
            run(['./.main', '1', pss])
        elif option == 2:
            run(['./.main', '2', pss])
        elif option == 3:
            run(['./.main', '3', pss])
        else:
            c = True
        # remove_decrypted_file
        run(['rm', '-f', '.main'])
        return c
    except Exception():
        print('Problem with executable.')

def main():
    "Main function to get entry pass and check for entry"
    salt = ''   #pre-salt
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
        while True:
            #now_print_the_option_interface
            print_interface(salt)
            #get_options
            try:
                option = int(input("\n   ... "))
            except TypeError():
                print('Error in input. You are not trustable. Exiting...')
                break
            if pursue(option, salt):
                break
        exit(0)


if __name__ == '__main__':
    main()
