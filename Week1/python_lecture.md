## Introduction to Python

### Numeric Variable Types
Today we are going to learn about base numeric variable types in Python. And learn how to write scripts (programs) that can compute useful things.

There are a number of base numeric variable types built into Python. The ones that we will be looking at today are ints, short for integers, floats, these are floating point decimal numbers, and complex, containing real and imaginary parts stored as floats.

Lets experiment with using these types in the ipython. In the console. Type the number 7 and hit enter. You should see something like this.

```python
In [1]: 7
Out[1]: 7
```

The ipython console will accept arbitrary python commands, entered after the `In [#]:`, and execute them, handing you back the results of the computation, displayed after the `Out [#]:`.

You can test this out with other numbers, try one with a decimal and one by passing two numbers to the `complex()` constructor (we will talk about what these things are later).

```python
In [1]: 7.5
Out[1]: 7.5

In [2]: complex(3, 4)
Out[2]: (3+4j)
```

One thing that is important about Python is that it is a duck typed language. What does this mean? The name duck comes from the classic "If it walks like a duck, and quacks like a duck, then it must be a duck" adage. As applied to our situation, it simply means that Python will determine what it thinks is the best type to call a variable when you use it, unless explicitly told otherwise.

To inspect what type python thinks a number (or anything else is), you can pass it to the `type()` function. Lets see what we get out when we pass numbers of various types to this function.

```python
In [1]: type(7)
Out[1]: int

In [2]: type(7.5)
Out[2]: float

In [3]: type(complex(3, 4))
Out[3]: complex
```

As you can see, python assumes that a number with no decimal point is an int, those with a decimal point, a float, and (surprise!) those from the `complex()` constructor as complex. 

While, very frequently, these subtle differences wont matter too much, there are, however, plenty of occasions where Python hiding this implementation detail will make you think that something will work, when really it wont. So making sure you know how to check is very important.

### Numeric Operations

At its base level Python is really just a really awesome calculator that can do way more stuff than addition and subtraction. But let's focus on that functionality for now.

All of the simple operations that you think should be available are. Addition, subtraction, multiplication, division and exponentiation are all accessible via `+`, `-`, `*`, `/` and `**`, respectively.

```python
In [1]: 7 + 8
Out[1]: 15

In [2]: 7 - 8
Out[2]: -1

In [3]: 7 * 8
Out[3]: 56

In [4]: 7 / 8
Out[4]: 0

In [5]: 7 ** 8
Out[5]: 5764801
```

All of these operations output exactly what we think they would, except one. The fourth one, where we divided 7 by 8 gave us 0, even though we know that it should be 0.875. This happened because the input on both sides of the `/` were integers, so Python decided to cast the output as an integer. Let's visit all aspects of this problem.

```python
n [1]: 7 / 8
Out[1]: 0

In [2]: 7 / 8.0
Out[2]: 0.875

In [3]: 7 / 8.
Out[3]: 0.875

In [4]: int(7 / 8.)
Out[4]: 0

In [5]: 7 // 8.
Out[5]: 0.0
```

Notice that once we made one of the numbers in the operation a float python realized that it should return a float from the operation, and we got 0.875 as expected. This exact same procedure was followed the third time, but the trailing 0 on the float version of 8 was left off. Python doesn't need to see anything following the decimal point to know it should be interpreting the number as a float, so long as the "." is there. Similarly, we can manually cast the output of the 3rd operation as an integer, by passing the result directly to the `int()` constructor. Manually casting in this way can be very useful when Python is interpreting things differently than you would like it to. The last operation that we performed is called floor division, `//`. Really all it does is perform division and truncate the result. So, where `7 / 8.` gave us `0.875`, `7 // 8.` cuts off after the `0.` giving us `0.0`.

The last operation that we will go over is the modular division, `%` operator. This operation is the sibling to the `/`. Where `71 / 7` gives us the integer number of times that 7 goes into 71, 10; `71 % 7` gives us the remainder from that integer division, 1.

### Logic

Now that we have a thorough understanding of base numeric types and how to play with them in Python, lets keep building our tools so that we can use them to keep track of the state of our program.

The most simple way to check on the state of your Python program is with an `if` statement. From a high level, an if statement allows us to check whether or not a certain condition is true, and if it is gives us the opportunity to perform operations specific to that situation.

For example, say we're asked to write a program that takes a bunch of numbers and gives back to us those that are even. We would need write an if statement that identifies whether or not a number is even (we'll talk about how to do this), and check all the numbers giving back those that meet the even condition. This is a program that will be entirely within our ability to implement at the end of next week; for now though, lets focus on the if statement.

The general syntax of an if statement in Python is:

```python
if condition:
    if_block_statement
```

Let's tackle this one part at a time. What does it mean to be a condition? Really all an if is checking is for weather the condition is `True` or `False`. If it is true, then the body of the if statement is executed. If it is false, the if block is skipped. Intuitively, true and false are concepts that make perfect sense to us. But we should take the time to clearly define them in a programming context here.

True and False are what we call booleans in logic, bools for short and what python calls them. They are a special variable type with many potential uses; but mainly they are used as a way to put a label on the, capital T, truth of a statement. There are two specifically reserved words for bools in Python, `True` and `False`.

```python
In [1]: type(True)
Out[1]: bool

In [2]: type(False)
Out[2]: bool
```

In addition, a wide variety of statements an evaluate to bools. The ones that we will focus on today are the equalities, _equal to_ and _not equal to_, and the inequalities, _less than_, _greater than_, _less than or equal to_ and _greater than or equal to_. These comparisions are available in python via the `==`, `!=`, `<`, `>`, `<=` and `>=`, respectively.
