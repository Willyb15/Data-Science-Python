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

Here we are using the `len()` function, a Python built-in and passing it both a list and a dictionary. This might seem fairly natural now, if you take a moment to think about how this works you may run into some logical stops. One thing that my come to mind is, considering our knowledge of how functions work, how are we passing two different data structures to `len()` and Python still able to know what we're asking, number one, and number two, reason about how "long" these decidedly different data structures are?

#### Something about Polymorphism


### Everything in Python is an Object!



### When to Use Classes
