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

#### Types

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

### Variables

One of the most powerful constructs in programming is the ability to store arbitrary values in what we call variables. You can think of variable assignment as giving a name to something so that it can be accessed later by different parts of your program.

In Python variable assignment occurs with the `=` operation. So to assign a value to a variable name, declare it, you simply put the variable name on the left side of the `=` and the value you want to associate with that name on the right hand side. Now that this has happened, you can access the value in the variable simply by using it's name somewhere later in your code or ipython session.

```python
In [1]: x = 1

In [2]: x
Out[2]: 1

In [3]: x + 1
Out[3]: 2
```

The name you can give a variable can technically be any contiguous set of character, but there are some conventions followed in Python and programming in general. Python follows a variable naming convention called snake case. To write something in snake case simply use a `_` anywhere you would use a space and make sure every word is lower case. e.g. `this_is_variable`. Giving variables good names makes your code more readable and therefore maintainable. There is a big difference between seeing a variable called `degrees` and one called `y`. You should strive to give your variables good succinct names.

There are of course cases where using less than descript variable names follows convention and is therefore just fine to use. One that comes to mind `i`. Frequently it is used to keep track of an `i`ndex (we will cover this idea next week, but it wouldn't be surprising if you understood the concept already), and because if it's prevalent usage for this purpose it is usually easy to understand what is happening in that context. But the important thing is that the code is _understandable_.

Note that we saw no output from the first command above. This is because return value that would been printed to the console for output were assigned to the variable x. This is why we had to view it in the next line with a simple call to `x`.

A large part of the power of variables is the fact that they can change. This allows us to use a single variable name to keep track of a single thing throughout the life a program. The exact same syntax can be used to change the value stored in the variable. 

Say we want to add 5 to `x` from the previous code example and store it in x.

```python
In [1]: x = x + 5

In [2]: x
Out[2]: 6
```

Notice how the first line is formatted. Python knows that the `=` means variable assignment, so when it sees the first line it evaluates the right side of the equals and then puts that value in `x` even though `x` was part of the first calculation.

Changing variables in this way occurs so commonly that there is built-in shorthand for it. The result of the first line could have been achieved with `x += 5`. This _syntatic sugar_ is available for all the simple operations `+`, `-`, `*`, `/` and `**` that we covered earlier.

### Logic

Now that we have a thorough understanding of base numeric types and how to play with them and store them in Python, lets keep building our tools so that we can use them to keep track of the state of our program.

The most simple way to check on the state of your Python program is with an `if` statement. From a high level, an if statement allows us to check whether or not a certain condition is true, and if it is gives us the opportunity to perform operations specific to that situation.

For example, say we're asked to write a program that takes a bunch of numbers and gives back to us those that are even. We would need write an if statement that identifies whether or not a number is even (we'll talk about how to do this), and check all the numbers giving back those that meet the even condition. This is a program that will be entirely within our ability to implement at the end of next week; for now though, lets focus on the if statement.

The general syntax of an if statement in Python is:

```python
if conditional:
    if_block_statement
```

Notice how the if statement ends in a colon `:`. This is the way that Python declares the start of an indentation block. The function of indentation blocks manifest themselves in many different ways, for now know that they mark a section of code that is run under specific circumstances.

#### Conditionals

Let's tackle this one part at a time. What does it mean to be a condition? Really all an if is checking is for weather the conditional evaluates to `True` or `False`. If it is true, then the body of the if statement is executed. If it is false, the if block is skipped. Intuitively, true and false are concepts that make perfect sense to us. But we should take the time to clearly define them in a programming context here.

True and False are what we call booleans in logic, bools for short and what python calls them. They are a special variable type with many potential uses; but mainly they are used as a way to put a label on the, capital T, truth of a statement. There are two specifically reserved words for bools in Python, `True` and `False`.

```python
In [1]: type(True)
Out[1]: bool

In [2]: type(False)
Out[2]: bool
```

In addition, a wide variety of statements an evaluate to bools. The ones that we will focus on today are the equalities, _equal to_ and _not equal to_, and the inequalities, _less than_, _greater than_, _less than or equal to_ and _greater than or equal to_. These comparisions are available in python via the `==`, `!=`, `<`, `>`, `<=` and `>=`, respectively.

```python
In [1]: 1 == 2
Out[1]: False

In [2]: 1 != 2
Out[2]: True

In [3]: 1 < 2
Out[3]: True

In [4]: 1 > 2
Out[4]: False

In [5]: 1 <= 2
Out[5]: True

In [6]: 1 >= 2
Out[6]: False
```

#### Building on the If

Now that we understand conditionals we can gain a full understanding of what we can do with if statements. 
