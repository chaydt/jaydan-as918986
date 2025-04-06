import os
import random
"""
This script will take in the users name, destination, 
and whether or not they will be flying tomorrow

It will then make a email based off of that

"""
flights = {
    'a':{'cost':100, 'seats':44},
    'r':{'cost':90, 'seats':60},
    'w':{'cost':110, 'seats':77}
}

locations = ['wellington', 'rotorua', 'auckland']
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')


def flight_info(dest, tomorrow):
    """
    gets the flight info from flights
    """
    
    
    #get end flight letter
    dl = dest[:1]
    
    #set amount of seats and price
    cost = flights[dl]['cost']
    seats = flights[dl]['seats']
    
    #apply discount
    if tomorrow == True:
        off = 35/100*cost
        costn = cost - off
        
    #fill n seats
    randn = random.randint(5,seats-2)
    seats -= randn
    
    #return data
    return [round(costn, 2), seats, cost]
    

def make_email(dest, tomorrow, name):
    """
    makes the email.
    """
    clear()
    
    #gets items from flight info
    items = flight_info(dest, tomorrow)
    
    #set variables used for the email from items from flight info
    cost = items[0]
    seats = items[1]
    oldcost = items[2]
    
    #write email
    dear = f'Dear {name},'
    bodytmr = f'Flights to {dest} are usually {oldcost}, but flying with us tomorrow they are ${cost}!'
    body = f'Flights to {dest} start at around ${cost}, but flying with us tomorrow you can expect 35% off'
    end = f'There are only {seats} more tickets left, so dont miss out!'
    
    #display email
    print(dear)
    if tomorrow: 
        print(bodytmr)
    else:
        print(body)
    print(end)




def gather_data():
    """
    Def to gather data. takes in all data stated at top.
    """
    #input name
    name = input("Please enter your name: ")
    clear()
    
    #welcome user
    print(f'Welcome, {name}! ')
    print('We can fly you from Hamilton out to\nAuckland,\nRotorua,\nWellington\n')
    
    #get destination
    while True:
        dest = input('Where are you flying to? ')
        if dest.lower() in locations:
            break
        
        clear()
        

    #tomorrow?
    while True:
        tomorrow = input('Are you planning on flying today? (y or n) ')
        if tomorrow.lower() == 'y':
            tomorrow = True
            break
        elif tomorrow.lower() == 'n':
            tomorrow = False
            break
        
        clear()

    #get info
    make_email(dest, tomorrow, name)

    
    
gather_data()
