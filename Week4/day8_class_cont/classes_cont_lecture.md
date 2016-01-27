## More On Python Classes

### Intro

Last class we learned about the programming paradigm known as OOP and we got some practice writing simple classes in Python. Today we are going to build on that knowledge and discuss a number of important things regarding classes and their use:

    * Python classes magic methods.
    * How everything in Python is actually an object (instantiated class)!
    * How to analyze when to use classes.

### Magic Methods

There are a number of things that we have been taking for granted in our use of Python so far. Let's dive into an example of where we were using some functionality built into Python but didn't think too much about how it was working.

```python
In [1]: my_list = [1, 2, 3]

In [2]: my_dict = {1: 'first', 2: 'second'}

In [3]: len(my_list)
Out[3]: 3

In [4]: len(my_dict)
Out[4]: 2
```

Here we are using the `len()` function, a Python built-in and passing it both a list and a dictionary. This might seem fairly natural now, if you take a moment to think about how this works you may run into some logical stops. One thing that my come to mind is, considering our knowledge of how functions work, how are we passing two different data structures to `len()` and Python is still able to know what we're asking, number one, and number two, reason about how "long" these decidedly different data structures are?

What's really happening under the hood when we pass a data structure to the `len()` function is that Python is going to that object and running its `__len__()` method. Ok, that sounds cool, but what does it all mean? This is an example of a **magic method** and we will dive into them shortly. For now, know that magic methods allow us, as creators of custom classes, to give them more robust functionality in terms of interacting with Python. So, just as the `__len__()` method was called when both a list and a dictionary was passed to the `len()` function, we can define a `__len__()` method on our custom classes so that Python knows what to do when you pass an instance of that class to the `len()` method; in addition, how Python gets a "length" from your class is entirely up to you!

#### Polymorphism Detour

The above example is a great example of polymorphism, that idea we quickly discussed last class. Let's take a moment to get a better handle on this idea. Polymorphism is defined as the provision of the same interface for entities of different types.

We see that idea in direct action in the above example. Though we were passing different types of entities to the `len()` function, because it implements the `__len__()` method on whatever object was passed to it, and any object can implement that method, we this notion of the same interface. And, even further, we see the benefits of setting up a paradigm with this design principle implemented. To make something work with `len()` all you have to do is make sure it defines the `__len()__` method. And, tada! The general structure of the interface, polymorphism in action, takes care of the rest.

Speaking of which. How do we define these "magic" methods?? End detour.

#### Defining a Magic Method

### Everything in Python is an Object!



### When to Use Classes
