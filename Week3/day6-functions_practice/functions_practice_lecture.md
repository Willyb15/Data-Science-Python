## Getting Our Hands Dirty with Functions

### Top-Down Programming

Up until now we've only written one-off functions, aka ones that operate independently of one another. But a great use for functions is making them so they help you solve small pieces of a large problem. This idea begets a programming strategy known as **top-down**. The idea behind the top-down approach to programming is, start at the definition of the problem and distribute out tasks, defined at a high level, to functions. Then each of those functions will implement more functions. As you go to subsequently deeper layers of your program the functions perform increasingly specific tasks, until there is a specific piece of the programming puzzle that a function can perform, a base task if you will.

One difficulty regarding this approach is that it requires full vision about how a problem should be broken down before you get into the nitty-gritty implementation of any base tasks. This is a problem that is oft discussed during software design. Luckily, for most of the problems that we will want to solve on our own, unless we're working within a larger framework of a project (as would exist if you were part of a team, either independent or within a company), can be managed with an iterative approach to implementing top-down.

Basically, this involves writing some code to start solving the first part of the problem, then once that code starts becoming it's own independent piece, putting it into a function. At that point, start writing more code that will likely become it's own funciton. Et cetera. This mish-mash of an approach can be difficult to get used to, and is by no means perfect. But with practice it starts feeling second nature. To that end, we will being going through that process today, solving a problem that is too large to be implemented in a single function, to see how it is carried out. Along the way we will learn about a few more Python tools, be able to see how the solution to a problem can evolve over time, and see how functions in action are such a powerful tool (both in taking advantage of employing a DRY methodology and seeing the power of abstraction).

### Let's Do Python

Ok, time to solve a problem:

    Write a function, call it `create_report` that takes the path for a text file and tells you the number of sentences, words and characters in that file.

#### Starting Slow

This doesn't seem to bad, there are obvious use cases for the function, so having it all bundled up in a reusable form makes a lot of sense. Let's start off by opening a new Python script file, call it `txt_file_processing.py`. Throughout the rest of this lecture we will being seeing updates of the code in this file so that we can watch the solution evolve in the iterative manner which was discussed above. What's the first thing that we put in `txt_file_processing.py`? The function that we want to write! For the code to run, whenever we set up a skeleton for a functionality that isn't yet implemented we'll use a `pass` until we figure out how it's going to work. So our script currently looks like this:

```python
def create_report():
    pass
```

Alright, maybe a bit obvious, if not a slightly slow start, lets pick up the pace. Back to the problem at hand. We were told that `create_report()` should take the path to a text file.

```python
def create_report(file_path):
    pass
```

