# Python Workshop: Classes and Objects

Today we will add a very important skill to our toolbox: the ability to create our own data types.

We have already seen how useful having many data types can be:
  - Lists store ordered collections of data.
  - Dictionaries create mappings between one type of data and another.

To create our own datatypes, we will need to introduce two new primary concepts:

  - **Objects** is (are?) a word we have been using informally up to now.  An object is the most generic name for a piece of data manipulated within a computer program.  Everything we have studied so far is an object.  After today we will be able to create our own custom objects and inject them with whatever behaviour is appropriate to the problem we are solving.

  - **Classes** are object templates.  They are a sort of design document for manufacturing objects of a custom type.  They are also used to define the behaviour of a new type of object, and also serve as factories to create them.

Classes and objects are powerful, subtle tools.  It takes many years of practice to master their use.

## Outline

#### Objects

  - The primary objects: lists, sets, dictionaries, tuples, strings, numeric types
  - An example custom object: `StringStamper`
  - Creating objects
  - Looking inside an object: `dir`
  - Picking apart objects: attributes
  - Picking apart objects: methods

#### Classes and Methods

  - The `StringStamper` class.
  - The `class` keyword
  - Constructing new objects: the `__init__` method
  - `self` and self-reference
  - Methods.
  - `self` and self reference
  
## Objects

**Object** is a generic term for data inside a computer program.  This data can come in many forms, don't think of just tables or spreadsheets.  Think numbers, strings, and collections of them.

### The primary objects: lists, sets, dictionaries, tuples, strings, numeric types.

These primary objects are provided by python itself, and will serve as building blocks for all of our further exploration.  Because they are so fundamental, it is imperative that any python programmer is skilled in manipulating these objects.

  - Objects can contain other objects.

I.e., dictionaries can contain lists which in turn contain dictionaries.  You can make this as complex as you wish, but be careful, you still need to understand what you've done!

### An example custom object: `StringStamper`

We've provided a very simple custom object template (what we will call a **class** very soon) in `stringstamper.py`.  To use it in your python environment, use the `import` statement like this:

```
$ from stringstamper import StringStamper
```

### Creating objects: The Construction Pattern

The `StringStamper` we imported serves as a template for creating new object.  Here's how you can use it to create a new object.

```
$ ss = StringStamper("Property of Matt.")
```

Now `ss` is an object of type `StringStamper`.  We have a new **type** of object to play with.

```
$ type(ss)
stringstamper.StringStamper
```

#### Exercise: Two Objects
Create two `StringSampler` objects containing different messages.

### Looking inside an object: `dir`

One you have an object to play with, the `dir` function will show all its contents, options, bells and whistles.

```
$ dir(ss)
```

We will leave the weird contents that begin with double underscores as a topic for tomorrow. 

### Picking apart objects: attributes

When you called `dir` on the `ss` object hopefully you saw something like this:

```
$ dir(ss)
[...,
 'message',
 'stamp']
```

Let's look at what `message` is all about.

```
$ ss.message
'Property of Matt.'
```

#### Question:

Where did this come from?

It looks like what has happened is this:
  - When we *created* the `StringStamper` object, we supplied it with a message.
  - The resulting `StringStamper` object has stored the message internally.
  - We can access this stored message with a dot notation: `ss.message`.

This kind of *internal storage box* on an object is called an **attribute**.

#### Exercise: Two Objects

Look inside your two different string sampler objects.  Are the messages the same?  Are the messages stored independently?

#### Exercise: Changing an Attribute

Try to figure out how to *change the value of an attribute*, then verify that it has actually changed.

### Picking apart objects: methods

There's another attribute of the object, the `stamp` attribute.  This one is a bit special.  Instead of just storing data, it is actually a function.

```
$ ss.stamp("The Elements of Statistical Learning.")
'The Elements of Statistical Learning. Property of Matt.'
```

### Discussion: Ok, what just happened?

### Exercise: Using `stamp`

Call the `stamp` method on different strings.  What stays the same and what changes?

### Exercise: Changing Attributes Revisited

Change the `message` attribute of your `StringStamper` object a few times, and call `stamp` before and afterwards.  What stays the same and what has changed?

### Exercise: Explore Die Roller
Import the `DiceRoller` class

```
from diceroller import DiceRoller
```

Create some `DiceRoller`s and investigate their attributes and methods.  Call the methods on your dice roller objects.


## Classes

### The String Stamper Class

#### Exercise: Archaeology.
You know what the `StringStamper` class is supposed to do now.  Spend five minuets looking at the code for the `StringStamper` class.  Take notes on its curious features, and form some hypothesises about what the different parts do.
  
###  The `class` keyword

