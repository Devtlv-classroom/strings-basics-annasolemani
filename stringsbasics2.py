#<!-Tags=["strings", "if-statements", "input"]-->

#Exercise (easy)
#Ask the user for his name, and tell him if the last letter is a vowel or a consonant
name= input("What is your name? ")

if ((name[-1]) in"AEIOUaeiou"):
    print("Hello {}".format(name)+", the last letter of your name is a vowel.")
else:
    print("Hello {}".format(name)+", the last letter of your name is a consonant.")

#Exercise (easy)
#Ask the user for two numbers (one after the other) and then print their sum
number1= input("Please enter the first number: ")
number2= input("Please enter the second number: ")
number1= int(number1)
number2= int(number2)
print("The sum of the two numbers is {}.".format(number1+number2))

#Exercise (medium)
#Challenge the user to print the longest sentence without any "A", if he achieves it, tell him how many letters he wrote, else, print a fail message.
sentence= input("Please enter the longest sentence you can without using the letter 'A'. ")
length= len(sentence) - sentence.count(' ')

if ("A" in sentence) or ("a" in sentence):
    print("This sentence contains an 'A'. Try again.")

else:
    print("Well done! Your sentence contains {} letters.".format(length))

#Exercise (medium)
#Ask the user for his full name (example: "John Doe"), and check the validity of his answer:
#The name should contain only letters.
#The name should contain only one space.
#The first letter of each name should be upper cased.
name= input("Please enter your first and last name: ")

if name.islower():
    print("Error. First letter of each name should be capitalized.")
if "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0" in name:
    print("Error: Name should contain only letters.")
if (name.count(' ') >= 2):
    print("Error: Name should contain only one space.")
else:
    print("Hello, {}.".format(name))



#Exercise (medium)
#Ask the user for a sentence, and then tell him how many words are in it.

#Exercise (medium)
#Write a python program to get a string made of the first 2 and the last 2 chars from a given string, if the string length is less than 2, return instead the empty string.
#For example: "Helloworld" output "Held", while "Sik" returns ""