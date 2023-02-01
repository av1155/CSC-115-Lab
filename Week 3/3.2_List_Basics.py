# Creating a list

''' 
Container: A construct used to group related values together and contains references to other objects instead of data.

List: A container created by surrounding a sequence of variables or literals with brackets []. Ex:

my_list = [1, 2, 3, 'abc']

 '''

my_list = ['$10', 14.99, 'abc']

print(my_list)

my_list2 = []  # empty list

# Accessing list elements
# Ex:

rolls_royce = 340000
bentley = 202000
ferrari = 302000

prices = [rolls_royce, bentley, ferrari]

print(f'Rolls Royce: {prices[0]} dollars')
print(f'Bentley: {prices[1]} dollars')
print(f'Ferrari: {prices[2]} dollars')

# Update / Modify List

prices[1] = 700000
print(f'Bentley: {prices[1]} dollars')

print()

my_var = my_list[2]  # Assigning my_var with the 3rd element of my_list.
print(my_var)

print()

# Adding and remove list elements.

'''
A method instructs an object to perform a certain action, and this is executed by specifying the method name following a "." symbol and an object.
* append() is used to ADD new elements to a list.
* pop() or remove() is used to remove elements from a list. 
'''

example_list = ['hi', 'THIS WAS REMOVED WITH .POP', 10, 'hello world']
example_list.append('abc123')

print(example_list)
print(example_list[3])

example_list.pop(1)
print(example_list)

example_list.remove('abc123')
print(example_list)

print()

the_list = [10, 'Andrea']
print(the_list)

# Adds the sentence "i am the best" to the list
the_list.append('I am the best')
print(f'After append: {the_list}')

# Removes the value associated to index 0 from the list.
the_list.pop(0)
print(f'After pop: {the_list}')

# Removes the sentence "i am the best" from the list
the_list.remove('I am the best')
print(f'After remove: {the_list}')


print()

''' 
Operation	        Description

len(list)	        Find the length of the list.
list1 + list2	    Produce a new list by concatenating list2 to the end of list1.
min(list)	        Find the element in the list with the smallest value. All elements must be of the same type.
max(list)	        Find the element in the list with the largest value. All elements must be of the same type.
sum(list)	        Find the sum of all elements of a list (numbers only).
list.index(val)	    Find the index of the first element in the list whose value matches val.
list.count(val)	    Count the number of occurrences of the value val in the list.

'''

# Concatenating lists
car_prices = [25000, 50000, 75000, 100000] + [150000]
print(f'There are {len(car_prices)} car prices in the list, and the cheapest car is: {min(car_prices)}.\nThe most expensive is: {max(car_prices)}')

print()

# AVERAGE # avg_price = sum(data) / len(data)

midterm_scores = [99.5, 78.25, 76, 58.5, 100, 87.5, 91, 68, 100]
final_scores = [55, 62, 100, 98.75, 80, 76.5, 85.25]

print(
    f'The average of the midterm scores is{(sum(midterm_scores) / len(midterm_scores)): .2f}')
print(
    f'The average of the final scores is{(sum(final_scores) / len(final_scores)): .2f}')

print(
    f'The average of both the midterm and final scores combined is:{(sum(midterm_scores) + sum(final_scores)) / (len(midterm_scores) + len(final_scores)): .2f}')

print('The index returned by number 62 is:', final_scores.index(62))
