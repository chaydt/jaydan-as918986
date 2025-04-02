import os

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

locations = ['w', 'r', 'a']

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')


def flight_info(dest, tomorrow):
    #get end flight letter
    dl = dest[:1]
    
    cost = flights[dl]['cost']
    seats = flights[dl]['seats']
    
    return [cost, seats]
    
    


def gather_data():
    """
    Def to gather data. takes in all data stated at top.
    """
    #input name
    name = input("Please enter your name: ")
    clear()
    
    #welcome user
    print(f'Welcome, {name}! ')
    
    #get destination
    while True:
        dest = input('Where are you flying to? ')
        if dest.lower() in locations:
            break
        
        clear()
        

    #tomorrow?
    while True:
        tomorrow = input('Are you planning on flying today? (yes or no) ')
        if tomorrow.lower() == 'yes':
            tomorrow = True
            break
        elif tomorrow.lower() == 'no':
            tomorrow = False
            break
        
        clear()

    #get info
    print(flight_info(dest, tomorrow))

    
    
gather_data()
