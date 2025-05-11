"""
This script will take in the users name, destination,.

and whether or not they will be flying tomorrow

It will then make a email based off of that

"""
import os
import random

flights = {
    'a': {'cost': 100, 'seats': 44},
    'r': {'cost': 90, 'seats': 60},
    'w': {'cost': 110, 'seats': 77}
}

locations = ['wellington', 'rotorua', 'auckland']


def clear():
    """Clear the screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def flight_number(dest):
    """Make flight number (e.g haw182)."""
    # get number
    nums = random.randint(100, 500)

    # get string
    letters = 'ha' + dest[:1]

    # make number
    number = letters + str(nums)

    return number


def flight_info(dest, tomorrow):
    """Get the flight info about flight from flights."""
    # get end flight letter
    d = dest.lower()
    dl = d[:1]

    # set amount of seats and price
    cost = flights[dl]['cost']
    seats = flights[dl]['seats']
    
    # fill n seats
    randn = random.randint(5, seats-2)
    occupied = seats - randn
    
    # get % of seats taken
    sp = occupied/seats*100
    if sp > 45:
        sp = 45 # cap at 45%
    sp = round(sp, 2)

    # apply discount
    if tomorrow:
        off = sp/100*cost
        costn = cost - off
    else:
        costn = cost

    # return data
    return [round(costn, 2), occupied, cost]


def make_email(dest, tomorrow, name):
    """Make the email."""
    clear()

    # gets items from flight info
    items = flight_info(dest, tomorrow)

    # set variables used for the email from items from flight info
    cost = items[0]
    seats = items[1]
    oldcost = items[2]
    
    # add a 0 to the end of cost if decimal place present
    if '.' in str(cost)[-2:]:
        cost = str(cost) + '0'

    # get flight number
    flightn = flight_number(dest.lower())

    # write email
    dear = f'Dear {name},'
    bodytmr = (f'Flights to {dest} on flight {flightn} are usually '
               f'{oldcost}, but flying with us tomorrow they are ${cost}!')
    body = (f'Flights to {dest} on flight {flightn} start at around ${cost}, '
            f'but flying with us tomorrow you can expect 35% off.')
    end = f'There are only {seats} more tickets left, so dont miss out!'

    # display email
    print(dear)
    if tomorrow:
        print(bodytmr)
    else:
        print(body)
    print(end)


def by_dest():
    """Gather data. takes in all data stated at top."""
    # welcome user and get destination
    while True:
        print(f'Welcome, {name.capitalize()}! ')
        print('We can fly you from Hamilton out to\nAuckland,\nRotorua,'
              '\nOr Wellington\n')

        dest = input('Where would you like to fly to? ')
        if dest.lower() in locations:
            break

        clear()

    # tomorrow?
    while True:
        tomorrow = input('Are you planning on flying today? (y or n) ')
        if 'y' in tomorrow.lower():
            tomorrow = True
            break
        elif 'n' in tomorrow.lower():
            tomorrow = False
            break

        clear()

    # get info
    make_email(dest.capitalize(), tomorrow, name.capitalize())

def greet():
    
    # get name
    while True:
        name = input("Please enter your name: ")
        clear()
        if name.isalpha() and len(name) > 1:
            break
    
    # inform
    print('Welcome to Waikato Air Email Generator.\nThis program will make \nan'
          ' email template for your flight.\nPlease select an option:\n')

    while True:
        # give info
        print('[1] Enter flight information\n[2] Find flight by destination'
          '\n[3] Print email')
          
        # check if valid
        choice = int(input('Please select 1, 2, or 3: '))
        clear()
        if choice != 1 and choice != 2 and choice != 3:
            pass
        else:
            break
        
    if choice == 1:
        ...
    if choice == 2:
        by_dest(name)

greet()
