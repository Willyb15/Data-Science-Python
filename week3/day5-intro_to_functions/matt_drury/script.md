Python Fundamentals: Functions
==============================

Today we will be learning about one of the most central and important topics in programming: **Functions**.

Functions supply is with many beneficial properties for our programs:

  - They allow us to re-use code we have written and checked for correctness for other purposes.
  - They allow us to give operations and computations names.
  - They allow us to *encapsulate* computations.  This means that the consumer of our code may use our computations, and obtain results, without actually needing to know the details of how the computations work. 

## Functions in Python

Creating functions in python requires us to understand four main components:

  - The `def` keyword tells python we are defining a function, and allows us to give it a name.
  - The **parameters** of the function allow us to input data into our calculation.
  - The **body** of our function is the code that actually performs a calculation.
  - The `return` statement specifies the **result** of our computation.

#### Example: Is a Number Even

Let's write a function with the following properties:

  - The name of the function is `is_even`.
  - The function has one **parameter**.  Let's call it `n`.
  - In the body of the function, we determine whether `n` is an even number.
  - We return `True` if `n` is an even number, and return `False` if not.

```python
def is_even(n):
    if n % 2 == 0:
        return True
    else
        return False
```

## Defining vs. Calling a Function.

There are two main things you do with functions, first you **define** them, and then you **call** them.

  - When you **define** a function you use `def` and actually write the code that does the thing the function is intended to do.
  - When you **call** a function, you are asking an **already defined** function to do it's thing for you.

So, it's very important to realize that **a function must first be defined before it is called!**.

### Defining a Function

```python
def is_even(n):
    if n % 2 == 0:
        return True
    else
        return False
```

### Calling a Function

```python
$ is_even(2)
True
$ is_even(3)
False
```

Here are some notes on calling vs. defining a function.

  - When you **define** a function, the things that go into the function are called **parameters**.  When you **call** a function, the things that go in are called **arguments**.

```python
def is_even(n):
            ^
	    | This is a parameter, we are defining the function!

is_even(2)
        ^
	| This is an argument, we are calling the function!
```

  - The person that defines a function does not have to be the same as the person that calls it!  You can define a function, pass it off to a co-worker, and they can use it in their work without getting into the weeds of how you coded it.  This is called **encapsulation** (or **abstraction**, depending on who you ask)!

#### Example: Is a Number Odd

See if you can modify the above function to check if a number is odd.

#### Example: Get First Letter

Write a function with the following properties
  - The name of the function is `get_first_letter`.
  - The function has one **parameter**.  Let's call it `string`.
  - In the body of the function, we get the first letter in the string.
  - We return the first letter in the string.

#### Example: Get n'th Letter

Ok.  Let's *generalize* the function from the last example.  Instead of always getting the fist letter, let's:

  - Have our function take **two parameters**, `string` and `n`.
  - Return the `n`'th character of the string.

Our `def` should look like this:

```python
def get_nth_letter(string, n):
   ...
```

### Default Values


Sometimes we want some of our parameters to be unnecessary.  The person who calls the function (often called the **caller**) may specify them, but if they do not, they assume some sensible default value.

#### Discussion: Default Values.

Give some examples of situations where a default value is appropriate for an argument in a function.

#### Example: Get n'th Letter with a Default

Modify the `get_nth_letter` function so that supplying `n` is optional (when calling the function).  If the caller does not supply n, assume a default value of zero.

## Practice with Functions

The only way to get better at writing functions is to practice!

#### Exercise: Doubling a List
Write a function `double_elements` which takes a numeric list, and returns a new list of the same length where all the elements are doubled.

```python
$ double_elements([0, 1, 2, 3])
[0, 2, 4, 6]
```

#### Exercise: Get Evens
Write a function `get_evens` that takes a numeric list, then creates a new list containing only the even numbers in the original list.

#### Exercise: Multiply List By
Write a function `multiply_list_by` which takes a numeric list and a number, and returns a new list of the same length where all the elements are multiplied by that number.

#### Exercise: Dictionary Reversal
Write a function `reverse_dictionary` that swaps the roles of keys and values in a dictionary.

```python
$ reverse_dictionary({'a': 1, 'b': 2, 'c': 3})
{1: 'a', 2: 'b', 3: 'c'}
```

#### Exercise: Searching for a Number
Write a function that returns the first number in a list that is divisible by a given number:

```python
$ search_for_divisibility([2, 4, 6, 8, 10, 12, 12, 10, 8], by=3)
6
$ search_for_divisibility([2, 4, 6, 8, 10, 12, 12, 10, 8], by=5)
10
```

### The Builder Pattern and List Comprehensions

Let's look at one possible implementation of `get_evens`

```python
def get_evens(lst):
    evens = []
    for n in lst:
        if n % 2 == 0:
	    evens.append(n)
    return evens
```

