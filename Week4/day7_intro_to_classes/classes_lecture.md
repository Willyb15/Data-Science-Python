## Object-Oriented Programming with Classes 

### Background/Motivation 

From [wikipedia](https://en.wikipedia.org/wiki/Object-oriented_programming): 'Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which are data structures that contain data, in the form of fields, often known as attributes; and code, in the form of procedures, often known as methods.'

Okay, so I now have this vague idea of what an 'object' is, but how does it relate to Python? It turns out, everything in Python is an object. Everything in Python stores data, and has methods that operate on that data. Strings are a perfect example of this. When we have a string, it stores the individual characters that make up the string (*this is the __data__*), and we have **methods** (`lower()`, `upper()`, `replace()`, etc.) that operate on that data.

With knowledge of what an object is, let's discuss how they are related to **classes**. It turns out that a **class** is simply a blueprint for how to create an object. It tells us what data an object will store, and what methods that object will have available.  By building different classes (i.e. blueprints), we can build different objects (and then they can interact with each other, which we'll get to). Okay, cool. But why use classes? 

We use classes for much the same reasons that we use functions - *reusability* and *abstraction* (there are actually some more speific design princples behind OOP that we'll go into shortly). Classes allow us to build reusable objects, while at the same time abstracting away the inner workings of those objects. This way, users of our classes can build objects with them, and then interact with those objects without really caring about their inner workings. For example, when we interact with strings using the `replace()` method, we don't have to think about how the string replaces a given substring with whatever substring we tell it to; we just have to know that it does in fact do that.


