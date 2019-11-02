# Ask two users for their names, and then tell them who got the longest name.
#

name1= input("Please enter the first name ")
name2= input("Please enter the second name ")

if len(name1)>=len(name2):
    print("{} is longer than {}".format(name1, name2))
else:
    print("{} is longer than {}.".format(name2, name1))