# Simple madlib program to understand formated string

# String's can be added to varibale using
# concatination
# name = input("Your name: ")
# print("Hello," + name + "!")

# format operation
# print("Hello,{}!".format(name))

# # f' formatting
# print(f"Hello,{name}!")


# madlib is game where we can input of strings from user
# and fit in a already defined string to genereate a meanningful 
# # statement
# adj = input("Enter the adj:")
# verb = input("Enter the verb:")
# last = input("Enter the last word:")

# base  = f"Programming is for people who love to {adj}.It can be very \n intiutive to learn at first because of {verb}.But it's {last}!"
# print(base)

food = input("Food:")
name = input("Name:")
adj = input("Adjective:")
noun = input("Noun:")
verb1 = input("Verb1: ")
verb2 = input("Verb2: ")
verb3 = input("Verb3: ")

story1 = f'''It was {food} day at school, and {name} was super
{adj} for lunch. But when she went outside to eat, a
{noun} stole her {food}! {name} chased the {noun} all 
over school. She {verb1}, {verb2}, and {verb3} through 
the playground. Then she tripped on her {noun} and the 
{noun} escaped! Luckily, {name} ’s friends were willing 
to share their {food} with her.'''
print(story1)