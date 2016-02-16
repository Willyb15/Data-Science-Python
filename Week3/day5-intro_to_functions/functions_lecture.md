## Functions

### Motivation 

Today we are going to learn about functions. In computer science terms, Python functions are known as subroutines. **Subroutines** are defined as a sequence of instructions that perform a specific task, packaged together as a unit (i.e. a small independent piece of code). We'll be talking all about how to define and use functions today. However, it's important to know why we want to use functions.

Our first reason for using functions is *reusability*, and stems from an idea called **Don't Repeat Yourself**, or **DRY** for short. The concept of DRY boils down to the idea that we want to be as concise as possible when writing code - we don't want to write unnecessary instructions. Part of this, as explicitly addressed by DRY, is not wanting to repeat the same or similar instructions over and over. Functions allow us to achieve this goal by giving us a tool that we can use to wrap up a set of instructions into a single independent unit. That independent unit can then be used to perform a specific task over and over, without needing to rewrite those instructions. They are written just once, in the function.

The second reason we want to use functions is *abstraction*. Consider a function that we've used already, `type()`. To use it we needed to know:

1. What the function is (i.e. its name)
2. What the function expects passed to it (i.e. the arguments)
3. What the function does
4. What the function gives back to us (i.e returns)

That's it - that's all we knew about `type()`, and we used it just fine. The key thing here is that we don't need to know anything about how `type()` does what it says it's supposed to do! This is the idea of abstraction - the implementation within a function is hidden from the caller (abstracted away if you will). There are a number of reasons why this trait is desirable.

