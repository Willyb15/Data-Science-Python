# Magic Methods and Interfaces
  
  - Magic Methods
  - Pretty printing with `__repr__` and `__str__`
  - Indexing with `__getitem__`
  - Setting with `__setitem__`
  - Arithmetic methods
  - Comparison methods

## You Can Add Multiple Things

Consider an example that may or may not have been mysterious until now: in python, the `+` operation can mean multiple things:

```python
$ 2 + 5
7

$ 'Matt' + ' ' + 'Drury'
'Matt Drury'

$ ['apples', 'oranges'] + ['bananas', 'tomatoes']
['apples', 'oranges', 'bananas', 'tomatoes']
```

We used the same symbol `+` to operate on many different data types.  In each different situation, a different thing happened:

  - When we used `+` on numbers, we did standard arithemetic.
  - When we used `+` on strings, we concatinated.
  - When we used `+` on lists, we extended the lists.

#### Question: What Else?

What other types of things does it make sense to add?

#### Questions To Answer...

So, a couple questions arise:

  - How does python know what to do with each different use of the `+` symbol?
  - How can we create objects that know how to use the `+` symbol?

The answer to these questions are found in python's concept of **magic methods**.


##  Magic Methods

**Magic methods** are a special notation in python that can be used to add natural behaviour to classes.  For example, we can use magic methods to:

  - Allow our custom objects to be added.

###  Magic Methods

  - What's so magic about magic methods.
  - What is a dunder and why do we care?

### Making a Dictionary like Obejct


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
