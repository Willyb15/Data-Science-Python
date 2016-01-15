## Data Structures Continued

Up till now you have learned about some very useful data structures in Python, numeric types, strings and lists. However, the fun doesn't stop there! Today we are going to talk about some which will help us solve very different problems than we could up till now.

### Mutability

One thing that will come up as important distinction in the structures we learn about today is the concept of mutability. Mutability refers to the capability of an object to be changes after it has been instantiated. Remember that with lists we could change the contents at any arbitrary index and even grow the list dynamically. Just to refresh your memory.

```python
# Declare a simple list
l = range(10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8 , 9]

# Change the element at the 4th index, the fifth in the list, to 0
l[4] = 0  # [0, 1, 2, 3, 0, 5, 6, 7, 8 , 9] 

# Add the number 1 to the end of the list
l.append(1)  # [0, 1, 2, 3, 0, 5, 6, 7, 8 , 9, 1] 
```

However, there are times when you don't want your data structure to be mutable. For example, if you're allowing a user of your program to have access to a data structure, one way to ensure that they wont mess with it (sometimes users do this out of malice so we want to try and prevent it) is to make the structure immutable. There are many more reasons why mutability is a desired trait, we will discuss plenty more of them throughout the rest of the course.

Let's quickly discuss the mutability of objects you already know about. The first type you learned about were various numerics, these are all immutable. What?! Immutable you say? But I can change a value in a variable after it's been declared. Consider the following simple code.

```python
# First mention of x
x = 1

# Change the value of x
x = 2
```

How can numerics be immutable while, simultaneously, you can change the value of a numeric variable? What's really going on under the hood when you assign to a variable is Python puts that value or data structure in memory, then simply associates the variable name with that value or data structure. Changing a variable then simply amount to associating that name with a different thing in memory.

Using this same logic, it shouldn't be too hard to explain to yourself why strings are immutable as well. The contents of that string are put in memory and the variable name you want to use is associated with that string. When you want to change the variable to a different string, Python simply associates that name with a different, also immutable string.

`Note, the discussion of Python having names, [here](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#python-has-names) is really good if you're looking for more clarification.`

Lists, on the other hand, are mutable. What this really means is that you can change the structure of the list in addition to the names of the things that are in the list (notice the specific use of names there, we'll come back to that in the next section).

### Tuples

Tuples are simply the immutable brother of the list, aka immutable ordered collections. This means that once a tuple is instantiated, all you can do is access its contents. You cannot make a tuple longer. You cannot reassign what is in a tuple (there are some subtleties to this which we will discuss presently). Similar to lists, tuples are declared by passing an iterable to the `tuple()` constructor, with the syntactic sugary parenthesis, or without parenthesis (this works because Python automatically interprets comma separated things that aren't specifically specified otherwise, as tuples).

```python
my_first_tuple = tuple([1, 2])
my_other_tuple = (1, 2)
my_third_tuple = 1, 2
```

Alright, thats all well and good. But what are the direct implications of using a tuple versus a list. Well, suppose we are trying to grab the even numbers, stored in some collection, somewhere. If we were to do this with a list that might look like. 

```python
evens = []
for element in some_collection:
    if element % 2 == 0:
        evens.append(element)
```

We could try to do this with evens as a tuple instead of a list with `evens = ()`, but once we tried to run our code we would immediately get an error that says `AttributeError: 'tuple' object has no attribute 'append'` The error message is pretty self explanatory, in plain English it tells us that tuples have no ability to append. This is just as we expected given that they are immutable. (There are ways around constructing tuples with more complicated contents without first storing things in a list, we will talk about them later in the course).

You might be asking yourself, what can a tuple store? The answer is, just as with lists, anything! And just as with lists built in Python containers can all be either homogeneous or heterogeneous (know though, that there structures available that enforce homogeneity). Lets take a look at some of the things we can store. 

```python
In [1]: t = (1, 3.5)

In [2]: type(t[0])
Out[2]: int

In [3]: type(t[1])
Out[3]: float

In [4]: t = (1, [1, 2])

In [5]: type(t[1])
Out[5]: list

In [6]: t = (1, (1, 2))

In [7]: type(t[1])
Out[7]: tuple
```

One tricky thing about tuples is that even though they are immutable, if they are storing any mutable data types, those structures **can** be changed!

```python
In [1]: t = (1, [1, 2])

In [2]: t[1].append(3)

In [3]: t
Out[3]: (1, [1, 2, 3])
```

One last thing to note is that since tuples are immutable they very few methods associated with them, only `count()` and `index()`. For this reason we say that they are very lightweight, aka they don't take up much space in memory, but also don't have much built in functionality.
