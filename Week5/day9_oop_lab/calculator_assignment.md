## Reverse Polish Notation Calculator

Your assignment today is to implement a program that functions as a calculator; but not just any calculator, a reverse polish notation calculator. There's a good chance you've never heard of this particular flavor of calculator so here's a quick overview.

### Reverse Polish Notation

Many of us are solely used to entering computations into a calculator by putting an operation between two values. E.g.

| value | operation | value |
|:-----:|:---------:|:-----:|
|   3   |     +     |   4   |

However there are other notations that can be used to express mathematical operations, prefix, also known as Polish, notation and postfix, also know as Reverse Polish, notation. Today we will be implementing a calculator that implements Reverse Polish Notation ([RPN](https://en.wikipedia.org/wiki/Reverse_Polish_notation)). E.g.

| value | value | operation |
|:-----:|:-----:|:---------:|
|   3   |   4   |     +     |

This method of inputting computations actually makes it easier to write logic, for the computer, to perform the operations. This is because the format lends itself to storing computations in a [stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)). A stack is a specific type of queue (know as last in, first out, LIFO)  which only supports two types of operations, pushing and popping.

You can think of a stack as a list with less functionality. (**Note**: the [deque](https://docs.python.org/2/library/collections.html#collections.deque) class is the closest native Python class to a stack. When you go to implement you're version of a RPN calculator today you can choose to use this class instead of a list as it will technically give you speed gains on the pushing and popping operations you will need to perform over the same functionality being implemented with a list.) What a RPN calculator does is accept input one element at a time, these elements can either be values or operations, and pushes them, in turn, onto the stack; in Python list lingo, appends them to a list. When the user wants to perform an operation the correct number values necessary to perform the operation are [popped](https://docs.python.org/2/tutorial/datastructures.html) off the stack, in turn. The value resulting from that operation is then pushed back onto the stack. If it is the last value on the stack then that value is returned, else the process starts over again.

### RPN Example

Say we want to calculate, in infix notation, the value resulting from the calculation: `6 + ((5 + 3) / 4) - 3`. In RPN that calculation is written: `6 5 3 + 4 / + 3 −`. To input this calculation into a RPN calculator one would enter those elements, in turn, and the corresponding operations would occur in the following order.

| Input |  Operation   |    Stack    |                   Other                   |
|:-----:|:------------:| ----------- |:-----------------------------------------:|
|   6   |  Push Value  | [ 6 ]       |                                           |
|   5   |  Push Value  | [ 6, 5 ]    |                                           |
|   3   |  Push Value  | [ 6, 5, 3 ] |                                           |
|   +   |     Add      | [ 6, 8 ]    | Pop two values (3 then 5), push result, 8 |
|   4   |  Push Value  | [ 6, 8, 4 ] |                                           |
|   /   |    Divide    | [ 6, 2 ]    | Pop two values (8 then 4), push result, 2 |
|   +   |     Add      | [ 8 ]       | Pop two values (2 then 6), push result, 8 |
|   3   |  Push Value  | [ 8, 3 ]    |                                           |
|   -   |   Subtract   | [ 5 ]       | Pop two values (3 then 8), push result  5 |
|       |    Return    |   5         |                                           |

If you want to play around with a RPN calculator to get a feel for them and how they operate check out [this](http://www.meta-calculator.com/learning-lab/reverse-polish-notation-calculator.php) link.

### RPN Calculator

Your assignment is to implement a calculator that operates with reverse polish notation. This can be done with solely functions, and while this is supposed to be an OOP lab, if you'd like you're welcome to start off by writing functions that solve the problem. Though, at some point in the assignment there will be a part that nearly necessitates implementation of the calculator with OOP.

The following steps are suggestions, and while they could possibly make your journey through this programming assignment easier, they do not need to be followed. Remember, there is always another way to solve any problem when programming. Sometimes there's an obvious solution, sometimes not so much. Sometimes there's a more elegant solution, sometimes they all function about the same. At a high level, the purpose of this lab is to have you work through a problem, on your own, start to finish, so you can get a good feel for what that process is like. In addition the instructors will be around if you have any questions or concerns about how you are wanting to implement your solution.

You are encouraged to talk about the problem with your classmates and/or the instructors at any time; frequently one of the biggest hurdles when trying to solve a problem is trying to figure out what the problem actually is. Trying to explain it to someone, and having a conversation about it can go a long way towards understanding the problem fully.

#### Step 1: Interact with the Problem at a High Level

Take a look at wikipedia's description of the [algorithm](https://en.wikipedia.org/wiki/Reverse_Polish_notation#Postfix_algorithm) for evaluating a string of operations in RPN. This is a great outline of what your program will need to be able to do. Follow along with the example, making sure you understand how the algorithm is evaluating the sequence and what the state of the stack is at each step.

#### Step 2: Devise a Plan

With the RPN algorithm for computing a string of numbers and operations in mind you're going to want to write a function that takes a string of characters as computes the result of that computation.

In line with the top-down tactics that we have previously discussed, consider how this problem can be broken down into smaller pieces that are easier to be solved. What will the big problem be then? Consider making a function that will take a string of elements, separated by spaces, and evaluate them with a stack like storage procedure (LIFO queue). Some questions to ask yourself:

* What would that function look like? 
* What would you call it? 
* What parts of what it needs to do could be assigned to other functions? 
* What would they be called?

Once you have answered some or all of these questions you are well on your way to writing some pseudocode.

#### Step 3: Pseudocode

Now that you've moved from the outline of the algorithm to thinking about how you will task out parts of it to functions you are in a great position to begin pseudocoding. Pseudocode can take on a variety of different appearances. It can be simple notes to yourself about steps you want to take. It can be instructions that are semi-code like, e.g. if you're going to loop over some container you might write a line of pseudocode that looks like `for thing in stuff`, giving better names to each thing and the stuff. It can be almost functioning code.

The nice thing about pseudocode in Python is that you can write in nearly accurate Python syntax. While variables you want to reference or functions you want to call might not exist yet this isn't a problem, its just pseudocode! Then when you want to go fill in the pseudocode, and make it code, you already have lines that will work in Python and you should have great names for everything you'll need to name. For example, if I'm trying to solve a problem that needs to loads a list of words then loops through that list and makes a dictionary with the number of words of different counts my pseudocode might look like:

```python
def get_word_count_dict():
    word_list = load_word_list()
    count_dict = make_count_dict()
    return count_dict


def load_word_list():
    with open get file(s):
        load words from files to list
    return word_list


def make_count_dict():
    for word in word_list:
        build up dictionary
    return dictionary
```

Now that this skeleton exists it's easier to see what types of parameters each function will take and think about how the whole program will flow. You might notice that both `load_word_list()` and `make_count_dict()` will need to accept parameters. But that's way easier to see than when you first thought about how to solve the problem.

#### Step 4: Implement Real Code

Now that you have a really good, nearly code-like, structure for your program to create a function to calculate a RPN operation you can go through and make the pseudocode working code by filling it in and building out functionality. Along the way you'll start seeing places where you can make functions out of certain routines that do their own thing and/or are run in a loop, and that's great! You're well on your way to a working program.

#### Step 5: Debug

Once you get your code to a state where it can run you're at the point of debugging. There's a chance that you won't need to go through this step, but it way more likely that there will be some small error or something you didn't account for in your first solution, so you'll need to go through your code and figure out where the error lies.

Don't fret, this is part of the programming process, even the best programmers have to debug their code, embrace it. It means you're making mistakes and learning!

There are many methods by which you can debug. You can read through your code for syntax/logic errors, you can print things out to make it easier to follow the flow of your program as it actually runs. You can also use the Python Debugger, [pdb](https://docs.python.org/2/library/pdb.html) for short. This tool can be really helpful if you want to interact with your program similarly to way you interact with IPython, it allows you to stall the state of the Python interpreter while it is running your script so that you have a chance to poke around and see the state of your program, the variables that exist, what their values are, etc., at any point in the execution. Check out this [blog post](https://pythonconquerstheuniverse.wordpress.com/2009/09/10/debugging-in-python/) for a great intro on using this tool.

#### Step 6: Persist the Stack

Now you have a way 
