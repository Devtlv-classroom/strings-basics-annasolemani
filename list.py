list= [825, 262, 627, 826, 285, 221, 730, 340, 750, 989, 272, 842, 383, 575, 810]

print("There are {} numbers in the list.".format(len(list)))
print("The lowest number on the list is {}.".format(min(list)))
print("The highest number on the list is {}.".format(max(list)))
print("The sum of the list is {}.".format(sum(list)))

list2= ['spring', 'autumn', 'summer']
list2.insert(4, 'winter')
print(list2)
list2[1]='summer'
list2[2]='autumn'
print(list2)


topping = input("Please add a topping. Type 'quit' when finished adding. ")
while topping != "quit":
    topping = input("You have added {}. Please add another topping. Type 'quit' when finished adding. ".format(topping))
print("Your pizza has been ordered.")

age1= input("Please enter your age ")
while age1 != "quit":
    if age1 <3:
        price="free"
    if age1 >=3 and <12:
        price="$10"
    if age1 >=12:
        price="$15"
    age1 = input("Your ticket will be {}. Please add the next customer's age. Type 'quit' when finished adding. ".format(price))
print("Your tickets have been ordered.")