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

### Dictionaries

So far the only collections that we have talked about are ordered and these are great if there is some intrinsic order to that data that we're storing in them. However, there are plenty of times when we don't care about order, either because it simply doesn't matter or because the data is associated with each other in a different way. For example say we have a bunch of state names and we want to associate their capital. How would we do this in a list? One way would be to have tuples that store the state and it's capital together.

```python
states_caps = [('Georgia', 'Atlanta'), ('Colorado', 'Denver'), ('Indiana', 'Indianapolis')]
```

But there are limits to how intuitive this storage method is. Consider that, if we wanted to find the capital of Indiana, we would have to search through the entire list checking to see if Indiana is in the first position of each tuple, and when/if we found it, then grab the second position of that tuple.

```python
search_state = 'Indiana'
capital = 'State not found'
for state_cap in states_caps:
    if state_cap[0] == search_state:
        capital = state_cap[1]
        break
print(capital)
```

While this isn't horrible, we can do better. Python to the rescue!!!

The dictionary data structure in Python allows us to store data in exactly the way that we wanted, storing a value associated with a keyword. In the example above we wanted to store the capital as the value associated with each state keyword. There are many ways to instantiate a dictionary. Lets look at the simplest way first.

```python
In [1]: states_caps_dict = {'Georgia': 'Atlanta', 'Colorado': 'Denver', 'Indiana': 'Indianapolis'}

In [2]: states_caps_dict
Out[2]: {'Colorado': 'Denver', 'Georgia': 'Atlanta', 'Indiana': 'Indianapolis'}
```

See how it looks very similar to the way the we made lists and tuples, expect now we use curly braces and there is this new use of colons, `:`. On the left side of each colon we have the keyword, and on the right the value associated with it. Each *key-value* pair, as we call them, is separated by a comma.

So how do we use these things once we have them? Lets take the example from above and say we're trying to figure out what the capital of Indiana is. With a list of tuples we had to search through to find the entry with 'Indiana' in the first position and then grab the second entry in that tuple. With dictionaries it's way simpler!

```python
In [1]: states_caps_dict = {'Georgia': 'Atlanta', 'Colorado': 'Denver', 'Indiana': 'Indianapolis'}

In [2]: states_caps_dict['Indiana']
Out[2]: 'Indianapolis'

In [3]: states_caps_dict['Washington']
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-3-96fac88f6748> in <module>()
----> 1 states_caps_dict['Washington']

KeyError: 'Washington'
```

All we had to do was index into the dictionary, like we did with lists, but this time with the keyword, and the dictionary returns the associated value. Notice how, if we tried to find a keyword that wasn't already in the dictionary with `[]` indexing we get a `KeyError` telling us that that key is not stored in the dictionary. 

This shouldn't happen to frequently, because we often know exactly what the keys in our dictionaries are. However, there are times when we don't know if a keyword is in the dictionary already. For these times we luckily have the `get()` method. This method takes the keyword you're trying to find and a default return value to hand back if the key doesn't exist.

```python
In [4]: states_caps_dict.get('Washington', 'State not found')
Out[4]: 'State not found'
```

Above we asked `states_caps_dict` for the value associated with the key `'Washington'`, and told it to return `'State not found'` if the keyword wasn't in the dictionary. And lo-and-behold, we get back `'State not found'` which makes sense because we knew that `'Washington'` wasn't in the dictionary.

#### Mutability of Dictionaries

At this point a question that could be on your mind couple be, are dictionaries mutable? Well, first, great question. And, second, yes, yes they are! Before we talk about how to mutate them, lets describe dictionaries in the language that we used for lists and tuples. A dictionary is defined as an unordered collection of key-value pairs that require unique keys.

With that in mind, lets recall how we mutated a list. To change an element at an existing index we just indexed into the list and did assignment. To make them bigger we used the `append()` method. This method of mutation made a lot of sense considering that lists are ordered. So, in the unordered paradigm where dictionaries live to either change/add a key-value pair to a dictionary all you have to do index into it with the existing/new, respectively, key and assign the value to it. Lets take a look.

```python
In [1]: my_dict = {'thing': 1, 'other': 2}

In [2]: my_dict['thing']
Out[2]: 1

In [3]: my_dict['thing'] = 3

In [4]: my_dict['thing']
Out[4]: 3

In [5]: my_dict['thingy'] = 4

In [6]: my_dict['thingy']
Out[6]: 4

In [7]: my_dict
Out[7]: {'other': 2, 'thing': 3, 'thingy': 4}
```

#### Caveat to Dictionary Keys, More on Mutability

We have learned that dictionaries make it easy to store key-value relationships in a single data structure that is designed for easy value retrieval. So, what are the restrictions on things you can put in a dictionary? As for the values, like in lists, there are none! But the keys those values are associated with, that's a different story.

Keys in dictionaries **must** be an immutable type, and if that type is an container then the container cannot contain any mutable types. Why is this the case? The answer lies in the way that dictionaries store values and associate them with a key under the hood.