First, it allows callers of the function to not be concerned with how the function itself works. Rather, they stay safe in the assumption that the function will work (know, though, that this assumption does not always prove true, in which case you'll have to do some of your own trouble shooting). This allows functionality to be easily shared, and makes it easier to build more complex things, since you're able to stand on the shoulders of those who have already written functions that you want to use.

Second, since the implementation is hidden from the caller, that actual implementation can change (so long as those four things listed above stay the same) and the caller wont know the difference. This makes it easy to split up problems into smaller pieces, and when something in one of those pieces needs to change, it wont affect the rest of the system. This is super powerful stuff.

### Intro to Functions

#### Built-in Functions  

In our programming journey so far, we've actually seen a number of functions. We've worked with the `len()` function, which returns the length of an inputted iterable. We've also worked with the `range()` function, which returns a list of numbers from an inputted minimum number to an inputted maximum number. There are many built-in functions that are available in Python, and you can find them [here](https://docs.python.org/2/library/functions.html). Each one of these functions is constructed in a very similar way, and they all take some arbitrary number of arguments. What if we want to have functions that perform tasks other than those available to us in the built-ins, though? Tonight, we'll learn how to define our own functions in such a way that we can use them as we have been using the built-ins! 

#### Function Definition Part 1

The first thing we're going to figure out how to do is actually define these things. To build up to this, let's take a look back at some code we previously wrote to output a list of all of the even elements in `some_collection`.

```python
evens = []
for element in some_collection:
    if element % 2 == 0:
        evens.append(element)
```

Now, let's imagine that that `some_collection` is actually just a list of numbers from 0 to 9 (i.e. `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`). Remember that we can use the `range()` function to create this. To get a list of all the even numbers from 0 to 9, then, we can modify our code as follows. 

```python 
evens = []
for element in range(10): 
    if element % 2 == 0: 
        evens.append(element)
```

**Note**: Remember that a `range(n)` call gives us a list from 0 up to but not including `n`, which is why we use `range(10)` above to get our list from 0 to 9. 

What if we wanted to put this code into a function, so that we could then get a list of evens from 0 to 9 anytime we wanted? This is a simple but straightforward example of reusability.

While not every function definition in Python will look the same (they'll have different names, different arguments passed to them, etc.), there is a general syntax that every function definition will follow. This syntax will look somewhat similar to the `while` and `for` loops in the sense that we will start off with some line (this line will define the function), followed by an indented block of code. That indented block of code will define what the function does. Okay, awesome! What goes on that first line, though?

The first line will always start off with a `def` statement followed by a space. What follows will then be the function name, a set of parentheses (without or without function parameters in them), and finally a colon. Let's see what this looks like.

```python
def my_func():
    pass # This pass just acts as a filler right now. 
```
Let's dive a little more into each of the parts and note what's important about them. First off, the `def` statement. This is what tells Python that what's coming after is a function, and what will make Python store your function in such a way that it is callable later on in your program. Second, the function name. The only real thing to note about this is that function naming conventions follow variable naming conventions (i.e. *snakecase*, where we lowercase our words and separate them by underscores). Next up are the parentheses. These are going to be filled with an optional and arbitrary number of parameters (which will dive into a little later). Finally, the colon, `:`. This is what is going to signal to Python that the function definition is over, and what follows will be the block of code that makes up the meat of the function. 

So, how would we build our `evens` code from earlier into a function? Well, all we have to do is simply copy and paste that block of code after our function definition. Let's be sure to give it a more descriptive name, though...

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

Hmmm, we didn't get anything back out, though? Why is that? It's because we didn't tell it to give us anything back out! Remember, we have to be explicit about what we want. The computer won't know that we want our evens list back unless we tell it to give it back. How do we do this? Python offers a special keyword, `return`, that we use to specifically return something back from a function (*note that this `return` keyword is specific to functions, and Python will throw an error if you try to use it outside of a function*). With this in mind, let's fix up our function to actually output our list of evens. 

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

Let's take a little bit more time to discuss the `return` statement. It's nice that it allows us to get back something from a function, but we do have to be careful with it, and make sure that we are using it in the way that we want. `return` is similar to the `break` statement that we learned about in Week 1. As soon as our function sees the `return` statement during execution, it will immediately exit from the function, giving back whatever output it has when it encounters the `return` statement. Let's alter the `return` statement in our `get_evens()` function to see how this comes into play. 

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

So we've now moved the `return` statement into the `if` block of our function, and we notice we get a different result. Why is this? Well, like we discussed, when the function encounters that `return` statement, it immediately gives back whatever output it has. When we called `get_evens()` above, it encountered that `return` statement in our first iteration through our `for` loop, when `element` was equal to `0`. As a result, `0` got appended to the `evens` list, and then in the next line that `evens` list got returned from the function. 


Okay, cool! 

#### Function Definitions Part 2

This is great, but what if we want to have the function act in a different way depending on how I (or somebody else) want to use it? What good is `get_evens()` if I want the evens from 0 to 20? As we've been hinting at, you can define functions in such a way that you can pass values to them. Let's change the `get_evens()` function that we defined above so that it can build an arbitrarily sized list of evens. We'll use our current code as a base, and build off of it as we work through defining functions with parameters, and calling functions with arguments passed in. We'll begin this exploration by adding in a parameter to the function definition. This parameter will control the range of numbers that we will grab evens from. 

```python 
In [1]: def get_evens(n): 
   ...:     evens = []
   ...:     for element in range(n): 
   ...:         if element % 2 == 0: 
   ...:             evens.append(element)
   ...:     return evens
```

With this implementation of our function, we can now pass in an arbitrary number to our function call, and then we will search for evens in a `range()` built with that arbitrary number. How exactly does this work, though? Well, we've told Python that our function should expect one and only one argument to be passed to it. When we call the function and pass in that argument, it will get assigned to whatever name we have given in the function definition (here it's `n`). Then, anytime we reference that given name (`n`) within the function, it will replace that given name with the value that we passed in. Let's check out a couple of different calls with this function, and see what they return. 

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

In addition to defining our function with the ability to now have arguments passed in, we can also build it so that if our function is called without an argument passed in, our parameter gets a value **by default**. This is useful if you want to build your function to have some default behavior, but still allow users to pass in arguments that change the default behavior or build off of it somehow. So how do we specify a default parameter value for our function? It's actually pretty simple. In the function definition itself, we just place an equals sign (`=`)  after the parameter name, and then the default value that we want to specify (*Note*: Python syntax dictates that there should be no spaces surrounding equals signs used in this way).

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

Okay, so those are the basics! We can of course define our functions with multiple parameters, and then pass in multiple arguments for those parameters when calling the function. And just like we can specify a default value for a single parameter, we can also specify default values for multiple parameters if we would like. Let's first modify our function so that we by default return a list of evens from the user inputted range (defined by `n`), but also give the user the option to input a different divisor (instead of 2) that will then return numbers in the inputted range that are divisible by the inputted divisor (i.e. the multiples of that number). We'll also change our function name and the name of the returned list (`evens`) so that they become more descriptive (our function is no longer outputting just evens).  

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
Out[4]: [0, 2, 4]

In [5]: get_multiples(10, 2)
Out[5]: [0, 2, 4, 6, 8]

In [6]: get_multiples(10, 3)
Out[6]: [0, 3, 6, 9]

In [7]: get_multiples(100, 10)
Out[7]: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
```

As you can see from our first three examples above, the output of our function hasn't changed - by default we still output a list of the even numbers up to 5, and when we pass in 5 as the value passed to `n` and 2 as the value passed to `divisor`, we also output a list of the evens up to 5. Cool! The other function calls also give us the results that we would expect.

Now let's get down to a syntactic "rule" that we have to follow when we define functions with default values. When we do this, we have to make sure that any parameters we are giving default values are **after** any parameters that we are not giving default values. Let's check out some examples...

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

Hopefully this pretty clearly demonstrates this "rule". In the first case, we defined our parameters that have default values (which is only one, `divisor`, here) after defining our parameters that don't have default values (which is only one, `n`, here), just as we are supposed to. And everything worked fine! In the second case, we defined a parameter with a default value before a parameter without a default value. That's a no no, and Python let us know! 

#### Parameters vs Arguments

As a quick aside, you may have noticed that we are using the terms "parameter" and "argument" seemingly interchangeably. What's up with that? Actually, these two terms have specific and distinct definitions. A **parameter** is the name of a variable given in a function definition. An **argument** is the value that is passed to a function when it is called. Phew! Glad that's all cleared up!

#### Calling functions with Positional Versus Keyword Arguments

So far, we've been calling this function that we built, and when we call it Python assigns the values to the correct parameters (for example, 5 to `n` and 2 to `divisor` above). But how exactly does this happen - how does Python know that when we call `get_multiples(5, 2)`, 5 should get assigned to `n` and 2 should get assigned to `divisor`? It turns out that by default, Python simply matches up the position of the arguments that are passed in with the position of the parameters that are given in the function definition. So, in our `get_multiples(5, 2)` call, it takes the first argument passed, `5`, and assigns that to the first parameter in the function definition, `n`. Similarly, it takes the second argument passed, `2`, and assigns it to the second parameter in the function definition, `divisor`. This method of passing arguments is **by position**, and the arguments `5` and `2` in this example are considered to be **positional arguments**. 

As you might have guessed from the title of this section, there is also another method of passing arguments, and that is **by keword**. The way this works is that instead of passing just the values in the function call, we call the values with the parameter name that they correspond to. Building off of our example above, using **keyword arguments** would mean our function call would look like this: `get_multiples(n=5, divisor=2)`. 

Okay, got it! But, there are one or two more things that we need to cover with regards to this topic. In the above examples, we used either **all** positional arguments or **all** keyword arguments. However, there is the possibility that we can use a **mixture** of positional and keyword arguments if we'd like. The only caveat is that we have to pass all positional arguments **before** passing any keyword arguments. For example: 

```python
In [1]: def get_multiples(n=5, divisor=2): 
   ...:     multiples_lst = []
   ...:     for element in range(n): 
   ...:         if element % divisor == 0: 
   ...:             multiples_lst.append(element)
   ...:     return multiples_lst

In [2]: get_multiples(5, 2) # All arguments passed by position. 
Out[2]: [0, 2, 4] 

In [3]: get_multiples(n=5, divisor=2) # All arguments passed by keyword. 
Out[3]: [0, 2, 4]

In [4]: get_multiples(10, divisor=3) # Okay mix of positional and keyword arguments.
Out[4]: [0, 3, 6, 9] 

In [5]: get_multiples(n=10, 3) # Not okay mix of positional and keyword arguments.
  File "<ipython-input-15-e4167d3728c9>", line 1
    get_multiples(n=10, 3)
SyntaxError: non-keyword arg after keyword arg
```

### Variable Scope

Variable scope is a topic in and of itself, but up until now we haven't really had a good reason to discuss it. **Variable scope** is going to define the part (or block) of your program in which a variable is visible. We typically refer to one of two scopes for variables - **global** scope and **local** scope. A variable with **global** scope is visible everywhere. It can be used anywhere in your script, including any of the functions you have written (it can even be used inside of a function written inside of a function). A variable with **local** scope, on the other hand, is only visible in the scope in which it is enclosed (typically a function). 

When referencing a variable, Python will search the following scopes (in order) to resolve the reference: 

1. The current function's scope. 
2. Any enclosing scopes (like other containing functions). 
3. The scope of the module (i.e. script) that contains the code (often referred to as the **global** scope). 
4. The built-in scope (contains the built-in functions).

This is kind of a confusing concept to grasp, so let's look at a concrete example.

```python 
In [1]: my_global_var = 5

In [2]: def my_test_func(): 
   ...:     print "My global variable:",  my_global_var # Accessible and will print. 
   ...:     my_local_var = 10 # This is only accessible in my_test_func. 
   ...:     print "My local variable:", my_local_var  
   ...:

In [3]: my_global_var # Remember it's accessible anywhere. 
Out[3]: 5

In [4]: my_test_func()
My global variable: 5
My local variable: 10

In [5]: print my_local_var
NameError                                 Traceback (most recent call last)
<ipython-input-4-b0b2b2a41781> in <module>()
    > 1 print my_local_var

NameError: name 'my_local_var' is not defined
```

Notice that `my_global_var` is accessible anywhere - both inside and outside of our function. This is because it is in the **global scope**. `my_local_var`, on the other hand, was defined within `my_test_func`. As a result, it is enclosed within the scope of `my_test_func`, and not accessible outside of it.   

### List and Dictionary Comprehensions

The last topic we're going to cover today is not on functions, but instead a different way to accomplish something you already know about: constructing list and dictionaries. Consider the frequent task that we perform at the beginning of dealing with lists and dictionaries, constructing them. Thus far we have taken advantage of the mutability inherent to lists and dictionaries to build them up one element or key-value pair, respectively, at a time. However there is a more succinct way to accomplish the vast majority of your list and dictionary construction tasks.

#### List Comprehensions

Before we dive into the specifics about how this new tools works, lets look at a toy question where we build a list so that we can break down the process.

Consider you have the list `[1, 5, 9, 33]` stored in the variable `my_list`. Now you want to make a new list of the squares of all the values in `my_list` and call it `my_squares`. With the tools you know about, code that you'd write to perform this task might look like this:

```python
my_squares = []
for num in my_list:
    my_squares.append(num ** 2)
```

And now `my_squares` will hold the list `[1, 25, 81, 1089]`. To get is basically what we were doing was specifying a range of stuff that will be added on to the end of the list. So from a high level we can write the framework of creating a list in code as:

```python
list_were_building = []
for thing in iterable:
    list_were_building.append(transform(thing))
```

Now for the fun part, with this structure in mind we can use the following syntax to perform the same task of building up a list in a single line! Check it out, along with how it would look for the construction of `my_squares`.

```python
list_were_building = [transform(thing) for thing in iterable]
my_squares = [num ** 2 for num in my_list]
```

This last line of code does the exact same thing as the three lines above! In this line the thing that we would pass to the `append()` method on the list we're building up, `transformed_thing_to_append` gets comes at the beginning of the statement in the `[]`, then the loop statement that we had written previously comes after. Neat, huh?? Speaking of which, really what's happening is those `transformed_thing_to_append`s are getting passed to the syntactic sugar  version of the list constructor that you know so well. This is the basic idea behind the [list comprehension](https://en.wikipedia.org/wiki/List_comprehension).

But wait! There's more! Remember, in all the examples where we were getting evens we had a condition to decide when to append a value to a list? We can also use conditions to determine what "transformed things" get added in a list comprehension! In addition, the syntax flows the same as we saw above. After the transformed thing that would be passed to the append method in the old way of constructing a list, you write the same structure as if you were writing the old loops, but without colons and new lines. Lets look at the evens list builder we're all so familiar with and then descriptive fake code to hammer this home.

```python
# Old way of constructing list of evens
evens = []
for num in range(10):
    if num % 2 == 0:
        evens.append(num)

# Old way at high level
list_were_building = []
for thing in iterable:
    if condition:
        list_were_building.append(transform(thing))

# List comprehension way of constructing list of evens
evens = [num for num in range(10) if num % 2 == 0]

# List comprehension way at high level
list_were_building = [transform(thing) for thing in iterable if condition]
```

Same as before, just reading left to right after the thing to append, instead of top down. One thing to note though, while in the evens case we didn't actually "transform" the thing we were appending, that's fine. The way `transform()` was called in the above examples as though it were a function is actually an option when writing list comps. For example, the `my_squares` example could be accomplished in the same way with:

```python
def square(num):
    return num ** 2

my_squares = [square(num) for num in my_list]
```

This might seem silly since we could just write `num ** 2` directly in the list comp as we did above. However, this, calling of a function, in the list comp, becomes a powerful idea when you want to transform the values being iterated over is a complex way.

#### Dictionary Comprehensions 

Just as with list comps being a more succinct way of constructing a list, we have the same ability for dictionaries. Dictionary comprehensions operate in the same way as their list counterparts, except for one fundamental difference.
