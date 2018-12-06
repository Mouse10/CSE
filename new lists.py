# creating a list
fruit = [' apples', 'oranges',  'watermelons',
         'strawberries','pears', 'melon', 'coconut', 'banana', ]
                                                                # use square brackets
print(fruit)


#putting items from a lists
print(fruit[1])

# getting the length of a lists
print(len(fruit))
print("The length of the lists is %d" % len(fruit))\

# modifying
fruit[1] = 'banana'
print(fruit)

# looping through lists
for item in fruit:
    print(item)

Games = ['Rocket League', 'fortnite', 'Destiny 2', 'Bo4']
print(Games[1])


food_lists = ['pizza', 'chicken', 'chips', 'tacos', 'mac and cheese', 'salmon',
              'sushi', 'hot fries', 'salad', 'tamales']


# slicing
print(food_lists[2:5])
print(food_lists[3:4])
print(food_lists[10:])
print(food_lists[:5])

# Adding stuff to a lists (part 1)
food_lists.append('oranges')
food_lists.append('tacos')
print(food_lists)
# Everything is in a form object.method(parameters)
food_lists.insert(2, 'pizza')
print(food_lists)


#Removing from a lists
food_lists.remove('tacos')
food_lists.remove('pizza')
print(food_lists)

# this removes the specific item from the lists

#removing from a lists (part 2)
#removing, you don't know what is in the lists, but you know
# you want to get rid of something at a specific index
food_lists.pop(0)
print(food_lists)

# Notice that 'pizza' is no longer in the lists because was at the index 0

#practice time...
"""
1. make a new lists with three items
2. Add a 4th item to the lists
3. Remove one of the first three items from the lists
"""


Sports_lists = ['Soccer', 'Football', 'Hockey', 'Ice Skating', 'Bicycle']


#finding things in a lists
print(Sports_lists.index('Hockey'))
# this printed 9 for me, so chicken must be at index 9
# this is an easy way of finding things in a lists

# things i notice people do
# some people have made lists with parenthesis instead of brackets
brands = ('apple', 'samsung', 'htc')
# this is a triple, not a lists tuples are immutable

# changing things in to a lists
string1 = "turquoise"
list1 = list(string1)
print(list1)

# hangman hints
for i in range(len(list1)):  # i goes through all indices robotis
    if list1[i] == "u":  # if we find a "u"
        list1.pop(i)  # Remove the i-th index
        list1.insert(1, "*")  #put a * there instead

#changing back into a string (list string)
print("".join(list1))

# Function Notes
# a** + b**2 = c**2
def pythagorean (a, b):
    return (a**2 + b**2) ** (1/2)


#
print(pythagorean(3, 4))


