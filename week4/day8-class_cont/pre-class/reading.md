# Notes

This document will be present a framework for choosing to use OOP in Python. This is important because the programming problems that you will work on in the future might lend themselves to be solved procedurally, with top-down, as you learned about last week; but, plenty will be better solved with OOP techniques. Frequently you can solve a problem with either, however it's better to use the right tool for the job. This means knowing how to reason about what the right tool is.

With this in mind, the rest of the document is devoted to presenting some programming tactics and discussing them in a general framework. This may not seem like "programming"; however, learning these meta skills will both allow you to solve increasingly difficult problems and solve them in decreasing amounts of time.

## Making Proper Use of OOP

Now that you've learned about objects and how they intuitively provide a way for you to model the world with code via classes you might be thinking about all the amazing use cases for this new paradigm. An important thing to note is that not every problem is suited to being solved with OOP. But it is easy to think that every programming problem looks like a nail when you have a hammer as big as OOP. So how can you tell whether to use functions or classes when you're writing a solution to a programming problem?

Unfortunately there is no cut-and-dried answer to this question. But there are some simple ways to think about how to make this choice in addition to some tools that will make transitioning from one solution, functions or classes, to the other. In addition, you can always use a mixture of functions and classes, so know that you're not making a mutually exclusive choice.

The most straightforward way to determine if something should be a class is to ask yourself if that class would be making use of any of those design principles that we talked about in the last lecture: *inheritance*, *encapsulation*, and *polymorphism*. The most frequent of these that will motivate the choice to use classes is encapsulation, so we'll be focusing on that. (You can read some about why inheritance isn't most people's favorite [here](https://en.wikipedia.org/wiki/Composition_over_inheritance), and we'll talk a little about leveraging polymorphism during lecture and see examples of it later in the course.)

## Thinking About Encapsulation

What encapsulation comes down to revolves entirely around how a class is composed. Remember that a class can have both data, *attributes*, and functions that act on/with that data, *methods*. It is the act on/with part that is important here. While you can have classes that simply group together data by making them attributes, see the code below, this is not worthwhile as the same result can be achieved with a data structure such as the [named tuple](https://docs.python.org/2/library/collections.html#collections.namedtuple).

```python
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
from collections import namedtuple
NTPoint = namedtuple('Point', ['x', 'y'])

my_point = Point(3, 5)
nt_point = NTPoint(3, 5)
print 'From Point class: ({}, {})'.format(my_point.x, my_point.y)
print 'From namedtuple: ({}, {})'.format(nt_point.x, nt_point.y)
```

So what is it that makes classes worthwhile? Much of the power in classes comes from the encapsulation, in that **both** the data, attributes, and ways to act on it, methods, are house within the class. This means that, as the writer of a class, you an provide easy ways for the user of your class to interact with it via methods. This is something that can't be done with just attributes or, e.g., a named tuple.

So, when you're trying to decide if you should be using a class or a function to solve your problem an good questions to ask yourself are:

* What data would be the attributes of your class?
* What ways would you provide to act on that data, aka, what would be the class' methods?

If you can't answer these questions then it's probably better to just write functions for now. If you can, then you're probably justified in going down the OOP route. I frequently start writing solutions with functions and if I find myself writing a lot of them that are acting on the same group of data then I'll begin to think about moving to a class.

## What if You Make the "Wrong" Choice?

There will be plenty of times when you're working on a solution and you decide that using a different paradigm will be better than your current one. Never fear, you can always refactor! **Refactoring** is the process of changing your current code, technically, without changing it's external behavior. Note that this is only really possible if you were writing modular, well abstracted, code, either with functions or with classes. What refactoring amounts to is changing the implementation within one of more layers of your abstracted solution. At the top layer, though, nothing looks different. 

Refactoring functions into classes usually just looks like making the data your passing between each function an attribute on the class, making the functions methods and adding `self` in a lot of places. Going from a class to functions usually looks like the exact opposite.

Because of the general lack of difficulty in moving between a class and functions and back (unless there are a lot of dependencies that you haven't modularized) it's generally not too painful to try if you're wondering what an implementation of your solution would look like in the other paradigm. If you start making the change and unforeseen complications arise, e.g. it's unnatural to keep track of a counter that was a class attribute when you try to change to functions, or things just look sloppy in the new paradigm, then go back to your previous solution!

### Git to the Rescue

Considering that you will, at some point, want to undertake a refactoring of your code, it's good to know about the existence of branches in git. Remember that git is the version control system that we use to keep track of the changes that we make to our code via adding and committing? It turns out that you have the option to go through this process of changing, adding and committing without effecting the current state of your code. WHAT?? How is this possible, you ask? With branches.

Branches are a git tool that allow you to maintain your git repository in more than one state, aka on more than one branch. Your main branch is called `master`, and it is generally reserved for changes that you know you want to make. You can, however, add other branches, which, when you do work on, will not effect `master`. When you initially make your new branch it's state will be the same as master, but the changes you make to it won't change master. Aka, you'll be committing to the new branch, not master.

This is a great way to test out something, e.g. a refactoring of your code, without changing a bunch of working code and putting it in a state that's potentially difficult to fix. The cool part comes in when you decide that the changes that you've made on your separate branch are good. At this point you would like master to have those changes. Luckily it's very simple to put the branches changes into master. It's done with a merge.

The one thing that can make this process go wrong is when their are commits to the same file as are being changed in the new branch as on master. At this point git doesn't know which changes you want master to have. This results in what's known as a merge conflict. Merge conflicts aren't fun, but they are fixable.

For a great intro to the ideas of branching and merging check out [this](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) page of the git documentation.
