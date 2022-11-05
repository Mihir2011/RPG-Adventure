import os

def Dereckbro():
    input(BLUE + "Dereck says: Why did you come here ")
    ask1 = input(WHITE + "1. For earning money \n2. For exploring ")
    if ask1 == "1":
        input(BLUE + "Lame bro lets explore")
    
    if ask1 == "2":
        input(BLUE + "Nice bro you have some SWAG ")



def bagcheck():
    c3 = input(WHITE + "1. Water bottle \n2. Toilet paper \n3. Towel \n4. Cloths \n5. Back ")
    if c3 == "5":
        os.system('cls')
        doselect()

def bagselect():
    c2 = input(WHITE + "1. Check bag \n2. Back ")
    if c2 == "1":
        os.system('cls')
        bagcheck()

    if c2 == "2":
        os.system('cls') 
        doselect()

def doselect():
    c1 = input(WHITE + "What do u want to do? \n1. Bag \n2. Talk with Dereck ")
    if c1 == "1":
        bagselect()

    if c1 == "2":
        Dereckbro()


BLUE    = '\033[34m'
WHITE   = '\033[37m'
input(WHITE + "Welcome To The Amazing World Of Life ")
input(WHITE + "This Game Has No Limits ")
input(WHITE + "Exept you that is. ")
input(WHITE + "Very well then lets get started. ")
os.system('cls')
input(BLUE + "Dereck says: Hello welcome to tokyo ")
doselect()


