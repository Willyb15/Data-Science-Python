## Functions

### Motivation 

CARY, HELP!!! 

### Intro to Functions

#### Function Definition

The first thing we're going to figure out how to do is actually define these things. To build up to this, let's take a look back at some code we previously wrote to output a list of all of the even elements in `some_collection`.

```python
evens = []
for element in some_collection:
    if element % 2 == 0:
        evens.append(element)
```

Now let's imagine that that `some_collection` is actually just a list of numbers from 0 to 9 (i.e. `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`). Remember that we can use the `range()` function to create this. To get a list of all the even numbers from 0 to 9,then, we can modify our code as follows. 

```python 
evens = []
for element in range(10): 
    if element % 2 == 0: 
        evens.append(element)
```

**Note**: Remember that a `range(n)` call gives us a list from 0 up to but not including `n`, which is why we use `range(10)` above to get our list from 0 to 9. 

What if we wanted to throw this into a function, so that we could then get a list of evens from 0 to 9 anytime we wanted? 

While not every function definition in Python will look the same (they'll have different names, different arguments passed to them, etc.), there is a general syntax that every function definition will follow. This syntax will look somewhat similar to the `while` and `for` loops in the sense that we will start off with some line (this line will define the function) followed by an indented block of code. That indented block of code will define what the function does. Okay, awesome! So what goes on that first line, though?

The first line will always start off with a `def` statement followed by a space. What follows will then be the function name, a set of parentheses (without or without function arguments with them), and finally a colon. Let's see what this looks like.

```python
def my_func():
    pass # This pass just acts as a filler right now. 
```
Let's dive a little more into each of the parts and note what's important to know about them. First off, the `def` statement. This is what is going to tell Python that what's coming after is a function, and what will make Python store your function in such a way that it is callable later on in your program. Second, the function name. The only real thing to note about this is that function naming conventions follow variable naming conventions (i.e. snakecase, where we lowercase our words and separate them by underscores). Next up are the parentheses. These are going to be filled with an optional and arbitrary number of arguments (which will dive into a little later). Finally, the colon, `:`. This is what is going to signal to Python that the function definition is over, and what follows will be the block of code that the function operates. 

So how would we build our evens code from ealier into a function? All we have to do is simply copy and paste that block of code after our function definition. Let's be sure to give it a more descriptive name, though...

```python 
In [1]: def get_evens(): 
   ...:     evens = []
   ...:     for element in range(10): 
   ...:         if element % 2 == 0: 
   ...:             evens.append(element)
```

Awesome! Now we can call this function anytime.

```python
In [2]: get_evens()
```

Hmmm, we didn't get anything back out, though? Why is that? It's because we didn't tell it to give us anything back out! Remember, we have to be explicit about what we want. The computer won't know that we want our evens list back unless we tell it to give it back. How we do this? Python offers a special keyword, `return`, that we use to specifically return something back from a function (*note that this `return` keyword is specific to functions, and Python will throw an error if you try to use it outside of a function*). With this in mind, let's fix up our function to actually output our list of evens. 

```python
In [1]: def get_evens(): 
   ...:     evens = []
   ...:     for element in range(10): 
   ...:         if element % 2 == 0: 
   ...:             evens.append(element)
   ...:     return evens
```

Now when we call this function, it will actually give us back that list of evens...

```python
In [2]: get_evens()
Out[2]: [0, 2, 4, 6, 8]
```

Let's take a little bit more time to dicuss the `return` statement. It's nice that it allows us to get back something from a function, but we do have to be careful with it, and make sure that we are using it in the way that we want. `return` is similar to the `break` statement that we learned about in Week 1, in the sense that as soon as our function see's the `return` statement during execution, it will immediately exit from the function, giving back whatever output it has when it encounters the `return` statement. Let's alter the `return` statement in our `get_evens()` function to see how this comes into play. 

```python
In [1]: def get_evens(): 
   ...:     evens = []
   ...:     for element in range(10): 
   ...:         if element % 2 == 0: 
   ...:             evens.append(element)
   ...:             return evens 

In [2]: get_evens()
Out[2]: [0]
```

So we've now moved the `return` statement into the `if` block of our function, and we notice we get a different result. Why is this? Well, like we discussed, when the function encounters that `return` statement, it immediately gives back whatever output it has. When we called `get_evens()` above, it encountered that `return` statement in our first iteration through our for loop, when `element` was equal to `0`. As a result, `0` got appended to the `evens` list, and then in the next line that `evens` list got returned from the function. 

Okay, cool! 

