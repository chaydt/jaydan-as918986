"""
This script will take in the users name, destination,.

and whether or not they will be flying tomorrow

It will then make a email based off of that

"""
import os
import random
from time import sleep

flights = {
    'a': {'cost': 100, 'seats': 44},
    'r': {'cost': 90, 'seats': 60},
    'w': {'cost': 110, 'seats': 77}
}

userInfo = {
    'name': '',
    'dest': '',
    'tomorrow': '',
    'discount': 0
}

locations = ['wellington', 'rotorua', 'auckland']

global_email = ''  # works better than returning it through defs


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
        sp = 45  # cap at 45%
    sp = round(sp, 2)
    userInfo['discount'] = sp

    # apply discount
    if tomorrow:
        off = sp/100*cost
        costn = cost - off
    else:
        costn = cost

    # return data
    return [round(costn, 2), occupied, cost, seats, sp]


def make_email(occupied=-1, display=1):
    """Make the email."""
    global global_email
    clear()

    # set variables from userInfo
    name = userInfo['name']
    dest = userInfo['dest']
    tomorrow = userInfo['tomorrow']
    discount = userInfo["discount"]

    # gets items from flight info
    items = flight_info(dest, tomorrow)

    # set variables used for the email from items from flight info
    cost = items[0]
    seats = items[1]
    oldcost = items[2]
    fullseats = items[3]

    if occupied > 0:
        seats = fullseats - occupied

    # add a 0 to the end of cost if decimal place present
    if '.' in str(cost)[-2:]:
        cost = str(cost) + '0'

    # get flight number
    flightn = flight_number(dest.lower())

    # write email
    dear = f'Dear {name},'
    bodytmr = (f'Flights to {dest} on flight {flightn} are usually '
               f'${oldcost}, but because you are flying with us tomorrow,'
               f' they are ${cost}!')
    body = (f'Flights to {dest} on flight {flightn} start at around ${cost}, '
            f'but flying with us tomorrow you can expect {discount}% off.')
    end = f'There are only {seats} more tickets left, so dont miss out!'
    email = ''

    # display email
    if display == 1:
        print(dear)
        if tomorrow:
            print(bodytmr)
        else:
            print(body)
        print(end)
    else:
        email += dear+'\n'
        if tomorrow:
            email += bodytmr+'\n'
        else:
            email += body+'\n'
        email += end

    global_email = email
    print('\nEmail Made!')


def by_dest():
    """Gather data. takes in all data stated at top."""
    # get destination
    while True:
        print('We can fly you from Hamilton out to\nAuckland,\nRotorua,'
              '\nOr Wellington\n')

        dest = input('Where would you like to fly to? ')
        if dest.lower() in locations:
            break

        clear()
    userInfo['dest'] = dest.capitalize()

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
    userInfo['tomorrow'] = tomorrow

    # make email
    make_email(display=2)


def get_info():
    """Get the information for flight to be made into email."""
    while True:
        print('The destinations we have on offer are:\nAuckland,\nRotorua,'
              '\nOr Wellington\n')

        dest = input('Where would you like to fly to? ')
        dest = dest.lower()
        if dest in locations:
            break

        clear()
    userInfo['dest'] = dest.capitalize()

    # seats/occupied seats and cost
    seats = flights[dest[:1]]['seats']
    cost = flights[dest[:1]]['cost']

    while True:
        try:
            taken = int(input('How many seats taken up?'
                              f'(must be lower than {seats}) '))
        except:
            print('must be a number!')
        if taken >= seats:
            print(f'Must be lower than {seats}')
            sleep(2)
        else:
            break
        clear()

    # tomorrow?
    while True:
        tomorrow = input('Will the flight be today? (y or n) ')
        if 'y' in tomorrow.lower():
            tomorrow = True
            userInfo['tomorrow'] = True
            break
        elif 'n' in tomorrow.lower():
            tomorrow = False
            userInfo['tomorrow'] = False
            break
        clear()

    # get % of taken seats
    sp = taken/seats*100
    if sp > 45:
        sp = 45  # cap at 45%
    sp = round(sp, 2)
    userInfo['discount'] = sp

    # apply discount
    if tomorrow:
        off = sp/100*cost
        costn = cost - off
    else:
        costn = cost

    make_email(occupied=taken, display=2)


def greet(ask=True, informed=False):
    """Greet user and present options"""
    # get name
    if ask:
        while True:
            name = input("Please enter your name: ")
            clear()
            if name.isalpha() and len(name) > 1 and len(name) <= 10:
                userInfo['name'] = name.capitalize()
                break
    else:
        name = userInfo['name']
    while True:
        # inform
        if not informed:
            print('Welcome to Waikato Air Email Generator.'
                  '\nThis program will make \nan'
                  ' email template for your flight.'
                  '\nPlease select an option:\n')
        informed = True
        while True:
            # give info
            print('[1] Enter flight information\n[2] Find flight by destination'
                  '\n[3] Print email \n[4] Quit program')

            # check if valid
            try:
                choice = int(input('Please select 1, 2, 3, or 4: '))

                if choice != 1 and choice != 2 and choice != 3 and choice != 4:
                    clear()
                    pass
                else:
                    break
            except:
                clear()
                pass

        # let user choose
        if choice == 1:
            clear()
            get_info()
        if choice == 2:
            clear()
            by_dest()
        if choice == 4:
            break
        if choice == 3 and global_email != '':
            clear()
            print(global_email, '\n')
            print(userInfo)
            break
        elif global_email == '':
            print('Please enter flight information first!')
            sleep(1)
            clear()
            greet(ask=False)


greet()
