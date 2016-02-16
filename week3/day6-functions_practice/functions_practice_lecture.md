## Getting Our Hands Dirty with Functions

### Top-Down Programming

Up until now we've only written one-off functions (ones that operate independently of one another). A great use for functions, though, is building them so that they work together to help you solve small pieces of a larger problem. This idea begets a programming strategy known as **top-down**. The idea behind the top-down approach to programming is to start out at the definition of the problem, and break it out into smaller problems. We then distribute out these smaller problems as tasks, defined at a high level, to functions. Each of those functions will implement more functions, and so on and so forth. As you go to subsequently deeper layers of your program, the functions will perform increasingly specific tasks, until there is a specific piece of the programming puzzle that a single function can perform (a base task if you will).

One difficulty with this approach is that it requires full vision about how a problem should be broken down before you get into the nitty-gritty implementation of any base tasks. This is a problem that is oft discussed during software design. Luckily, for most of the problems that we will want to solve on our own, we can manage them with an iterative approach to implementing top-down.

Basically, this involves writing some code to start solving the first part of the problem, and once that code starts becoming it's own independent piece, putting it into a function. At that point, we start writing more code that will likely become it's own function, and so on and so forth. This mish-mash of an approach can be difficult to get used to, and is by no means perfect. But with practice, it starts feeling like second nature. To that end, we will be going through that process today and solving a problem that is too large to be implemented in a single function. Along the way, we will learn about a few more Python tools, be able to see how the solution to a problem can evolve over time, and see how functions in action are such a powerful tool (both in taking advantage of employing a DRY methodology and seeing the power of abstraction).

### Let's Do Python

Ok, time to solve a problem:

Your boss comes to you and asks you to write a function, call it `create_report`, that takes the path for a text file and tells you the number of sentences, words, and characters in that file.

#### Starting Slow

This doesn't seem to bad; there are obvious use cases for the function, so having it all bundled up in a reusable form makes a lot of sense. Let's start off by opening a new Python script file, calling it `txt_file_processing.py`. Throughout the rest of this lecture, we will be seeing updates of the code in this `.md` file so that we can watch the solution evolve in the iterative manner which was discussed above. What's the first thing that we put in `txt_file_processing.py`? The function that we want to write! In order for the code to run and not throw us any errors, we'll use a `pass` whenever we set up a skeleton for a function that isn't actually implemented yet (i.e. we haven't fully written). So our script will start out looking like this:

```python
def create_report():
    pass
```

Alright, maybe a bit obvious, if not a slightly slow start; let's pick up the pace. Back to the problem at hand. We were told that `create_report()` should take the path to a text file.

```python
def create_report(file_path):
    pass
```

