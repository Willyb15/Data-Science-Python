## Introduction to Strings and Lists

### Strings
Today we are going to learn about another pretty common varaible type, strings. From a high-level perspective, a string is just a bit of text. This could be text that you have read in from a file, html that you pulled from the internet, or any other text. From Python's perspective, a string (type `str`) is simply a collection of encoded characters. Wait, what's an encoding...?

An encoding is just a fancy way of us saying that the characters in our string follow a certain format, or structure. The reason it matters for us in terms of our Python programs, though, is that Python expects that our strings are in one of a couple of different encodings (either ASCII, utf-8, or unicode). This isn't something you will run into often, and especially not when defining your own strings (it's probably most prevelant when pulling text from the Internet). However, it's worth noting because there is a good chance that sometime in your Python career, you will end up with Python telling you it doesn't recognize a certain character in one of your strings, and an unexpected encoding will most likely be at the heart of that error. 

In Python, strings are recognized as a collection of characters surrounded by a set of either single quotation marks (`''`) or double quotation marks (`""`). So long as you open and close your string with a **matching** set of single or double quotation marks, you are free to use either. The single caveat to that is that if you are writing an expression with a single quotation mark in it (such as "Don't do that"), you have to use a matching set of **double** quotation marks. Let's experiment with some strings in the IPython console...

```python 
In [1]: 'This is a string.'
Out [1]: 'This is a string.'

In [2]: "This is another string, but this time with double quotation marks."
Out [2]: 'This is another string, but this time with double quotation marks.'

In [3]: 'They told me not to do this, but I didn't listen.'

SyntaxError: invalid syntax
```

Just like we expected, we can use both single and double quotation marks. But what happend in the 3rd case there? Well, we opened the string with a single quotation mark, and Python started looking for the next single quotation mark to close your string. When it found that quotation mark in the word `didn't`, it assumed the string was closed after `didn`. As a result, this left `t listen.'` just hanging out, and Python didn't know how to interpret that, resulting in our error. The solution to this, as mentioned above, is to use double quotation marks in any case where your text will have single quotation marks in it. For example...

```python 
In [1]: "Now that I've got double quotes, I can use all the contractions!"
Out [1]: "Now that I've got double quotes, I can use all the contractions!"

In [2]: "Can't, won't, didn't, don't... all the contractions!"
Out [2]: "Can't, won't, didn't, don't... all the contractions!"
```
As a final note before we dive into string operations, note we can store them in variables in the exact same way that we can store an `int`, `float`, or `complex`. 

```python
In [1]: my_str_variable = 'This is a string variable.'

In [2]: my_str_variable
Out [2]: 'This is a string variable.'
```

### String Operations

Suprisingly, a couple of our standard mathematical operations will work on strings, namely `+` and `*`. We can use the `+` operator to add two strings together (this is know as string **concatenation**), and we can use the `*` operator to repeat a string a given number of times. Let's take a look... 

```python 
In [1]: 'My first string' + 'My second string'
Out [1]: 'My first stringMy second string'

In [2]: 'Repeating string' * 3
Out [2]: 'Repeating stringRepeating stringRepeating string'
```

Note that it didn't put spaces between my strings when I used the `+` operator or the `*` operator. Why not, you ask? Because we didn't tell it to! In this case, and in programming in general, we have to be extremely explicit about what we want the computer to do. To fix this, we can add a space in the middle of the first case, and then add a space to the end of our string in the second case.

```python 
In [1]: 'My first string' + ' ' + 'My second string'
Out [1]: 'My first string My second string'

In [2]: 'Repeating string ' * 3
Out [2]: 'Repeating string Repeating string Repeating string '
```

Much better! But, what about that pesky little space at the end of our second string: `'Repeating string Repeating string Repeating string '`. Is there a way to remove this? It turns out there is! One of the methods (a name for a function that is attached to a particular object) that we can call on strings is the `strip()` method. Methods are something that we will cover in much more depth later, but for now just note that we call them on our objects through **dot notation**. We simply place a `.` at the end of our object (`str`, `int`, `float`, any variable, etc.), and then call the method like we would call a function. Check this out. 

```python 
In [1]: 'Repeating string Repeating string Repeating string '.strip()
Out [2]: 'Repeating string Repeating string Repeating string'

In [1]: ' Repeating string Repeating string Repeating string '.strip()
Out [2]: 'Repeating string Repeating string Repeating string'
```

So what did the `strip()` method do? In the first example, it removed the trailing space from our string. In the second example, it removed both the leading and trailing spaces. In fact this is exactly what the `strip()` method does - by default (without any arguments) it removes leading and trailing whitespaces. 

Are there other things that we can do with strings? There are tons! I'm going to store our string in a variable below, just so we can get some exposure working with with strings in variables. 

```python
In [1]: my_str_variable = 'this IS my STRING to PLAY around WITH.'

In [2]: my_str_variable.capitalize()
Out [2]: 'This is my string to play around with.'

In [3]: my_str_variable.upper()
Out [3]: 'THIS IS MY STRING TO PLAY AROUND WITH.'

In [4]: my_str_variable.lower()
Out [4]: 'this is my string to play around with.'

In [5]: my_str_variable.replace('STR', 'fl')
Out [5]: 'this IS my flING to PLAY around WITH.'

In [6]: my_str_variable.split()
Out [6]: ['this', 'IS', 'my', 'STRING', 'to', 'PLAY', 'around', 'WITH.']
```

These are some of the most commonly used string methods. We've shown you what they do by default: `.capitalize()` capitalizes the first letter of the string and lowercases the rest; `.upper()` converts all the letters in the string to uppercase, and `.lower()` to lowercase; `.replace()` replaces a given substring in your string with another given substring; finally, `.split()` splits the string by a given string (space by default). There are many more string methods availiabe, and you can check them out in the [docs]('https://docs.python.org/2/library/stdtypes.html#string-methods').
