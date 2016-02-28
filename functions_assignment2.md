# Instructions 

Tonight we'll work through building functions and getting practice with their syntax. We'll begin by having you complete function definitions that are already written, and then move on to you writing function definitions for code that is already written. Next, we'll work on translating some of the code we've already written into functions. We'll finish up by writing some functions of our own, from start to finish.  

# Warmup 

For the first set of problems below, fill in the given function definition to achieve the desired results.  

1. Remember the song '99 bottles of beer on the wall'? Well, we've written a function that will take in a number (`n`), and we want you to complete it such that it prints a line from the song. `n` will hold the number of bottles of beer on the wall, and we want you to complete the function assuming that there are `n` bottles of beer on the wall. After completing it, test that it works by calling it some number of times. 

```python 
def calc_beers_on_the_wall(n=99): 
    """Print how many beers remain on the wall. 

    Args: 
        n: int
            Holds the number of beers that remain on the wall. 
    """
    pass
```

* What does it mean for me to write `n=99` in the function definition, as opposed to just `n`? Try calling your function both with and without an argument given - what happens in each case? Why does this happen?
* Change the `99` to `50`. What do you expect to happen? Call your function, and verify that you get the intended results. 

2. Remember [Elsa](http://pre11.deviantart.net/7144/th/pre/f/2014/027/b/d/let_it_go_by_impala99-d740xws.png) from `Frozen`? We've heard mixed reviews of her song 'Let it go'. We've written a function below that will take in a boolean (the `fan` parameter), where this boolean holds whether or not a person is in favor of 'Let it go' (i.e. if `fan` is `True`, they are in favor, and if it is `False`, they are not in favor). We want you to complete the function such that: 

* If the person is a fan, then it prints "I love Elsa! She's my favorite!"
* If the person is not a fan, then it prints "Let it go, it's not that great."

```python 
def check_elsa_fan(fan): 
    """Print a certain phrase depending on the value of fan. 

    Args: 
        fan: boolean 
    """
    pass
```

* Change the function definition so that it **defaults** to the person being a fan. Try calling your function both with and without arguments now - how does this effect what gets printed out? 

 