#### Exercise: Assignments in a Class
Create a new class with the `class` keyword, and assign to a variable within the body of the class.  Like this:

```
class MagicalMysteryTour:

    i_am = "Walrus"
```

Create some objects using your class.  What happened to the variable you created?  Can you change the value of this variable?  If you have multiple `MagicalMysterTour` objects, what happens if you change the variable you stored?

###  Constructing new objects: the `__init__` method

  - What data does this class need to store?
  - The `__init__` method, and the `self.thing = ...` pattern.
  - Attributes of an object are created in `__int__`
  - Attributes can be created any time

#### Exercise: Prefix and Suffix
Create a `PrefixAndSuffix` class that is like the `StringStamper`, but stamps *both* a prefix and suffix on the string.  For now

  1. Think about what data a `PrefixAndSuffixStamper` object needs to store.
  2. Write the `__init__` method to accept and store that data.
  3. Create some objects and verify that they work as intended.

Note that you do *not* yet have to create the `stamp` method, but if you think you can figure out how to do that, go for it.

###  `self` and self-reference

  - So what is this `self` thing.

###  Methods.

  - Methods are functions with a pinch of flavor.
  - How `self` is handled.

#### Exercise: Prefix and Suffix
Update your `PrefixAndSuffixStamper` class to include a method `stamp` which takes a string as input, and returns the string with the prefix and suffix appended.

#### Exercise: Coffee Cup
Make a `CoffeeCup` class, which can be used to make `CoffeeCup` objects.  The cup should have two states, full or not full.  Create a method `drink` which empties a full cup, and `fill` which fills an empty cup.

#### Exercise: Coffee Cup Revisited
Ok, maybe that was unreasonable, no one drinks a full cup of coffee in one drink.  Modify your `CoffeeCup` class to keep track of *how full* the coffee cup is.  Create a `sip` method which takes a small drink, a `gulp` method which takes a large drink, and a `pour_out` method which empties the cup (along with the `fill` method from before).

#### Exercise: Reverse Indexer
During our collections and iteration day, we wrote a function that reverse indexes a list.

```python
$ reverse_index([1, 2, 3, 4], 0)
4
$ reverse_index([1, 2, 3, 4], 3)
1
$ reverse_index([1, 2, 3, 4], 1)
3
```

We could just as well express this idea as a class.

```python
$ rev_list = ReverseList([1, 2, 3, 4])
$ rev_list.index(0)
4
$ rev_list.index(3)
1
$ rev_list.index(1)
3
```

Create this class.

#### Exercise: Reverse Slicer
We also wrote a function that reverse slices a list

```python
$ reverse_slice([1, 2, 3, 4], 0, 1)
[3, 4]
$ reverse_slice([1, 2, 3, 4], 0, 2)
[2, 3, 4]
$ reverse_slice([1, 2, 3, 4], 1, 2)
[2, 3]
```

Add a `slice` method to your `ReverseList` class that does the same.

##  Magic Methods

###  Magic Methods

  - What's so magic about magic methods.
  - What is a dunder and why do we care?

###  Pretty printing with `__repr__` and `__str__`

  - How custom objects are displayed by default is not very useful.
  - `__repr__` and how to use it.

#### Exercise: Repr StringStamper
Write a `__repr__` method for your `StringStamper` class.  You will find the `.format` method useful.

#### Exercise: Repr CoffeCup
Write a ``__repr__` for your coffee cup class.  Again, `.format` will be useful.

- `__repr__` vs. `__str__`, why both?

#### Exercise: Repr vs. String
Would you implement differnet behaviour for `__repr__` vs. `__str__` for either `CoffeeCup` or `StringStamper`?  Why or why not?

#### Exercise: ReverseList Repr and Str
Add `__repr__` 

###  Indexing with `__getitem__`

  - List or dictionary like behaviour with `__getitem__`.

#### Exercise:  ReverseList indexing. 
Write a `__getitem__` method for your `ReverseList` class.  Should you keep the `index` method from before, or replace it?

###  Setting with `__setitem__`

  - List or dictionary like behaviour with `__setitem__`.

#### Exercise: RevereSlist Setitem.
Write a `__setitem__` method for your `ReverseList` class.  Should the behaviour be consistent with `__getitem__`, or should it work just like a regular old list.

###  Arithmetic methods

  - `__add__` and `__sub__` methods for addition and subtraction.

#### Exercise: ReverseList Arithmetic
Write `__add__` and `__sub__` methods for your `ReverseList` class.  These should have the same result as using `+` and `-` on numpy lists.

###  All the others

  - There are many, many magic methods.  You will have to learn them over time.  A full list is [here](https://www.python-course.eu/python3_magic_methods.php): 
