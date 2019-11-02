# Ask a user for his name, and if it starts with a vowel, greet him
# 
name= input("What is your name? ")

if ((name[0]) in"AEIOUaeiou"):
    print("Hello {}".format(name)+", your name begins with a vowel.")
else:
    print("No greeting for you.")