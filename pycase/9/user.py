#！/usr/bin/env python3
# -*- coding utf-8 -*-

class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        full_name = self.first_name + ' ' + self.last_name
        print(full_name.title() + ' is ' + str(age) +  ' years old.')

    def greet_user(self):
        print("Hello, Mr " + self.first_name.title() + '.')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempt(self):
        self.login_attempts = 0

class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
        print("The rights of the Admin are: ")
        for i in self.privileges:
            print("\t-" + i)

class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()

admin = Admin('xie', 'ping', 34)
admin.privileges.show_privileges()