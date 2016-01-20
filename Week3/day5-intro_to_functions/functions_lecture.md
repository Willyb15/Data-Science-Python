## Functions

### Motivation 

CARY, HELP!!! 

### Intro to Functions

#### Function Definition Part 1

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

The first line will always start off with a `def` statement followed by a space. What follows will then be the function name, a set of parentheses (without or without function parameters in them), and finally a colon. Let's see what this looks like.

```python
def my_func():
    pass # This pass just acts as a filler right now. 
```
Let's dive a little more into each of the parts and note what's important to know about them. First off, the `def` statement. This is what is going to tell Python that what's coming after is a function, and what will make Python store your function in such a way that it is callable later on in your program. Second, the function name. The only real thing to note about this is that function naming conventions follow variable naming conventions (i.e. snakecase, where we lowercase our words and separate them by underscores). Next up are the parentheses. These are going to be filled with an optional and arbitrary number of parameters (which will dive into a little later). Finally, the colon, `:`. This is what is going to signal to Python that the function definition is over, and what follows will be the block of code that the function operates. 

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

#### Function Definitions Part 2

As we've been hinting at, you can define functions in such a way that you can pass arguments in. Let's start out using the `get_evens()` function that we defined above. We'll use this as our base and build off of it as we work through defining functions with parameters, and calling functions with arguments passed in. We'll begin this exploration by adding in parameter to the function definition. This parameter will control the range of numbers that we will grab evens from. 

```python 
In [1]: def get_evens(n): 
   ...:     evens = []
   ...:     for element in range(n): 
   ...:         if element % 2 == 0: 
   ...:             evens.append(element)
   ...:     return evens
```

With this implementation of our function, we can now pass in an arbitrary number to our function call, and then we will search for evens in a `range()` built with that arbitrary number. How exactly does this work, though? Well, we've told Python that our function will expect one argument to be passed in. When we call the function and pass in that argument, it will get assigned to whatever name we have given in the function definition (here it's `n`). Then, anytime we reference that given name (`n`) within the function, it will replace that given name with the value that we passed in. Let's check out a couple of different calls with this function, and see what they return. 

```python
In [1]: def get_evens(n): 
   ...:     evens = []
   ...:     for element in range(n): 
   ...:         if element % 2 == 0: 
   ...:             evens.append(element)
   ...:     return evens

In [2]: get_evens(5)
Out[2]: [0, 2, 4]

In [3]: get_evens(14)
Out[3]: [0, 2, 4, 6, 8, 10, 12]

In [4]: get_evens(20)
Out[4]: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

Neat, huh!? Turns out we're just getting started...

In addition to defining our function with the ability to now have an argument passed in, we can also build it so that if our function is called without an argument passed in, our parameter gets a value **by default**. This is useful if you want to build your function to have some default behavior but still allow users to pass in arguments that change the default behavior or build off of it somehow. So how do specify a default parameter value for our function? It's actually pretty simple. In the function definition itself, we just place an equals sign (`=`) after the parameter name, and then the default value that we want to specify.

```python
In [1]: def get_evens(n=5): 
   ...:     evens = []
   ...:     for element in range(n): 
   ...:         if element % 2 == 0: 
   ...:             evens.append(element)
   ...:     return evens

In [2]: get_evens()
Out[2]: [0, 2, 4]

In [3]: get_evens(5)
Out[3]: [0, 2, 4]

In [4]: get_evens(14)
Out[4]: [0, 2, 4, 6, 8, 10, 12]

In [5]: get_evens(20)
Out[5]: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

Here, we've specified the default value for `n` to be 5. That is, if no value is passed in for `n`, we assign the value of 5 to it. So you'll notice in the first function call to `get_evens()` where we pass no arguments, we get the same output as if we pass in the value 5 (which makes sense, since we set 5 as the default). Meanwhile, when we pass in other values (14 and 20), we get the same results as before. This is the point of setting a default parameter value - if the caller of the function specifies a value for that parameter, then that is the value used in the function; otherwise, the default value that was specified is used.

Okay, so those are the basics! We can of course define our functions with multiple parameters, and then pass in multiple arguments for those parameters when calling the function. And just like we can specify a default value for a single parameter, we can also specify default values for multiple parameters if we would like. Let's first modify our function so that we return a list of evens from the user inputted range (defined by `n`) by default, but also give the user to input a different divisor (instead of 2) that will then return numbers in the inputted range that are divisible by the inputted divisor (i.e. the multiples of that number). We'll also change our function name and the name of the returned list (`evens`) so that they become more descriptive (our function is no longer ouputting just evens).  

```python 
In [1]: def get_multiples(n=5, divisor=2): 
   ...:     multiples_lst = []
   ...:     for element in range(n): 
   ...:         if element % divisor == 0: 
   ...:             multiples_lst.append(element)
   ...:     return multiples_lst 

In [2]: get_multiples()
Out[2]: [0, 2, 4]

In [3]: get_multiples(5)
Out[3]: [0, 2, 4]

In [4]: get_multiples(5, 2)
Out[4] [0, 2, 4]

In [5]: get_multiples(10, 2)
Out[5]: [0, 2, 4, 6, 8]

In [6]: get_multiples(10, 3)
Out[6]: [0, 3, 6, 9]

In [7]: get_multiples(100, 10)
Out[7]: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
```

As you can see from our first three examples above, the output of our function hasn't changed - by default we still output a list of the even numbers up to 5, and when we pass in 5 as the value passed to `n` and 2 as the value passed to `divisor`, we also output a list of the evens up to 5. Cool! 

Now let's get down to a syntatical 'rule' that we have to follow when we define functions with default arguments. When we do this, we have to make sure that any parameters we are giving default arguments are **after** any parameters that we are not giving default arguments. Let's check out some examples...

```python
In [1]: def get_multiples(n, divisor=2): 
   ...:     multiples_lst = []
   ...:     for element in range(n): 
   ...:         if element % divisor == 0: 
   ...:             multiples_lst.append(element)
   ...:     return multiples_lst 

In [2]: def get_multiples(n=5, divisor): 
   ...:     multiples_lst = []
   ...:     for element in range(n): 
   ...:         if element % divisor == 0: 
   ...:             multiples_lst.append(element)
   ...:     return multiples_lst 
  File "<ipython-input-2-fa1c095e8bea>", line 1
    def get_multiple(n=5, divisor): 
SyntaxError: non-default argument follows default argument
```

Hopefully this pretty clearly demonstrates this 'rule'. In the first case, we defined our parameters that have default values (which is only one, `divisor`, here) after defining our parameters that don't have default values (which is only one, `n`, here), just we are supposed to. And everything worked fine! In the second case, we defined a parameter with a default value before a parameter without a default value. That's a no no! 