Done. Now it's time for a little more Python learning. How are we going to get at the contents in the text file located at `file_path`? There's actually a Python function for exactly this problem (you'll come to learn that many, many things you want to do in Python are available to you via built-in functions). Here we want to use the appropriately named `open()` function with a `with` statement.

```python
def create_report(file_path):
    with open(file_path) as txt_file:
        pass
```

Let's talk about what this line does. The `open()` (docs [here](https://docs.python.org/2/library/functions.html#open)), takes a file path and returns a "file object" which we are storing in the variable `txt_file`. The `with` statement allows us to not be concerned with closing the connection to the file object when we're done with it. Notice that we're in an indented block for the body of the `with` - when we end that block, the `with` will automatically deal with closing the file for us, and for that reason is considered the Pythonic way to handle files.

At this point, we now have access to the contents of the file via the variable `txt_file` within the scope of the `with`. So what do we do with it? There are a couple of things that are advised at this point. One is reading the documentation for [file objects](https://docs.python.org/2/library/stdtypes.html#bltin-file-objects). Reading documentation is almost never a bad idea. Another option would be for you to get your hands dirty in IPython. This would require you to have a test file to play with, which is a great thing to have in general so that you can verify whether the code your writing is working as you move through solving the problem. 

Check out the included `test_text.txt` file, which is filled with a small amount of text so that it's easy to play with. We can use it to test out some of the code we've written inside of IPython. Frequently a simple `print()` will allow you to get a handle on what's going on, but sometimes its necessary to inspect things with `type()`, or by calling other functions. Let's see how we would figure out what's going on with the `txt_file` variable that we get back from the `with` statement.

```python
In [1]: with open('test_text.txt') as txt_file:
   ...:     print(txt_file)
   ...:     
<_io.TextIOWrapper name='test_text.txt' mode='r' encoding='UTF-8'>
```

Ok, that wasn't as useful as we may have wanted it to be. Taking a look at the docs linked from above for file objects, we see an example where we use a `for` loop to go through the lines in the file we open. Let's try that!

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

Back to the problem specification. We need to take these lines and get the number of sentences, words, and characters contained within them. At this point we should realize that we need to aggregate these counts somewhere. There are a lot of ways that we could do that. One way would be to have each count stored in it's own variable, but here we're going to do it with a dictionary (we'll see why this is a good idea very soon). Let's initialize one now.

```python
def create_report(file_path):
    counts_dict = {'sentences': 0, 'words': 0, 'characters': 0}
    with open(file_path) as txt_file:
        for line in txt_file:
            pass
```

Now that we have a place to store the counts that we come across while looping through our lines, we can start writing the body of our loop. Here's a place where our workflow could diverge. We could start writing code inside the body of our loop and later figure out what of that code completed a specific, independent task, or we could recognize that what we're about to do in the loop is it's own distinct task and start writing a function. Let's go with the latter option, since we've seen plenty of examples of turning existing code into a function. 

So what does this process look like? We don't have any code to put into a function - what are we supposed to do? Consider the fact that we didn't have any code when we started writing `create_report()`, but we started anyways! Let's do something like that here, but this time realize that we're tasked with identifying the function that we're trying to write. To do this, let's think about what we want to do inside the loop. We said it above - we're "updating our counts with the info from the current line". 

Let's start a function with an appropriate name, knowing that it's going to need a `line` passed to it, as well as `counts_dict`. The first, `line`, will be necessary because the line we're analyzing changes in each iteration of the loop; the second, `counts_dict`, is necessary because it's keeping track of all the counts, and therefore needs to be accessible for update while `line` is being processed. We now see why keeping a dictionary of all the counts is a good idea - only one variable needs to be passed to our function, the dictionary, as opposed to three if we were storing the counts in three separate variables. Thinking things through in this way makes is easy to write out a function definition.

```python
def update_counts(line, counts_dict):
    pass


def create_report(file_path):
    counts_dict = {'sentences': 0, 'words': 0, 'characters': 0}
    with open(file_path) as txt_file:
        for line in txt_file:
            update_counts(line, counts_dict)
```

**Note**: While the names of the variables that we're passing to `update_counts()` are the same as the names of the parameters we defined in the function definition, this is not necessary. Sometimes this is useful so that it's easier to follow the flow of variables being passed between functions, and other times parameter names need to be more general because the function is performing a more general task.

What exactly does `update_counts()` need to do with a line? Well, we know that we're going to have to count the number of words in it, and the number of characters in those words. As for the number of sentences, this is a fairly difficult problem. One way that we could solve this is by counting the number of periods, ".", assuming that any sentences we will see will end in one. Admittedly, this is a fairly naive way to solve the problem; sentences can end with other punctuation (for example, exclamation points and question marks). This solution is also susceptible to the ellipsis, which has three periods all in a row. 

For now, we will neglect these obvious defects in our solution - we can always go back later to make it better. This type of practice is very regular when solving programming problems. As we've talked about, solutions are often built up in an iterative, testing as you go, manner. In addition, there's a decent chance that there are other edge cases that haven't even been considered. That's part of the beauty of using functions. Since they abstract away the implementation of counting sentences, words, and characters, we can later go back and change this single piece of our problem.

At this point, let's set up a small test case so that we can verify the functionality of `update_counts()`. Consider the string 'This is a test string. Only for testing'. We can see that it has 1 well defined sentence, 8 words, and 39 characters counting spaces. Let's set up a counts dictionary and test this string in an IPython environment.

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

As for counting the words, we can call `len()` on the results of the `split()` method, which will separate our string into individual words.

```python
In [5]: test_string.split()
Out[5]: ['This', 'is', 'a', 'test', 'string.', 'Only', 'for', 'testing']

In [6]: len(_)
Out[6]: 8

In [7]: counts_dict['words'] += len(test_string.split())
```

**Note**: The underscore, `_`, can be used in IPython to access the most recent output.

As for finding the number of periods within our string, there happens to be a very useful string method called `count()`.

```python
In [8]: test_string.count('.')
Out[8]: 1

In [9]: counts_dict['sentences'] += test_string.count('.')

In [10]: counts_dict
Out[10]: {'characters': 39, 'sentences': 1, 'words': 8}
```

With all of this testing done, verified by checking what's stored in `counts_dict`, we can now go back to our script and implement what we've found in `update_counts()`. The only difference is that the string that is accessible within its scope is named `line`.

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
    return counts_dict
```

We don't need to return anything from `update_counts()` because it is directly altering the state of `counts_dict`, which was one of the arguments it was passed. At this point we can now return `counts_dict` from `create_report()` and begin testing our full function.

To check how our function is working, we will need to have access to it. One way that we could use it is by adding some code to our script that calls the function. Possibly like this... 

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
    return counts_dict


print(create_report('test_text.txt'))
```

If we then run our script, we can see how or function is working.

```python

In [1]: run txt_file_processing.py
{'words': 16, 'sentences': 2, 'characters': 76}
```

#### Importing Detour

While this works, it turns out that it is generally bad practice. The reason has to do with what happens when we do something called importing. The **import** statement allows us to access code (generally functions and classes) from other existing scripts. These could be ones that are written by the creators of Python and are in libraries included with Python distributions, or ones that you've written yourself. We can test importing by trying to do it in IPython. Let's see what happens when we try to import the script we've just saved.

```python
In [1]: import txt_file_processing
{'words': 16, 'sentences': 2, 'characters': 76}

In [2]: txt_file_processing.create_report('test_text.txt')
Out[2]: {'characters': 76, 'sentences': 2, 'words': 16}
```

We can see importing in action here (the magic of the second line will be explained shortly). First, focus your attention on the first line. When we import a script, Python actually runs the code that is contained in the imported script, making it as though it was written in yours. While this is a very powerful concept, we can see a downfall here. The `print` function that we included in our `txt_file_processing` script was run when the import happened, and this is far from desirable behavior.

Luckily, we have a way to avoid this, and it's know as a **main-block**. Any code that is defined within a main-block will only be executed when the script is run, as opposed to when it is imported (in which case the contents of the main-block are ignored). We can see a main-block defined below.

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
    return counts_dict


if __name__ == '__main__':
    print(create_report('test_text.txt'))
```

Now, if we import the script we will not see the `print()` statement in the main-block run. Magic!

```python
In [1]: import txt_file_processing

In [2]: txt_file_processing.create_report('test_text.txt')
Out[2]: {'characters': 76, 'sentences': 2, 'words': 16}
```

Back to the second line here (its the same as above). Via importing, we gained access to `create_report()`, as it is stored in the `txt_file_processing.py` script. The syntax of importing allows us to do a number of other things as well. We can change the name that we will use to reference the script that contains the functions we want to access. We can do this from our import statement via the `as` statement. We can also import specific functions from a script using the `from` statement. These two statements can also be used together. Let's see them in action.

```python
In [1]: import txt_file_processing as tfp

In [2]: tfp.create_report('test_text.txt')
Out[2]: {'characters': 76, 'sentences': 2, 'words': 16}

In [3]: from txt_file_processing import create_report

In [4]: create_report('test_text.txt')
Out[4]: {'characters': 76, 'sentences': 2, 'words': 16}

In [5]: from txt_file_processing import create_report as cr

In [6]: cr('test_text.txt')
Out[6]: {'characters': 76, 'sentences': 2, 'words': 16}
```

All of this is very convenient, and we will use it extensively later in this course; for now, know that you can and often want to import from within a script to get access to functions from other scripts.

Back to testing. Now that we have importing and access to the main-block, we have convenient ways to test the code that we've written. We can either run the script using a test defined in the main-block or via importing the function and using it directly in IPython.

#### Abstraction Illustration

We've now verified the accuracy of our solution, and so you use `create_report()` to help your boss out with his problem. He tries it out on a couple of text files and is pleased with the results. Happy, you take the rest of the day off of work. The next day you come into work and you have an email in your inbox from your boss. It says that they tried to use `create_report()` overnight on a bunch of files and it took way too long - it was still running when they came back in the morning. You are told to make `create_report()` run faster.

Alright, I guess we didn't think about speed too much (if at all) while we were writing `create_report()`. So, what are we going to do to make it faster? Well, it might not be obvious at first, so let's walk though the code (specifically `update_counts()`) and think about what's happening.

On the first line of `update_counts()`, we count the number of periods in `line` and add that to the 'sentence' entry in `counts_dict`. On the second, we take `line`, split it apart on spaces, and add the number of words that come out to the 'words' entry of `counts_dict`. Lastly, we count the number of characters in `line` with `len()` and add that to the 'characters' entry of `counts_dict`. All of this makes perfect sense. So, how can we make it better? One way to make this better is by realizing that this approach is actually going over the contents of `line` 3 separate times to perform all of our updates. This isn't particularly efficient.

How can we make all of the necessary updates in fewer passes, then?? We'll, we could write our own loop to go over the line, character by character, and perform updates to the 'sentences', 'words' and 'characters' entries of `counts_dict` all within that loop. This is possible because we know that when we see a space we just finished another word, and when we see a period we just finished another sentence. Characters are self explanatory. Let's see what this might look like back in IPython.

```python
In [1]: test_string = 'This is a test string. Only for testing'

In [2]: counts_dict = {'sentences': 0, 'words': 0, 'characters': 0}

In [3]: for char in test_string:
   ...:     counts_dict['characters'] += 1
   ...:     if char == '.':
   ...:         counts_dict['sentences'] += 1
   ...:     elif char == ' ':
   ...:         counts_dict['words'] += 1
   ...:

In [4]: counts_dict
Out[4]: {'characters': 39, 'sentences': 1, 'words': 7}
```

This looks like it worked...wait! Does that say we only got 7 words?? We know that we're supposed to have 8. What happened?? Fixing these problems, either when our programs don't work and we're trying to make them functional, or ones that work but aren't giving us the expected output, is a process called **debugging**. Debugging can be very time consuming and frustrating, often because it's a super small error in your logic that is causing the problem. I find one good approach to debugging is isolating where the problem is occurring, and then stepping through the logic from that point. Being conscious about what you think the state of your program should be at each stage of execution, and then verifying that that state, is the approach that I take. Let's do that now for the for loop above, keeping track of what the character we're on is and what the counts in `counts_dict` are.

| Character  | sentences |  words  | characters |
| ---------- |:---------:|:-------:|:----------:|
| T          |  0        |    0    |     1      |
| h          |  0        |    0    |     2      |
| i          |  0        |    0    |     3      |
| s          |  0        |    0    |     4      |
|            |  0        |    1    |     5      |
| i          |  0        |    1    |     6      |
| s          |  0        |    1    |     7      |
|            |  0        |    2    |     8      |
| a          |  0        |    2    |     9      |
| ...        |  ...      |    ...  |     ...    |
| n          |  0        |    4    |     20     |
| g          |  0        |    4    |     21     |
| .          |  1        |    4    |     22     |
|            |  1        |    5    |     23     |
| O          |  1        |    5    |     24     |
| n          |  1        |    5    |     25     |
| ...        |  ...      |    ...  |     ...    |
| t          |  1        |    7    |     36     |
| i          |  1        |    7    |     37     |
| n          |  1        |    7    |     38     |
| g          |  1        |    7    |     39     |

Alright, that was straightforward (if a little time consuming), and we can immediately see the problem. We don't see a space after the last word in a line, so our algorithm doesn't add another word!! Alright, a simple solution to this is to add one to our word count after our loop. While it's fair to say that this solution fails in the case that the last character of a line is a space, we're going to ignore that edge case for now.  

```python
def update_counts(line, counts_dict):
    for char in line:
        counts_dict['characters'] += 1
        if char == '.':
            counts_dict['sentences'] += 1
        elif char == ' ':
            counts_dict['words'] += 1
    counts_dict['words'] += 1


def create_report(file_path):
    counts_dict = {'sentences': 0, 'words': 0, 'characters': 0}
    with open(file_path) as txt_file:
        for line in txt_file:
            update_counts(line, counts_dict)
    return counts_dict


if __name__ == '__main__':
    print(create_report('test_text.txt'))
```

```python
In [1]: run txt_file_processing.py
{'words': 16, 'characters': 76, 'sentences': 2}
```

Success!!!

While this may have seemed a somewhat contrived problem, the way we went about solving it and building upon it when we realized it needed better/smarter implementation was very much illustrative of how you should go about solving many programming problems.

I want to quickly draw your attention to how easy it was to speed up our program by changing the implementation of `update_counts`. This is abstraction in action! And say that later we're told to write a function that takes a list of file paths and creates a report for each one of them. Since we've wrapped up the functionality of our program in the `create_report()` function, doing something like that would be easy! We'd just make a new function that would loop through the list of file paths and call `create_report()`, passing the current file path in that iteration of the loop as the argument.

Hopefully this example has demonstrated a good workflow to follow when designing programs, and you've learned how to think about problems in an iterative top-down framework.
