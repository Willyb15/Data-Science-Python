# Instructions

Tonight we'll be working on building out the `OurClass` class that we looked at in lecture, as well as building out another class that we'll have interact with `OurClass`. We'll call that class `Member`. Your goal by the end of the night is to implement these classes by following along with the guidelines below (i.e. implementing the classes with the attributes and methods discussed below), such that you have a firmer grasp on building your own classes and having them interact with each other.  

# Assignment Questions

### Part 1 - Building out `OurClass`

We're going to rework `OurClass` a little. As a reminder, here is what we settled on during lecture: 

```python
class OurClass(): 
    
    def __init__(self, name, location, size=0): 
        self.name = name
        self.location = location
        self.size = size
        self.questions_asked = []
        if self.size >= 20: 
            self.at_capacity = True
        else: 
            self.at_capacity = False
   
   def add_question_asked(self, question): 
        self.questions_asked.append(question)
        
   def add_class_members(self, num): 
        self.size += num
    
        if self.size >= 20: 
            print 'Capacity Reached!!'
            self.at_capacity = True
    
   def check_if_at_capacity(self): 
        return self.at_capacity
``` 

1. The first thing you are going to do is to remove the `add_question_asked` method from `OurClass`. You can also remove the `questions_asked` attribute that is stored on the class, too. In terms of the `add_question_asked` method though, we are going to end up moving it into the `Member` class we will build, so it might be a good idea to keep that code in your back pocket.  
2. Next, you should do is to add an attribute to the class called `members`. Modify the `__init__` function so that it takes an additional parameter, called `members`, which will be stored as the `members` attribute on the class. This `members` attribute should be a list that is by default empty, but is assigned the `members` parameter if it is passed into the `__init__` function.  
3. Now, alter the `add_class_members` method in `OurClass` to not take in a number (e.g. the `num` parameter), but instead a new member. Change the function definition to take in that member parameter, and then add that member to the `members` list attribute of the class. You should keep the rest of the code the same (i.e. adding 1 to the `size` attribute of the class and checking the `at_capacity` attribute of the class).  

### Part 2 - Building out the `Member` class

Now we're going to start working on the `Member` class. Then we'll cycle back to actually have the `Member` class interact with the `OurClass` class.

1. Start out and define the `Member` class. Construct it such that users of the class need to instantiate it with an inputted `name`, `hair_color`, and `birthdate` (i.e. these will be accepted in the `__init__` method.  
2. Now, alter the `__init__` such that it creates a `questions_asked` attribute that starts out as an empty list.  
3. Build a method called `add_question_asked` that takes in `question` as a parameter and adds it to the `questions_asked` attribute on the `Member` class.  
4. Build a new method into the class called `add_coded_line` that takes in a string (of supposed code), and appends that string to an attribute called `lines_of_code` (you'll also have to add this to the `__init__` method). Also in that method, increment an attribute called `num_lines_coded` (you'll also have to add this to the `__init__` method). 
5. Now, let's build upon that `add_coded_line` method. Within that method, we're going to call another method, called `get_coding_level`, that we will now create. In `get_coding_level`, we want to determine what the coding level is of our `Member`. If they've coded less than 100 lines of code, they will be a `beginner`; more than 100 but less than 1000, a `novice`; more than 1000 but less than 10000, an `intermediate`; and greater than 10000, a `master`. So, `get_coding_level` should use the attribute to determine what `coding_level` the `Member` is at. Note that this means you will have to do a couple of things: 

* Define the `coding_level` attribute on the `Member` class. Initialize it to be `novice`. 
* Define and build the `get_coding_level` method, as described above. 
* Anytime that you add a line of code in the `add_coded_line` method, check if adding that line of code puts the `Member` at a new coding level by calling the `get_coding_level` method.  

