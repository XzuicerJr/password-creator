import random
import string
import os
import time
from datetime import datetime

def clear_terminal():
    if os.name == "posix":
        os.system ("clear")
    else:
        os.system ("cls")
    
def delay(num):
    time.sleep(num)

def password_generator():
    upper = list(string.ascii_uppercase)
    lower = list(string.ascii_lowercase)
    symbols = list(string.punctuation)
    numbers = list(string.digits)

    characters_list = upper + lower + symbols + numbers

    password = []

    for i in range(15):
        character_random = random.choice(characters_list)
        password.append(character_random)

    password = "".join(password)
    return password

def read_file():
    file = open("password.txt","r") 
    data = file.readlines()
    return data

def gen_date():
    now = datetime.now()
    current_date = now.strftime("%B %d, %Y | %H:%M:%S")
    date = "\n    Creation date:" + current_date
    return date

def save_password():
    clear_terminal()
    file = open("password.txt","a")

    if len(read_file()) > 0:
        file.write("\n")
    else:
        file.write("PASSWORD GENERATOR\n")

    print("Please, choise a name for this password:")
    pass_name = input(">> ")
    clear_terminal()
    if len(pass_name) == 0:
        pass_name = "untitled"
    file.write("\nName: " + pass_name + "\n")
    file.write("Pass: " + password_generator() +"\n")
    file.write(gen_date())
    file.write("\n------------------------------------------")
    file.close()

def run():
    clear_terminal()

    print("WELCOME TO THE PASSWORD GENERETOR\n")
    while True:
        password = password_generator()
        print(f"suggested password: {password} \n")
        print("Do you want to change this password? Y/N")
        change = input(">> ")
        clear_terminal()
        if change.lower() == "y":
            print("generating a new password...")
            delay(2)
            clear_terminal()

        elif change.lower() == "n":
            while change:
                print("Save this password? Y/N")
                save = input(">> ")
                clear_terminal()

                if save.lower() == "y":
                    print("Saving password...")
                    delay(2)
                    save_password()
                    print("Password saved!\n")
                    print("Was added in the file \"password.txt\"")
                    print("Check the program folder")
                    delay(4)
                    clear_terminal()
                    while save:
                        print("Do you want to generate another password? Y/N")
                        gen = input(">> ")
                        clear_terminal()

                        if gen.lower() == "y":
                            print("generating a new password...")
                            delay(2)
                            change = False
                            clear_terminal()
                            break

                        elif gen.lower() == "n":
                            print("Come back soon...")
                            delay(2)
                            clear_terminal()
                            exit()

                        else:
                            print("Incorrect Value! Enter \'Y\' or \'N\'...\n")

                elif save.lower() == "n":
                    print("Come back soon...")
                    delay(2)
                    clear_terminal()
                    exit()

                else:
                    print("Incorrect Value! Enter \'Y\' or \'N\'...\n")

        else:
            print("Incorrect Value! Enter \'Y\' or \'N\'...\n")

if __name__ == "__main__":
    run()