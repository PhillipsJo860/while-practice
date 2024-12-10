# Joshua Phillips
# 12/10/24
# While loops practice
import time

# age2 = age.isdigit()


# Exit Tickets (7-5)
# while True:
#     try:
#         user = input('Please enter your name here(QUIT = stop program here.): ')
#         age = int(input(f'Welcome {user}, Please enter your age: '))
#         print('We will now determin your ticket price...')
#         time.sleep(2)
#         if age < 3:
#             print('Your ticket is free!')
#         elif age > 12:
#             print('Your ticket is will be $15 USD.')
#         elif user == 'QUIT':
#             break
#         else:
#             print('Your ticket will be $10 USD')
#     except ValueError:
#         print('Please only enter a number as your age.')

# Three Exits (7-6)
# Base set of tickets expended
tickets_given = 0 

# Start of while loop
while True:
    # Assistance from Thayer
    try:
        tickets_given += 1
        user = input(f'Please note that you can only have 5 tickets on this account(This is your {tickets_given} ticket). Enter your name here(QUIT = stop program): ')
        age = int(input(f'Welcome {user}, Please enter your age: '))
        print('We will now determin your ticket price...')
        time.sleep(2)
        if age < 3:
            print('Your ticket is free!')
        elif age > 12:
            print('Your ticket is will be $15 USD.')
        # Failsafe
        elif user == 'QUIT':
            break
        # Banned individual
        elif user == 'Lucas' or 'Lucas Brinks':
            print('Banned!!')
            break
        # Max number of tickets
        elif tickets_given > 5:
            print('Sorry max tickets reached.')
            break
        else:
            print('Your ticket will be $10 USD')
    # Still assistance from Thayer
    except ValueError:
        print('Please only enter a number as your age.')