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

Defining a magic method is as easy as defining any other method in a class. We actually did it last time with the `__init__()` method, so all you have to do is start with a def and then the name of the magic with the double underscores. **Note**: All methods with names beginning and ending with double underscores are magic methods, this naming convention is reserved for them.

Let's take a look at this with the `OurClass` class we created last time. I'm going to add a `__len__()` implementation to the code from last lecture. Considering that the, logically, the `len()` function should return a number of something it seems reasonable to have it return the number of questions asked we have stored. Instead of putting our code directly into IPython, this time we're going to store it in a script, `lecture.py`, and get some practice importing. Let's take a look.

```python
class OurClass(): 
    
    def __init__(self, name, location, size=0): 
        self.name = name
        self.location = location
        self.size = size
        self.questions_asked = []
        if self.size >= 20: 
            self.at_capacity = True
        else: 
            self.at_capacity = False

    def __len__(self):
        return len(self.questions_asked)

    def add_question_asked(self, question): 
        self.questions_asked.append(question)
    
    def add_class_members(self, num): 
        self.size += num

        if self.size >= 20: 
            print 'Capacity Reached!!'
            self.at_capacity = True

    def check_if_at_capacity(self): 
        return self.at_capacity
```

Now we can have `len()` interact with instances of `OurClass`.

```python
In [1]: from lecture import OurClass

In [2]: our_class = OurClass('Intro Python', 'Platte', 15)

In [3]: len(our_class)
Out[3]: 0

In [4]: our_class.add_question_asked("What's he going to show?")

In [5]: our_class.add_question_asked('Do you know the answer?')

In [6]: len(our_class)
Out[6]: 2
```

Just as we'd expect if we want to get the number of questions when calling `len()`. For reference, check out what would happen if we hadn't defined an implementation for `__len__()`.

```python
In [1]: from lecture import OurClass

In [2]: our_class = OurClass('Intro Python', 'Platte', 15)

In [3]: len(our_class)
___________________________________________________________________________
TypeError                                 Traceback (most recent call last)
<ipython-input-3-ae0663a04767> in <module>()
    > 1 len(our_class)

TypeError: object of type 'OurClass' has no len()
```

An error! At least Python lets us know that it's related to having no length, a problem that we now know how to fix!

### Using Classes Pragmatically

One question that comes up frequently in languages like Python that don't fall into a single [paradigm](https://en.wikipedia.org/wiki/Programming_paradigm) is learning when to use the different features of the language. As applied to our current circumstance, when should we be making classes instead of just using functions?

Part of the confusion in answering this question frequently stems from an incomplete understanding OOP's purpose in life, to take advantage of the ideas of inheritance, encapsulation and polymorphism.With this in mind let's discuss classes at a high level and see what kinds of problem attributes lend themselves to being solved with functions, procedurally, vs with OOP.

Similarly to one of the motivations for functions, abstraction, we see the idea of encapsulation espoused by OOP. Encapsulation is very much like abstraction in that it hides implementation details; however, with it we see the distinction that many functions, abstractions, can be bundled up together in a class. In addition we also see anther aspect of abstraction introduced, abstraction of the data itself. While we can instantiate a class with whatever properties we dictate, often these will specify the nature of the data (though sometimes it wont), we have the bundled methods that act on the data which are designed to keep us from caring about the exact state of that data. Sometimes this can be good and sometimes it can be bad.

#### Python has both functions and classes, so you can choose the one that suits your needs!

### Everything in Python is an Object!
