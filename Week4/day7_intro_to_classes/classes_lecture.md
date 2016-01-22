## Object-Oriented Programming (OOP) with Classes 

### Background/Motivation 

From [wikipedia](https://en.wikipedia.org/wiki/Object-oriented_programming): 'Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which are data structures that contain data, in the form of fields, often known as attributes; and code, in the form of procedures, often known as methods.'

Okay, so I now have this vague idea of what an 'object' is, but how does it relate to Python? It turns out, everything in Python is an object. Everything in Python stores data, and has methods that operate on that data. Strings are a perfect example of this. When we have a string, it stores the individual characters that make up the string (*this is the __data__*), and we have **methods** (`lower()`, `upper()`, `replace()`, etc.) that operate on that data.

With knowledge of what an object is, let's discuss how they are related to **classes**. It turns out that a **class** is simply a blueprint for how to create an object. It tells us what data an object will store, and what methods that object will have available.  By building different classes (i.e. blueprints), we can build different objects (and then they can interact with each other, which we'll get to). Okay, cool. But why use classes? 

We use classes for much the same reasons that we use functions - *reusability* and *abstraction* (there are actually some more specific design principles behind OOP that we'll go into shortly). Classes allow us to build reusable objects, while at the same time abstracting away the inner workings of those objects. This way, users of our classes can build objects with them, and then interact with those objects without really caring about their inner workings. For example, when we interact with strings using the `replace()` method, we don't have to think about how the string replaces a given substring with whatever substring we tell it to; we just have to know that it does in fact do that.

### Design Principles 

The motivation for object-oriented programming (OOP) is actually heavily rooted in design principles, namely the principles of *inheritance*, *encapsulation*, and *polymorphism*. This terminology is more of an advanced topic in computer programming, and so we'll only cover it briefly here (while it is advanced, any treatment of OOP should at least mention these, which is why we do here).

* **Inheritance** - When a class is based on another class, using the same implementation to maintain the same behavior.  
* **Encapsulation** - The practice of hiding the inner workings of our class, and only exposing what is necessary to the outside world. This idea is effectively the same as the idea of **abstraction**, and allows users of our classes to only care about the what (i.e. what our class can do) and not the how (i.e. how our class does what it does). 
* **Polymorphism** - The provision of a single interface to entities of different types. This enables us to use a shared interface for similar classes while at the same time still allowing each class to have its own specialized behavior. 

While OOP does enjoy the benefits of the above design principles, it also kind of matches how we thing about the world. The world is composed of objects, where objects can be people, houses, cars, buildings, etc. These objects have some properties about them (i.e. they contain data), and they can do things (i.e. they have methods that can be applied). Object oriented programming approaches a programming problem by using objects that interact with each other, much like they do in the real world. 

### Terminology

Before we get to actually learning how to build a class, it'll be helpful to define some of the terminology surrounding classes/OOP. Often times, the terminology can be the most confusing part of learning OOP. 

1. Class - used to refer to the abstract concept of an object.
2. Object - An actual instance of a class.
3. Instance - What Python returns when you tell it to create a class.
4. Instantiation - A fancy for saying that we're going to create an instance of a class. 
5. Constructor - What we call to instantiate a class. 
6. self - Inside of a class, a variable for the instance/object being accessed (i.e. it holds a reference to the instance/object of that class).
7. attribute/field/property - A property or piece of data that a class has, stored in a variable. Inside of a class definition, all attributes/fields/properties are assigned via self, while outside of a class definition, they are accessed via *dot notation*.
8. method/procedure - A block of code that is accessible via the class, and typically acts on or with the classes attributes/fields/properties. Inside of a class definition, all methods/procedures are created via def. (they are really just functions) and accessible via self, while outside of a class definition, they are accessed via *dot notation*. 

Don't worry if this terminology isn't 100% clear at this point in time. It should become more clear as we work through these notes, and should be a useful reference. From here on out, we'll treat attribute, field, and property as interchangeable, and we'll do the same with method and procedure.

### Defining A Class

Much like defining a function, there is a common format to defining a class. It is almost exactly the same as defining a function, but we replace `def` with `class`. That is, we write `class`, then the name of the class that we are defining, followed by a set of parentheses, and finally a colon. After the colon is an indented block of code that we use to define the class attributes and methods. One subtle difference is that with functions, the standard is to name these beginning in lowercase and separating words with underscores (i.e. snake_case), while with classes, the standard is to name these beginning in uppercase, and not separate words at all (i.e. CamelCase). For example...

```python 
class OurClass(): 
    # attributes and methods go in here.
```

*Note*: As we'll show below, `OurClass()` is exactly what we'd used to create an instance of this class, and is the **constructor** for this class. 

#### Instantiation 

Like we mentioned above, **instantiation** is just a fancy word for saying that we're going to create an instance of a particular class. We do this by calling the **constructor** for our class, which is the name that we give our class right after the `class` statement in its definition. 

```python 
our_class = OurClass() 
```

Okay, cool! Let's revisit some of the terminology that we discuss above. We've shown you how to define a class, and **instantiate** it using a **constructor**. What we've done directly above, with `our_class`, is created an **instance** of `OurClass` that we've stored in the `our_class` variable. This variable is an object that theoretically has **attributes** and **methods** which we can use to interact with it (we say theoretically because we didn't actually define any attributes or methods above). Awesome! Now let's look at how to actually build a class that does something.   

