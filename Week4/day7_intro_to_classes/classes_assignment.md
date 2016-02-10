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

