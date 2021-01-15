class Card:
    def __init__(self, suit, number):
        # Adding an underscore at the start of "suit" in
        # self.suit is done to indicate that this attribute
        # should not be modified/accessed directly
        self._suit = suit
        self._number = number
        self._value_high = None
        self._value_low = None
        self.value(number)

    # The __repr__ method allows the user to define the
    # output when an instance of the class is printed
    def __repr__(self):
        return self.number + " of " + self.suit

    def value(self, number):
        if number.isnumeric():
            self._value_high = int(number)
            self._value_low = int(number)
        elif number.upper() in ["J", "Q", "K"]:
            self._value_high = 10
            self._value_low = 10
        elif number.upper() == "A":
            self._value_high = 11
            self._value_low = 1

    # The @property is a decorator used to identify the suit 
    # method as a "getter" function. It acts as an intermediary
    # to allow the user to GET the value of self._suit without
    # accessing it directly. This would be done with a call like
    # my_card.suit
    @property
    def suit(self):
        return self._suit

    # The @suit.setter is a decorator used to identify the suit
    # method as a "setter" function. It acts as an intermediary
    # to allow the user to SET the value of self._suit without
    # accessing it directly. This would be done with a call like
    # my_card.suit = "hearts"  
    @suit.setter
    def suit(self, suit):
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            print("That's not a suit!")

    # The "getter" and "setter" decorators allow their resptive
    # methods to share the same name. Depending on what the user
    # is trying to do, the program will know which one to use.

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if number in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
            self._number = number
            value(number)
        else:
            print("That's not a number found in a deck of cards!")

    
my_card = Card("hearts", "A")

# Without the __repr__ method defined in the class above
# print(my_card) would result in the output being an object 
# reference such as: <__main__.Card object at 0xb67290f0>
# print(my_card)

# By defining the __repr__ method in the class above, now when
# print(my_card) is called, instead of the ugly object reference
# the output shows as "6 of hearts"

# Another way of viewing the suit and number values of the
# card would be to call each through the attribute
# print(my_card.suit)
# print(my_card.number)

# Remember that my_card.suit can't access the suit attribute 
# directly, but instead triggers the "getter" method of the 
# class to retrieve the information. You can see by running both
# that they return the same thing.

# print(my_card.suit)
# print(my_card._suit)

# You can also tell that my_card.suit is triggering the "getter"
# and "setter" methods by trying to modify my_card.suit with 
# something other than "hearts", "clubs", "diamonds", or "spades".
# You will get the "That's not a suit!" message that is part of 
# the "setter" method

# my_card.suit = "pickles"

# But if you set my_card._suit instead, then you won't get an 
# error. You can check this by setting my_card._suit to something
# other than "hearts", "clubs", "diamonds", or "spades" and then 
# print my_card._suit

# my_card._suit = "pickles"
# print(my_card._suit)

# As you can see the "setter" method wasn't triggered and didn't 
# prevent you from setting my_card._suit to whatever you wanted to.
# Though let's set it back to "hearts"

# my_card._suit = "hearts"
# print(my_card._suit)

# print(my_card._value_low, my_card._value_high)
