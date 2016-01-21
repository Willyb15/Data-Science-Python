# Time to do Python

## Workflow
There's no better way to learn a programming language than to try and solve real problems with it. To that end this assignment will present a good workflow for working with IPython to iteratively test code while you create your scripts in a text editor.

Let's walk through an example, feel free to follow along so you get some hands on practice. Consider the problem:
    
    Write a script that prints the sum of the whole numbers between 1 and a user inputted number.

Alright, first we want to open up IPython and your favorite text editor (sublime if you followed our advice from day 1), I prefer to have these two side by side so that it's easy to look at and work in each.

We're going to have to start a new file in our text editor to store our script. You should give your script a short name that quickly describes what it does. Python scripts are appended with the file extension `.py`. So, for this problem I would name my script something like `sum_whole_numbers.py`. Now we're off to the races.

At this point I start thinking about how I'm going to solve my problem. Most of the time this means that I want to experiment with potential solutions/approaches. This is exactly what IPython is great for. It allows you to interact with Python one step at a time and remembers what you've done for the entire time the *session* has been open.

With that in mind I want to give myself a variable to play with as I solve this problem. Lets call it `my_num` and set it to 7 in IPython.

**Note**: If you want to look at the variables currently in the namespace of your IPython session simply type the command `whos` into the console.

```python
In [1]: my_num = 7

In [2]: whos
Variable   Type    Data/Info
============================
my_num     int     7
```

Now that I have a number to work with its time to think about how to solve the problem. I know that I'm going to need a variable to store my sum result in, `sum_result`, and another to keep track of the number I'm going to add to the sum, `current`. 

```python
In [3]: sum_result = 0

In [4]: current = 1
```

I know that I'm going to need a while loop that terminates when `current` is less than or equal to `my_num`.

```python
In [5]: while current <= my_num:
   ...:     
```

Notice that when we start a while loop IPython knows that you're going to want to write the while block so it prompts for that with the `...:`. What is this while going to do at each iteration. Well, we need to add the value of `current` (remember we will only make it into the loop if `current` is less than or equal to `my_num`) to `sum_result` and then increment current by one. Let's let IPython know what we want to do now!

```python
In [5]: while current <= my_num:
   ...:     sum_result += current
   ...:     current += 1
   ...:     
```

Ok, so, what happened? IPython didn't show us anything, did it even work?? It did actually! We just have to check `sum_result` to see what we got.

```python
In [6]: sum_result
Out[6]: 28
```

### Tying it All Together

This is great! Now that we know how we're solving our problem in Python we can go back to writing out script. Lets take what we've written and put it in our text file, `sum_whole_numbers.py`.

```python
my_num = 7
sum_result = 0
current = 1
while current <= my_num:
    sum_result += current
    current += 1
```

But wait, weren't we asked to take input from the user? And didn't we need to print the result? These aren't hard fixes, remember the `raw_input()` function to get numbers from the user? Lets use that. All we need to do print the value we computed is pass `sum_result` to `print()`.

```python
my_num = int(raw_input('Enter a number to find the sum up to: '))
sum_result = 0
current = 1
while current <= my_num:
    sum_result += current
    current += 1
print(sum_result)
```

Now we can simply run our new script from the IPython. Know that IPython needs to know where the script you wrote is in your file structure. So if you open IPython from the same directory that your script is saved in then there should be no problem. Otherwise you'll need to give IPython a path to the script.

```python
In [7]: run sum_whole_numbers.py
Enter a number to find the sum up to: 7
28

In [8]: run sum_whole_numbers.py
Enter a number to find the sum up to: 9
45
```

This is awesome! We now have a script that will solve a problem for arbitrary input! Congratulations, if you've been following along you've written your first dynamic program. The process outlined above is generally iterated over and over, as you test and find chunks of code that you know work in IPython you can iteratively add them to your script.

## Assignment Questions

1.  Write a script that computes and prints the factorial of a user inputted number.
2.  Write a script that determines whether or not a user inputted number is a [prime](https://en.wikipedia.org/wiki/Prime_number) and prints `'The number you inputted is a prime/ not a prime number.'` depending on what your script finds.
3.  One can use loops to compute the elements of a mathematical series. Series can be defined recursively with the value of each element depending on the one that comes before it. Consider the series created by the rules:  

    ![series](imgs/series_pic.png)  
   
    Write a script that prints the element in the series as determined by input from the user. e.g. If the user inputs the number `3`, your script should print `15`. You're welcome to check the math!

### Extra Credit

Try to break your scripts by passing them something other than a number. Make your scripts robust to poorly formatted input. Hint: Look at the [isinstance()](https://docs.python.org/2/library/functions.html#isinstance) function. How can we use this function and conditionals to guarentee only good input, ints, will be processed? If the input ends up being bad, print a message notifying the user.
