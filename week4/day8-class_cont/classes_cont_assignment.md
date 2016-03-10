# Instructions

Tonight we're going to be taking a look at classes, and the OOP paradigm in general. The problems in this assignment are designed to help you develop an intuition for, both, why we like object oriented programming, **and** when we want to use it. The first part of this assignment will revolve around taking a problem that has been solved with functions, which will be given to you, and turning it into a class. The second part will have you write a class from scratch, starting from the mindset of functions. The last part will gave you a problem that has been solved with a class; however, it will be a poor choice of using OOP. Here you will turn the class back into just functions to see how plenty of problems still ought to be solved with functions. 

# Assignment Questions

### Part 1 - Functions to Class

Imagine you are, while you're learning Python, waiting tables on the side. At the end of each night you have to find all you're bills and total the amount that you will be tipped out depending on what a client decided, or 18% if they didn't specify. You always end up spending an extra 10 minutes at the end of your shift calculating how much you made in tips so you decide to write a Python script to help automate the task.

After a little trial and error you came up with the functions below. The `0.18` is for the standard tip your restaurant charges if none is specified.

```python
def get_tips(bills_n_tips):
    return [bill * tip for bill, tip in bills_n_tips]

def add_bill_update_tips(new_bill, bills_n_tips, tip_rate=0.18):
    bills_n_tips.append((new_bill, tip_rate))
    tip_out = sum(get_tips(bills_n_tips))
    return tip_out
```

You tested them out as well with the following function. Cause who doesn't like well tested code??

```python
def test_tip_out():
    waiter_bills_n_tips = []
    print add_bill_update_tips(58.90, waiter_bills_n_tips, 0.15)
    print add_bill_update_tips(31.58, waiter_bills_n_tips) 
    print add_bill_update_tips(81.44, waiter_bills_n_tips, 0.20)
    print get_tips(waiter_bills_n_tips)
    print len(waiter_bills_n_tips)
```

As everything appeared to be working you happily went to work and kept track of your tips. Everything actually worked out, as you expected, I mean, you did your due diligence and tested. However, running the same function over and over, having to make sure that you we're passing the correct things to your function while you were trying to work quickly became a burden. In addition, some of your coworkers saw what you were doing and wanted to try next time you worked. You wonder to yourself if there is a simpler way to implement a solution to this problem, one where anyone could easily and intuitively use the program your wrote.

Luckily, you think to yourself, you learned about classes in Python class recently and realize that this is a great situation to employ your newfound tool! The first thing you do is sit down and think about how you'd want to use a class that allowed you to track and get information about the status of your tips. Here's an example usage of the class you're going to build that you come up with:

```python
tot = TipOutTracker(0.18)
tot.add_bill(58.90, 0.15)
tot.add_bill(31.58)
print tot.total_tip_out()
tot.add_bill(81.44, 0.20)
print len(tot)
```

Here, when you get the length of your tracker you are actually going to get the total amount that the tracker knows you're supposed to be tipped out.

With this in mind, your task is to take the code from the function solution of this problem and write a class `TipOutTracker` that will operate in the way shown above. The things that you should be thinking about as you start solving this problem are:

* What are the attributes, data, that you are going to store on the class?
* What are the methods, functions, that you are going to operate on the attributes with?

### Part 2 - Classes from Scratch

Now that you have a little bit of practice thinking about a problem that takes a solution from functions to a class, you're going to get some practice solving a problem from scratch with OOP.

This time you are going to create a class that allows you to keep track of a to-do list. The kinds of things that we'd want to be able to do with a to-do list (no pun intended) are:

* Add a to-do item.
* Mark a to-do item as done and remove it.
* Print all of your current to-do items.

As you work through this problem a good place to start is by thinking about how you'd want to use this class that you're about to right as was done in the first problem. If you were to be given a `ToDo` class, how would you want to use it? Go ahead and write up a test case where you "use" the class that you're about to write. This will help get you into the mindset of how the class will actually work.

With that in mind you're going to want to answer the same questions that were posed in the previous question:

* What are the attributes, data, that you are going to store on the class?
* What are the methods, functions, that you are going to operate on the attributes with?

Once you have an idea about the answers to these two questions you'll be in a great place to start writing some code!

### Part 3 - Times Not to Use Classes


### Extra Credit

Make it so you can add tipouttrackers

Add a done list of to-do items to the todo list class. Add priority to the todo list items, have these priorities change the way your items are stored and displayed.