This implementation uses a common pattern, then **builder pattern**

  - Initialize an empty collection.
  - Loop over something.
  - Make some calculation for each element in the thing being looped over.
  - Append the result to the initially empty collection.
  - Return the result.

We call this the builder pattern because we "built up" the resulting return value from an initially empty state.

The builder pattern is very, very common, so Python contains a very convenient shorthand for the builder pattern, **comprehensions**.

```python
def get_evens(lst):
    return [n for n in lst if n % 2 == 0]
```

This is called a **list comprehension**.  It builds up the result list in one go with no fuss.  After you get used to them, list comprehensions provide a very simple way to conveniently express a very common code pattern.

#### Example: Get Multiples
Create a function `get_multiples(lst, divisor)` that takes a numeric list, and a divisor, and returns a list made up of all the elements of the original list that are evenly divisible by the divisor.  Write one version using the builder pattern, and then another with a list comprehension.

```python
$ get_multiples([0, 1, 2, 3, 4, 5, 6], 2)
[0, 2, 4, 6]
$ get_multiples([0, 1, 2, 3, 4, 5, 6], 3)
[0, 3, 6]
```

### The "return True" Anti-pattern

Let's look at a possible implementation of `is_odd`.

```python
def is_odd(n):
    if n % 2 == 1:
        return True
    else:
        return False
```

This is an example of an anti-pattern (a code pattern that people don't like), in this case, its the **return True** anti-pattern.

Look at what we've done; we have a condition `n % 2 == 1`, and when that condition is `True` we return `True`, otherwise the condition must be `False`, and we return `False`.  In both cases we are just returning whatever the condition happened to be, so we may as well have just returned the value of the condition:

```python
def is_odd(n):
    return n % 2 == 1
```

For now, it's fine to use the `return True` style in your code (as long as you are resilient to the scoffing of more experienced programmers).  But you will want to be able to recognise the second style, since it is very common in experienced programmer's code.

### Why We Need `return`

It is very common for new programmers to wonder why we need `return` when we have `print`.  The next example will walk you though why `return` is much, much more useful than `print`.

#### Example: Get Valid Passwords
Suppose that, for a certain application, that a valid password must satisfy these two constraints:

  - The password must contain a digit (zero through nine)
  - The password must contain one of the symbols `^!#$?-`

Let's build a valid password filterer, which will take a list of candidate passwords, and return a list with only the valid ones:

```python
$ possible_passwords = ['moshi', 'm0shi', 'mosh!', 'm0sh!',
                        '^^oshi', '^^0shi', '^^0sh!']
$ get_valid_passwords(possible_passwords)
['m0sh!', '^^0shi', '^^0sh!']
```

We could do this all in one go, but let's try to break down the problem:

1. Write two functions, `contains_digit` and `contains_symbol` that check whether a **single string** contains either a digit / one of the specified symbols.

```python
$ contains_digit('mosh!')
False
$ contains_symbol('mosh!')
True
```

2. Write a function `get_containing_digit` that filters the list to the candidate passwords containing digits.

```python
$ get_containing_digit(possible_passwords)
['m0shi', 'm0sh!', '^^0shi', '^^0sh!']
```

3. Write a function `get_containing_symbol` that filters the list to the candidate passwords containing symbols.

```python
$ get_containing_symbol(possible_passwords)
['mosh!', 'm0sh!', '^^0shi', '^^0sh!']
```

4. Write `get_valid_passwords`.  This should be a **dead simple function**.  Instead of writing a bunch of code, use the `get_containing_digit` and `get_containing_symbol` functions you already have!

This is the point.  Functions transform data into new data.  You can pass the data that comes out of one function into another function, and create pipelines that do simple, understandable things, and get you closer yo your goal.  We will discuss this more next time.

### Documentation Strings

The last important note about functions is not about writing them, or calling them, but making them understandable.  The *best* thing you can do to help with this is write clear, concise code with descriptive names.

The *next best* thing you can do is write a *documentation string* for all your functions.  Here's an example:

```
def get_valid_passwords(possible_passwords)
    """Process a list if password strings and filter out invalid passwords.

    A valid password has the following two properties:
    
      - The password must contain a digit (zero through nine)
      - The password must contain one of the symbols `^!#$?-`
    
    Example
    -------
    $ possible_passwords = ['moshi', 'm0shi', 'mosh!', 'm0sh!',
                            '^^oshi', '^^0shi', '^^0sh!']
    $ get_valid_passwords(possible_passwords)
    ['m0sh!', '^^0shi', '^^0sh!']

    Arguments
    ---------
    possible_passwords: list of strings
      A list of passwords to check for validity.

    Returns
    -------
    valid_passwords: list of strings
      The sublist of possible_passwords containing exactly the valid passwords.
    """
```

It takes some investment of time to write function docstrings, but it is a wise investment.  You should write docstrings for all functions in your programs that you mean to be public facing (i.e. you mean to be called by humans, or other modules in your program).
