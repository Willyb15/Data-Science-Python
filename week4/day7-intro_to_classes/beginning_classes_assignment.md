# Instructions 

Tonight we'll work through building classes and getting practice with their syntax. We'll begin by having you complete class constructors that are already written, and then move on to having you write class constructors for some code that is already written. After that, we'll move on to building a class or two of our own!

For each of the classes you build tonight, you should test them out. Try instantiating a couple of different instances of each class you build, and make sure they work the way that you would expect. A couple of questions to ask yourself are: 

* If I tab complete, do I see the attributes/methods that I would expect?
* If I examine an attribute of my instantiated class/object, is it's value what you would expect?
* Do the methods that you've defined in your class work as expected for your instantiated class/object?

# Warmup

For the first set of problems, we'll give you class constructor and ask that you fill it in according to some specifications. 

1. Let's make a `Dog` class. In this dog class, we've gone ahead and given the skeleton for the `__init__` method, as well as a `wag_tail` method. We want you to fill these in such that: 

* In the `__init__` method, we assign to our `Dog` class a `name` attribute and a `happiness_level` attribute. 
* In the `wag_tail` method, the `Dog` "wags it's tail" for the inputted `n` number of times, and each time it wags it's tail, it's `happiness_level` increases by 5. 

```python 
class Dog(): 
    """This docstring will discuss how to interact with our Dog class. 

    Our Dog class will have two attributes - a name and happiness_level. 
    It's one method, wag_tail, will simulate the dog wagging it's tail 
    some number of times, and increasing it's happiness level. 

    Parameters: 
    -----------
        name: str
        happiness_level: int
    """
    
    def __init__(self, name, happiness_level=5): 
        pass

    def wag_tail(self, n): 
        """Wags the dogs tail n times, each time increase happiness level by 5. 

        Args: 
            n: int
        """
        pass
```

* What does it mean for me to have put an `=5` after the `happiness_level` parameter in the `__init__` method?
* Why do I have to pass self as the first argument in both the `__init__` method and the `wag_tail` method?

