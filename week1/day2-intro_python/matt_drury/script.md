# Introduction to Programming

## What is a Programming Language?

## Why Are There So Many Programming Languages?

## Why Do People Choose Python?

## What's It Like to Learn to Program?


# Introduction to Python


## Three Ways to Use Python

There are three popular ways to use python:

If we would like to use Python **interactively**, there are two options.

  - `ipython`: An interactive environment where you can type short pieces of python code which immediately get executed.  This is useful for quick exploratory experiments.
  - `jupyter notebook`: An interactive environment that runs in a web-browser.  This is more permanent than using `ipython`.  Notebooks are very popular in the scientific community, as they allow embedding images and text.

If we would like to **compose a longer program**, the workflow is different.  We use a **text editor** to compose files containing python code.  The files are always named like `name_of_file.py`, and they can be **run** with the command:

```
python name_of_file.py
```

I'll show some examples in the future.

Today I'll be using `ipython`, since most of our work will be exploratory.


## Numeric Data Types

Programming languages are primarily tools for doing **computation**.  Our meaning of the word "computation" will expand over time, it definitely means something very different to an experienced programmer compared to, say, a high school student.

To begin, we will discuss how to use python as a glorified calculator (it makes a really god one, and once you know a bit of python there is really no reason to every buy an actual calculator again).

### The Two Numeric Data Types

Python knows about both integer and decimal numbers.  These are two two primary types of numeric data in python.

This is an integer:

```
In [1]: 2
Out[1]: 2
```

That's a pretty silly action.  I entered the number `2` to python, and it spit it back to me.  Here's something a bit more interesting:

```
In [2]: 2 + 3
Out[2]: 5
```

I'm using python interactively here.  I typed in an **expression**, and python **evaluated it** and then informed me of the resulting value.

We can also do this with decimals:

```
In [3]: 2.0 + 3.0
Out[3]: 5.0
```

This is a different type of number to python.  Notice that when I added two *integer* numbers, the result was an integer, and when I added two *decimal* numbers the result was a decimal.

**Note:** In the context of programming decimal numbers are often called **floating point numbers**, or **floats**.  There is a technical reason this is done, but it's not important for now.

**Note:** There are some other numeric data types supported by python (complex numbers for example), but they are not worth worrying about at the moment.

### Arithmetic

There are many arithmetic operations supported by python.

```
In [4]: 2 - 3
Out[4]: -1

In [5]: 2 * 3
Out[5]: 6

In [6]: 2 / 3
Out[6]: 0.6666666666666666
```

The two are pretty clear, but the third is a bit more interesting.  Even though we divided two *integers* we got back a *decimal*.  This is in contrast to the other two examples, where we got back the same type of numbers as we put in.

We may suspect that if the division comes out evenly, they python will give us an integer, but this is not the case:

```
In [7]: 4/2
Out[7]: 2.0
```

### Exponentiation

There are two more arithmetic operations that are encountered more rarely.  **Exponentiation** is spelled with two stars `**`:

```
In [8]: 2**4
Out[8]: 16

In [9]: 2**0.5
Out[9]: 1.4142135623730951
```

Exponentiation can result in some massive numbers, but python handles them just fine:

```
In [10]: 2**100
Out[10]: 1267650600228229401496703205376

In [11]: 2**250
Out[11]: 1809251394333065553493296640760748560207343510400633813116524750123642650624

In [12]: 2**1000
Out[12]: 10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
```

There's an interesting quirk to this large number thing though:

```
In [13]: 2.0**1000
Out[13]: 1.0715086071862673e+301
```

While integers can have as many digits as needed, **decimals cannot, you only get (about) seventeen decimal digits to work with**.  So if you end up with really large decimal number, some of the digits will get truncated.  There is not much you can do about this, it's a pretty fundamental quirk of programming languages.

### Modular Division

The final arithmetic operation is called **modular division**.  This sounds gnarly, but it's actually really simple.

```
In [15]: 10 % 2
Out[15]: 0

In [16]: 10 % 3
Out[16]: 1

In [17]: 10 % 4
Out[17]: 2

In [18]: 10 % 5
Out[18]: 0
```

The `%` operator does division, but returns the **remainder** of the division (instead of the quotient).  This is a lot more useful than you may guess if you are not an experienced programmer, it allows for the clean solution to a surprising number of problems.

### Organization

If you end up with more complex mathematical expressions, you can use parentheses to organize them:

```
In [14]: (2 + 3) * ((15 - 6)**2 - (14 + 2)**2) + 5
Out[14]: -870
```

This works just like it should: the innermost parentheses are evaluated first, and then python works outwards.

### Review:

Here's a quick summary of what we learned.

  - Python is a damn good calculator.
  - There are two types of numeric data commonly used in python: **integers** and **Decimals**.
  - Doing arithmetic on numbers generally gives back the same type of number, except for division, which always gives back a decimal!
  - To organize work, you can use parentheses.


## Giving Things Names




## The Logical Data Type (Booleans)

### Using Comparisons to Create Booleans

### If Statements (Conditionals)

### The First Assignment Question.

```
Write a script that takes a user inputted number and prints whether it is positive, negative or zero, with "The inputted number is (positive/negative/zero)" depending.
```

### While Loops
