# this github file shows pep8 changes i forgot to document. this is an old version. changes have been made since.

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


# makes function to clear screen
def clear():
    """Clear the screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def flight_info(dest, tomorrow):
    """Get the flight info about flight from flights."""
    # get end flight letter
    d = dest.lower()
    dl = d[:1]

    # set amount of seats and price
    cost = flights[dl]['cost']
    seats = flights[dl]['seats']

    # apply discount
    if tomorrow is True:
        off = 35/100*cost
        costn = cost - off
    else:
        costn = cost

    # fill n seats
    randn = random.randint(5, seats-2)
    seats -= randn

    # return data
    return [round(costn, 2), seats, cost]


def make_email(dest, tomorrow, name):
    """Make the email."""
    clear()

    # gets items from flight info
    items = flight_info(dest, tomorrow)

    # set variables used for the email from items from flight info
    cost = items[0]
    seats = items[1]
    oldcost = items[2]

    # write email
    dear = f'Dear {name.capitalize()},'
    bodytmr = (f'Flights to {dest.capitalize()} are usually {oldcost},'
               f'but flying with us tomorrow they are ${cost}!')
    body = (f'Flights to {dest.capitalize()} start at around ${cost}, '
            f'but flying with us tomorrow you can expect 35% off.')
    end = f'There are only {seats} more tickets left, so dont miss out!'

    # display email
    print(dear)
    if tomorrow:
        print(bodytmr)
    else:
        print(body)
    print(end)


def gather_data():
    """Gather data. takes in all data stated at top."""
    # input name
    while True:
        name = input("Please enter your name: ")
        if name.isalpha():
            break
        clear()
    clear()

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
    make_email(dest, tomorrow, name)


gather_data()