Done. Now it's time for a little more Python learning. How are we going to get at the contents on the text file located a `file_path`? There's actually a Python function for exactly this problem (you'll come to learn that many, many things you want to do in Python are available to you). Here we want to use the appropriately name `open()` function with a `with` statement.

```python
def create_report(file_path):
    with open(file_path) as txt_file:
        pass
```

Let's talk about what this line does. The `open()` (docs [here](https://docs.python.org/2/library/functions.html#open), takes a file path and a couple of optional arguments that we don't have to worry about for this problem and returns a "file object" which we are storing in the variable `txt_file`. The `with` statement allows us to not be concerned with closing the connection to the file object when we're done with it, notice that we're in an indented block for the body of the `with`, when we end that block, the with will automatically deal with these details for us and for that reason is considered the Pythonic way to handle files.


At this point we now have access to the contents of the file via the variable `txt_file` within the scope of the `with`. So what do we do with it? There are a couple of things that are advised at this point, one is reading the documentation for [file objects](https://docs.python.org/2/library/stdtypes.html#bltin-file-objects), reading documentation is almost never a bad idea; and/or you could try to get your hands dirty in IPython. This would require you to have a test file to play with which is a great thing to have in general so that you can verify whether the code your writing is working as you move through solving the problem. 

Check out the included test txt file, `test_text.txt` which is filled with a small amount of text so it's easy to play with. We can use it along with some of the code we've writen already inside of IPython. Frequently a simple `print()` will allow you to get a handle on what's going on, but sometimes its necessary to inspect things with `type()` or by calling other functions. Lets see how we would figure out what's going on with `txt_file`.

```python
In [1]: with open('test_text.txt') as txt_file:
   ...:     print(txt_file)
   ...:     
<_io.TextIOWrapper name='test_text.txt' mode='r' encoding='UTF-8'>
```

Ok, that wasn't as useful as we may have wanted to be. Taking a look at the docs linked from above for file objects we see an example where we use a `for` loop to go through the lines in the file we open. Let's try that!

```python
In [2]: with open('test_text.txt') as txt_file:
   ...:     for line in txt_file:
   ...:         print(line)
   ...:         
This is a test

text file.

The quick red fox

jumped over the

lazy brown dog.
```

Awesome! This is way better. We now know how to access the contents of a text file! Let's add this new-found information to our ever growing script.

```python
def create_report(file_path):
    with open(file_path) as txt_file:
        for line in txt_file:
            pass
```

#### Let's Put the FUN in Functions!

Back to the problem specification. We need to take these lines and get the number of sentences, words and characters contained within them. At this point we should realize that we need to aggregate these counts somewhere. There are a lot of ways that we could do that, here we're going to do it with a dictionary. Let's initialize one now.

```python
def create_report(file_path):
    counts_dict = {'sentences': 0, 'words': 0, 'characters': 0}
    with open(file_path) as txt_file:
        for line in txt_file:
            pass
```

Now that we have a place to store the counts that we come across while looping through our lines we can start writing the body of our loop. Here's a place where our workflow could diverge. We could start writing code inside the body of our loop and later figure out what of that code completed a specific, indepent tast, or we could recognize that what we're about to do in the loop is it's own distict task, updating our counts with the info from a line, and start writing a function now. Let's go with the latter option since we've seen plently of examples of turning existing code into a function. 

So what does this process look like? We don't have any code to put into a function, what are we supposed to do? Consider though that we didn't have any code when we started writing `create_report()`, but we started writing it anyways! Lets do something like that here but this time realize that we're tasked with identifying the function that we're trying to write. To do this let's think about what we want to do inside the loop, we said it above, we're "updating our counts with the info from" the current line. 

Let's start a function with an appropriate name now, knowing that it's going to need `line` and `counts_dict` passed to it. The first, `lines`, will be neccessary because the line we're analyzing changes each iteration of the loop; the second, `counts_dict` is necessary because it's keeping track of all the counts and therefore needs to be accessible for update while `line` is being processed. Thinking things through in this way makes is easy to write out a function defintion.

```python
def update_counts(line, counts_dict):
    pass

def create_report(file_path):
    counts_dict = {'sentences': 0, 'words': 0, 'characters': 0}
    with open(file_path) as txt_file:
        for line in txt_file:
            update_counts(line, counts_dict)
```

**Note**: While the names of the variables that we're passing to `update_counts()` are the same as the names of the parameters we defined in the function definition, this is not necessary. Sometimes this is useful so that it's easier to follow the flow of variables being passed between functions. But sometimes the names need to be more general because the function is performing a more general task.

What exactly does `update_counts()` need to do with a line? Well, we know that we're going to have to count the number of words in it, and the number of characters in those words. As for the number of sentences, this is a fairly difficult problem. One way that we could solve this is by counting the number of periods, ".", assuming that any sentences we will see will end in one. Admittedly, this is a fairly naive way to solve the problem, sentences can end with other punctuation, exclaimation points and question marks immediately come to mind. This solution is also susceptable to the ellipsis which has three periods all in a row. 

For now we will neglect these obvious defects in our solution and go back later to make it better. This type of practice is very regular when solving programming problems. As we've talked about, solutions are often built up in an iterative, testing as you go manner. In addition, there's a decent chance there are other edge cases that haven't even been considered. That's part of the beauty of using functions. Since they abstract away the implementation of counting sentences, words and characters, we can later go back and change this single piece of our problem, potentially making it more complete or possibly more efficient.

At this point lets set up an even smaller test case so that we can verify the functionality of just `update_counts()`. Consider the string 'This is a test string. Only for testing'. We can see that it has 1 well defined sentence, 8 words and 39 characters counting spaces. Lets set up a counts dictionary and this string in an IPython environment.

```python

In [1]: test_string = 'This is a test string. Only for testing'

In [2]: counts_dict = {'sentences': 0, 'words': 0, 'characters': 0}
```

We can immediately see that the number of characters in this string can be easily found using the `len()` function.

```python
In [3]: len(test_string)
Out[3]: 39

In [4]: counts_dict['characters'] += len(test_string)
```

As for counting the words, we can count (get it??) on the `split()` method to separate our string into individual words.

```python
In [5]: test_string.split()
Out[5]: ['This', 'is', 'a', 'test', 'string.', 'Only', 'for', 'testing']

In [6]: len(_)
Out[6]: 8

In [7]: counts_dict['words'] += len(test_string.split())
```

**Note**: The underscore, `_` can be used in IPython to access the most recent output.

As for finding the number of periods within our string, there happens to be a very useful string method called `count()`.

```python
In [8]: test_string.count('.')
Out[8]: 1

In [9]: counts_dict['sentences'] += test_string.count('.')

In [10]: counts_dict
Out[10]: {'characters': 39, 'sentences': 1, 'words': 8}
```

With all of this testing done, verified by checking what's stored in `counts_dict`, we can now go back to our script and implement what we've found in `update_counts()`knowing that the string that is accessable within its scope is named `line`.

```python
def update_counts(line, counts_dict):
    counts_dict['sentences'] += line.count('.')
    counts_dict['words'] += len(line.split())
    counts_dict['characters'] += len(line)

def create_report(file_path):
    counts_dict = {'sentences': 0, 'words': 0, 'characters': 0}
    with open(file_path) as txt_file:
        for line in txt_file:
            update_counts(line, counts_dict)
```
