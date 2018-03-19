#！/usr/bin/env python3
# -*- coding utf-8 -*-

class Restaurant():
    def __init__(self, restaurant_name, restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name + "'s type is " + self.restaurant_type + ".")

    def open_restaurant(self):
        print(self.restaurant_name + " is open now!")

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, increment_num):
        self.number_served += increment_num

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, restaurant_type):
        super().__init__(restaurant_name, restaurant_type)
        self.flavors = ['abc', 'hhs', 'ddfsa', 'fgfdsd']

    def show_icecream(self):
        print("The icecream'types are:")
        for i in self.flavors:
            print("\t-" + i.title())

icrm = IceCreamStand('xiaodian', 'icecream')
icrm.show_icecream()