Python dictionaries are an implementation of what's known as a *hash map* or *hash table* ([here's](https://en.wikipedia.org/wiki/Hash_table) the wikipedia page for them if you want to learn more). This computer science idea is basically a function that relates any input, in our case the keys, to a location in memory. Thus, retrieval of a value from a dictionary is entirely dependent on what the key originally associated with it was. The consequence of this is that, if we were to use a mutable type as the key for a dictionary and later changed what that key looked like by mutating it, the dictionary wouldn't be able to find the value it was supposed to associate with that key; because that key is no longer the key it was.

```python
# Original key
my_bad_key = ['key']

# Dictionary declared with a list as a key
my_dict = {my_bad_key: 'This wont work'}

# Let's change that key
my_bad_key[0] = ['other_key']

# How is the dictionary supposed to know what we're looking for???
my_dict[my_bad_key]
```

This idea is so important that Python doesn't leave it up to you to remember to make keys types that are immutable. It just flat out wont let you do it.

```python
In [1]: my_bad_key = ['key']

In [2]: my_dict = {my_bad_key: 'This wont work'}
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-2-a1fb4b3621ba> in <module>()
----> 1 my_dict = {my_bad_key: 'This wont work'}

TypeError: unhashable type: 'list'
```

The above code attempts to set a list as a key to a dictionary. Luckily it throws an error as soon as we try, telling us that it can't hash a list, read: list's aren't immutable.

#### Getting More Out of Dictionaries

We now know how to make and alter dictionaries and how to use them to store arbitrary key-value pairs; let's talk about how to use them with loops.

As with lists and tuples, dictionaries are iterables in Python. This means that Python knows how to traverse everything that's stored in the collection. The way we did this with list was with a `for` loop. We will again use the `for` loop with dictionaries, however there are a few changes in how it's implemented because dictionaries are unordered key-value pairs whereas lists are ordered collections of values.

Lets revisit how we traverse a list with a `for` loop. Consider the following code that only prints the even numbers between 0 and 9.

```python
for element in range(10):
    if element % 2 == 0:
        print(element)
```

This specific syntax makes sense because, one at a time, we want to check each value in the list, each time we grab one we give it the name `element`, and check if it's even, printing that value if it is. It's the one at a time part that I want to call you're attention to, lists are an ordered collection of values; dictionaries on the other hand have keys and values that are tied together. However, if we were to traverse a dictionary with a for loop we expect to only get one of these out. Naturally it's the keys.

```python
In [1]: states_caps_dict = {'Georgia': 'Atlanta', 'Colorado': 'Denver', 'Indiana': 'Indianapolis'}

In [2]: for thing in states_caps_dict:
   ...:     print(thing)

Georgia
Indiana
Colorado
```

In addition to the states, aka the keys, being what is accessed when looping over a dictionary, notice that they aren't in the order that we we created the dictionary in. Remember that dictionaries are unordered?? Here we see a direct ramification of that fact; we are not guaranteed an particular order when accessing a dictionaries keys. It's not necessarily a problem, just something that's good to know.

The natural question then is to want to loop through all of the values. This can be done with the aptly named `values()` method on dictionaries.

```python
In [1]: states_caps_dict = {'Georgia': 'Atlanta', 'Colorado': 'Denver', 'Indiana': 'Indianapolis'}

In [2]: for value in states_caps_dict.values():
   ...:     print(value)

Atlanta
Indianapolis
Denver
```

We can see that all of the capitals, the values, in the dictionary, are printed, again in no particular order. One thing to know is that there is an analogue to values for keys, `keys()` that explicitly does exactly what we saw above when we just looped through the dictionary.

This is a very useful feature, but we can get better! One of the most useful ways to loop through the contents of a dictionary is by getting each key-value pair together in turn within the loop. The `items()` methods does exactly this. To use it we will employ the same syntax as we did with `enumerate`.

```python
In [1]: states_caps_dict = {'Georgia': 'Atlanta', 'Colorado': 'Denver', 'Indiana': 'Indianapolis'}

In [2]: for state, capital in states_caps_dict.items():
    print(state, capital)

Colorado Denver
Indiana Indianapolis
Georgia Atlanta
```

This is awesome! But as a learning tangent, lets see what's happening when we use this syntax. As above we are going to use the `items()` method, but this time not sure state *and* capital.

```python
In [1]: states_caps_dict = {'Georgia': 'Atlanta', 'Colorado': 'Denver', 'Indiana': 'Indianapolis'}

In [2]: for thing in states_caps_dict.items():
    print(thing)
   ...:     
('Georgia', 'Atlanta')
('Indiana', 'Indianapolis')
('Colorado', 'Denver')
```

Now that we're only using only a single variable to grab the output of `items()`, we can clearly see that the method is outputting a tuple. So what was happening when we used `state` and `capital` to grab the output?? Very frequently we want to put the separate values a collection stores into different variables. This happens so frequently, in fact that Python has a built way to do it quickly called **unpacking**. 

So, when, Python sees the two variable names `state` and `capital` in the first implementation, it knows to take the values in the tuple returned from `items()` and put the first one in `state` and the second in `capital`. This is what was happening when you called enumerate, it returned a tuple with the number value it was on, and the value itself. It is up to you whether or not to grab those values in a single variable as a tuple or have Python unpack it for you into two variables. 

`Note, Python will not allow you to "unpack" a single variable into multiple.`
