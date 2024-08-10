import random
import time
import string

# set special string
start = time.perf_counter()
special_chars = '!@#$%^&*()_+{}|:"<>?'
try:
    cont = int(input("enter length of password: "))
    if cont <= 8:
        print(f'{cont} is too short \n')
        raise ValueError("a password that is less than 8")

    all_chars = string.ascii_letters + string.digits + special_chars
    # set empty list
    password = []
    created_passwords = []
    for i in range(cont):
        password.append(random.choice(all_chars))
        print(password)
        # combine the list into a string
        final = ''.join(password)
    # create file to store password
    with open("saved.txt", 'a') as file:
        created_passwords.append(final)
        for into in created_passwords:
            file.write(into + '\n')
            print(created_passwords)
except Exception as strin:
    print(f'you used a {strin}')
except FileNotFoundError as found:
    print(f'can not find file{found}')

# calculates the average runtime of the program
finish = time.perf_counter()
print(f'it took {round(finish - start, 2)} seconds')
