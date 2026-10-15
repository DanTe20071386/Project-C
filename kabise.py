'''
this code checks leap years for shamsi and gregorian calendars
'''
def shamsi():
    '''
    this code checks leap years for shamsi
    '''
    year = int(input("enter a shamsi year(1244 to 1472) = "))
    if 1342 >= year >= 1244:
        if year % 33 == 1 or year % 33 == 5:
            print("your year is kabise")
        elif year % 33 == 9 or year % 33 == 13:
            print("your year is kabise")
        elif year % 33 == 17 or year % 33 == 21:
            print("your year is kabise")
        elif year % 33 == 26 or year % 33 == 30:
            print("your year is kabise")
        else:
            print("your year isn't kabise")
    elif 1472 >= year >= 1343:
        if year % 33 == 1 or year % 33 == 5:
            print("your year is kabise")
        elif year % 33 == 9 or year % 33 == 13:
            print("your year is kabise")
        elif year % 33 == 17 or year % 33 == 22:
            print("your year is kabise")
        elif year % 33 == 26 or year % 33 == 30:
            print("your year is kabise")
        else:
            print("your year isn't kabise")


shamsi()


def gregorian():
    '''
    this code checks leap years for gregorian
    '''
    miladi = int(input("enter a miladi year = "))
    if miladi % 400 == 0:
        print("your year is leap year")
    elif miladi % 100 == 0:
        print("your year isn't leap year")
    elif miladi % 4 == 0:
        print("your year is leap year")
    else:
        print("your year isn't leap year")


gregorian()
