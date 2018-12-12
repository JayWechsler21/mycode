#!/usr/bin/env python3
message = 'ok.. '
print('What is your favorite Christmas movie?')
list1 = ['1 Christmas Vacation', '2 Eight Crazy Nights', '3 Other']
print(list1[0])
print(list1[1])
print(list1[2])
connection = float(input())
if connection == 1:
    message = message + 'Awesome choice.'
elif connection == 2:
    message = message + 'Happy Hannukah.'
else:
    message = message + 'You need another choice of movie.'
print(message)