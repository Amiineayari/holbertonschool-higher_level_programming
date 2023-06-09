Python - Data Structures: Lists, Tuples
This repository contains Python code examples and explanations for working with two fundamental data structures: lists and tuples.

Table of Contents
Lists
Creating a List
Accessing List Elements
Modifying List Elements
List Operations
List Methods
Tuples
Creating a Tuple
Accessing Tuple Elements
Modifying Tuple Elements
Tuple Operations
Lists
Creating a List
Lists in Python are ordered, mutable collections of elements. They can contain elements of different data types. Here's an example of creating a list:

python
Copy code
my_list = [1, 2, 3, "apple", "banana"]
Accessing List Elements
List elements can be accessed using indices, starting from 0. Negative indices can be used to access elements from the end of the list. Here are a few examples:

python
Copy code
my_list = [1, 2, 3, 4, 5]
print(my_list[0])    # Output: 1
print(my_list[3])    # Output: 4
print(my_list[-1])   # Output: 5
Modifying List Elements
Lists are mutable, meaning their elements can be modified. You can assign new values to specific indices or use list methods to modify the list. Here's an example:

python
Copy code
my_list = [1, 2, 3]
my_list[1] = 10
print(my_list)    # Output: [1, 10, 3]
List Operations
Python provides several operations that can be performed on lists, such as concatenation, repetition, and membership testing. Here are a few examples:

python
Copy code
list1 = [1, 2, 3]
list2 = [4, 5, 6]

concatenated_list = list1 + list2
print(concatenated_list)    # Output: [1, 2, 3, 4, 5, 6]

repeated_list = list1 * 3
print(repeated_list)        # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

print(2 in list1)           # Output: True
print(5 not in list2)       # Output: False
List Methods
Python provides various built-in methods to manipulate lists. These methods can be used to add or remove elements, sort the list, obtain the length, and more. Here are a few examples:

python
Copy code
my_list = [3, 1, 2, 4, 5]

my_list.append(6)
print(my_list)              # Output: [3, 1, 2, 4, 5, 6]

my_list.remove(2)
print(my_list)              # Output: [3, 1, 4, 5, 6]

my_list.sort()
print(my_list)              # Output: [1, 3, 4, 5, 6]

list_length = len(my_list)
print(list_length)          # Output: 5
Tuples
Creating a Tuple
Tuples are ordered, immutable collections of elements. They are similar to lists but cannot be modified once created. Here's an example of creating a tuple:

python
Copy code
my_tuple = (1, 2, 3, "apple", "banana")
Accessing Tuple Elements
Tuple elements can be accessed using indices, just like lists. Here are a few examples:

python
Copy code
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])    # Output: 1
print(my_tuple[3])    # Output: 4
print(my_tuple[-1])   # Output: 5
Modifying Tuple Elements
Since tuples are immutable, their elements cannot be modified. If you need to change a tuple, you have to create a new tuple with the desired elements. Here's an example:

python
Copy code
my_tuple = (1, 2, 3)
new_tuple = my_tuple + (4,)
print(new_tuple)    # Output: (1, 2, 3, 4)
Tuple Operations
Tuples support various operations, including concatenation, repetition, and membership testing, similar to lists. Here are a few examples:

python
Copy code
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)    # Output: (1, 2, 3, 4, 5, 6)

repeated_tuple = tuple1 * 3
print(repeated_tuple)        # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

print(2 in tuple1)           # Output: True
print(5 not in tuple2)       # Output: False
Conclusion
Lists and tuples are essential data structures in Python that allow you to store and manipulate collections of elements. Understanding their creation, access, modification, and various operations will enable you to work effectively with data in your Python programs.