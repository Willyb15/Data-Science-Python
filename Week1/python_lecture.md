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

There are of course cases where using less than descript variable names follows convention and is therefore just fine to use. One that comes to mind `i`. Frequently it is used to keep track of an `i`ndex (we will cover this idea next week, but it wouldn't be surprising if you understood the concept already), and because if it's prevalent usage for this purpose it is usually easy to understand what is happening in that context. But the important thing is that the code is **understandable**.

Note that we saw no output from the first command above. This is because return value that would been printed to the console for output were assigned to the variable x. This is why we had to view it in the next line with a simple call to `x`.

A large part of the power of variables is the fact that they can change. This allows us to use a single variable name to keep track of a single thing throughout the life a program. The exact same syntax can be used to change the value stored in the variable. 

Say we want to add 5 to `x` from the previous code example and store it in x.

```python
In [1]: x = x + 5

In [2]: x
Out[2]: 6
```

Notice how the first line is formatted. Python knows that the `=` means variable assignment, so when it sees the first line it evaluates the right side of the equals and then puts that value in `x` even though `x` was part of the first calculation.

Changing variables in this way occurs so commonly that there is built-in shorthand for it. The result of the first line could have been achieved with `x += 5`. This *syntatic sugar* is available for all the simple operations `+`, `-`, `*`, `/` and `**` that we covered earlier.

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

In addition, a wide variety of statements an evaluate to bools. The ones that we will focus on today are the equalities, *equal to* and *not equal to*, and the inequalities, *less than*, *greater than*, *less than or equal to* and *greater than or equal to*. These comparisions are available in python via the `==`, `!=`, `<`, `>`, `<=` and `>=`, respectively.

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

#### Using the If

Now that we understand conditionals lets talk about how we can use them with variables to create a powerful construct in which to make dynamic programs. Consider the following code block.

```python
if x > 5:
    x += 10
print(x)
```

*Note, the print function simply pipes the value passed to it to the console.*

In the above code we don't need to know what the value of `x` is, but we can say that if it's greater than 5 it will come out of the code block 10 greater than before the if statement.

From what we know so far, this functionality isn't super useful. So lets quickly go over a way that that we can make out Python more flexible. Until now, we've had to hard code any variable or value that we want to use in our program. Python has a built in way to accept input from a user of a program. Lets examine this now, consider that the following code was stored in a file named `print_number.py`.

```python
x = raw_input('Please enter a number: ')
print(x) 
```

If we then ran the script from ipython. We would would see:

```python
In [1]: run print_number.py
Please enter a number: 
```

*Note, the raw_input() function accepts character input from the keyboard, printing the message it is passed as a prompt.*

We can then type a number followed by enter, and the script will print that number.

```python
In [1]: run print_number.py
Please enter a number: 3
3
```

*Note, raw_input() halts the execution of your script, so nothing will happen until you type something a press enter.*

Now that we have a way to get arbitrary input from a user of our program, we can begin to see the full power of the if. Let's combine the last two code blocks from above, and say we stored it in a script named `print_number_with_if.py`.

```python
x = int(raw_input('Please enter a number: '))
if x > 5:
    x += 10
print(x)
```

*Note, raw_input() actually interprets the input as strings, so we have to manually tell Python to treat the number we pass as an interger with int(). We'll talk about strings more next week.*

If we then ran the script from ipython as above, lets look at two ways we could interact with it.

```python
In [1]: run print_number_with_if.py
Please enter a number: 3
3

In [2]: run print_number_with_if.py
Please enter a number: 8
18
```

Notice how during the first time we run `print_number_with_if` and give it 3, it acts just like `print_number`. However, the second time, when we give it 8, it adds 10 and prints 18. Why did it do this? Because 8 is greater than 5 so our program added 10 to it before it was printed.

This may seem like a trivial example, and therefore not very exciting; but let me assure you, what you have just learned is amazingly powerful! So congratulations!

#### Building on the If

Ok, so, the if is cool. But it seems like, due to it's structure, there are only so many things you can do with it. Lets summarize this with what's known as a flow diagram.

![If Flow](http://www.tutorialspoint.com/cprogramming/images/if_statement.jpg)

You can see that there are two branches created by the if statement, one when the condition is true in which case the conditional code is executed, and the other when it is false, in which case the if block is ignored. But what if we wanted to check more than one thing, have more than two branches?

Python allows for two ways for us to do this. One by offering other conditionals, `elif` and `else`; and the other by allowing us to combine conditions with logical `and`, `or` and `not`.

##### Elif and Else

In addition to the if Python provides us with two other statements to build out those logical trees, the elif and the else. The elif is just like the if, it accepts a condition to check the truth of and has an indented code block that is executed when that condition evaluates to True. The else is similar, but it doesn't accept a condition; instead it mainly acts as a catch all for any other situation that you don't need to cover with your ifs and elifs. Note, there can only be a single if and up to a single else, but any number of elifs in an if-elif-else block. Lets take a closer look at this in the following code block that we'll store in `if_elif_else.py`.

```python
x = int(input('Please enter a number: '))
if x < 0:
    print('You entered a negative number.')
elif x > 0:
    print('You entered a positive number.')
else:
    print('You entered the number 0.')
```

Running the program and passing a number when prompted will cause the conditions to be checked and result in easily guessed output.

```python
In [1]: run if_elif_else.py
Please enter a number: 10
You entered a positive number.

In [2]: run if_elif_else.py
Please enter a number: -10
You entered a negative number.

In [3]: run if_elif_else.py
Please enter a number: 0
You entered the number 0.
```

Lets specifically talk about how the if-elif-else statements work. The programmers of Python designed these statements so that they would execute highly efficiently. They achieved this by making it so that which Python is going through your if-elif-else statements when it encounters a condition that evaluates to True it will execute the corresponding conditional code block and then skip to the line directly following the last conditional block in the. Lets examine this in the following code saved again in `if_elif_else.py`.

```python
x = int(input('Please enter a number: '))
if x > 5:
    print('You entered a number bigger than 5.')
elif x > 0:
    print('You entered a positive number.')
elif x < 0:
    print('You entered a negative number.')
else:
    print('You entered the number 0.')
```

Running this program produces slightly unexpected results. But they will soon make perfect sense and knowing what is going on will allow you full control over how you control the flow of your programs.

```python
In [1]: run if_elif_else.py
Please enter a number: 5
You entered a positive number.

In [2]: run if_elif_else.py
Please enter a number: 6
You entered a number bigger than 5.
```

In the first example we got something unsurprising. The only condition that evaluates to true when x is 5 is the second one. However, the second example yields only 'You entered a number bigger than 5.' Even though 6 is greater than 0. This shows that only one of the conditional block in an if-elif-else statement will ever be evaluated, and once this happens the rest are skipped.

*Note, the else part of the statement is actually optional. If it is not included then we'd notice that at most one of the conditional blocks in an if-else statement will be evaluated.*

##### And, Or and Not

There are plenty of times when we want execute some specific code when more than one condition is true. Check out the following code snippet.

```python
if x > 5:
    if x < 10:
        print(x)
```

We can see that what this *nested* if statement is checking for are numbers that lie in the interval (5, 10), if it finds one it prints it. We can intuitively guess that there is a better way to check for this condition. And there is!!!

Python gives us full access to what are known as boolean operations. The ones that we will use most often are and, or and not. Both the `and` and `or` take two conditions as inputs while the not affects only a single condition. They all return a single boolean with the and requiring both conditions to be True to return True; the or requiring only one of the conditions to be True to return True; and the not switching the truth on the input condition. These operations are derived from formal logic with a full discussion of their intricacies found [here](https://en.wikipedia.org/wiki/Truth_table).

What this means is that we now have a natural way to combine conditions. The previous nested if statement can now be written as a simple `if x > 5 and x < 10`. We can also chain other interesting conditionals together.

```python
if x > 10 or x < 5:
    print(x)

if not (x > 10 and x < 5):
    print(x)
```

Notice how the first if in the above code snippet uses an or, printing x if it is greater than 10 or less than 5. Inherently this statement is also saying that it will print x if x is not less than 10 and greater than 5 which is expressed in the second if statement. This illustrates an important point, that there is always more than one way to accomplish the same thing in programming.
