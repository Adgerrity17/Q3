#Quant connect tutorial 3- Functions
#https://www.quantconnect.com/tutorials/introduction-to-financial-python/functions-and-objective-oriented-programming
#Also utilzing examples from Automate the Boring Stuff Chapter 3

def product(x,y):
    return x*y # multiply the 2 parameters
print(product (2,3)) #returns 6

tickers = ['APPL', 'GOOGL', 'IBM', 'FB', 'F', 'V', 'G', 'GE']
print("the number of tickers is {}".format(len(tickers)))
for k in range(len(tickers)):
    print(k + 1, tickers[k])


print(list(map(len, tickers))) #print the length of the ticker inpu

a = map(lambda x: (x ** 2), range(10)) # should return the square of all values in range 10
print(a)


b = map(lambda x, y: (x + y), [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) # should add the values from list 1 to list 2
print(b)

price_list = [('Appl', 144.09), ('Googl', 911.11), ('Msft', 69.96), ('Wmt', 75.32)]
c = sorted(price_list, key = lambda x: x[1]) # sort low to high price
print(c)

d = sorted(price_list, key = lambda x: x[1], reverse = True) # sort high to low price
print(d)

price_list.sort(key = lambda x: x[1]) # sort high to low using the sort function
print(price_list)


#object oriented programming
class Stock:
    def __init__(self, ticker, open, close, volume):
        self.ticker = ticker
        self.open = open
        self.close = close
        self.volume = volume
        self.RoR = float(close) / open - 1

    def update(self, open, close):
        self.open = open
        self.close = close
        self.RoR = float(self.close) / self.open - 1

    def print_return(self):
        print(self.RoR)

        apple = Stock('APPL', 143.69, 144.09, 20109375)
        google = Stock('GOOGL', 898.70, 911.70, 1561616)

        apple.ticker()
        google.print_return()

#fortune project

print("This program will determine your fortune based upon your age, favorite color, and favorite number")
name = input("What is your name? : ")
age_str = input("How old are you? : ")
age_int = int(age_str)
user_color = input("What is your favorite color? : ")
number_str = input("What is your favorite numer? : ")
number_int = int(number_str)
#The information gathered above is the demographic information required to output the user's forturne

Fortune_1 = "You will see someone you did not expect to see today"
Fortune_2 = "Your lucky numbers for today are 18, 47, 28, and 94"
Fortune_3 = "Today is a good day to wear blue"
Fortune_4 = "Avoid taking unnecessary gambles"
Fortune_5 = "Time heals all wounds, keep your head up"
Fortune_6 = "Do or do not... there is no try"
Fortune_7 = "You will find a bushel of money"
Fortune_8 = "Watch out for cloaked strangers laughing menacingly"
Fortune_9 = "The rap game got it all wrong, you should save your money"
#These are the 9 possible fortune outputs
if (age_int < 18):
    if user_color == 'green':
        print(name, "the fortune teller predicts", Fortune_1)
    if user_color == 'blue':
        print(name, "the fortune teller predicts", Fortune_2)
    elif user_color != 'blue':
        if user_color != 'green':
            if number_int < 50:
                print(name, "the fortune teller predicts", Fortune_3)
            if number_int >= 50:
                print(name, "the fortune teller predicts", Fortune_4)
if (age_int > 18):
    if user_color == 'orange':
        if number_int <= 5:
            print(name, "the fortune teller predicts", Fortune_5)
        if number_int > 5:
            print(name, "the fortune teller predicts", Fortune_6)
    elif user_color != 'organge':
        print(name, "the fortune teller predicts", Fortune_7)
if (age_int == 18):
    if number_int == 3:
        print(name, "the fortune teller predicts", Fortune_9)
    else:
        print(name, "the fortune teller predicts", Fortune_8)
#The fortune will display below using boolian expression




import random
def fortune_teller(x):
    if x == 1:
	    print('You will have a good day')
    elif x == 2:
	    print('you will go to work')
    elif x == 3:
	    print('you will spend your day doing python')
    else:
	    print('go have a drink')
i = random.randint(1, 4)
fortune = fortune_teller(i)
print(fortune)





