# Instructions

As with your previous assignment, tonight's will get you practice with the data structures you learned about tonight. While most of the problems will be centered around tuples, dictionaries and sets, as they build on the structures you've already learned those will certainly be part of the questions and solutions you may come up with. 

# Assignment Questions

### Part 1 - Practice with Tuples

1. Write a script that prompts the user to input numbers separated by commas. Your script will take these numbers and store them as a list of tuples, taken two at a time, and print that to the user. If the user inputs an odd number of numbers only make a list of the largest number of pairs of two possible.
 
 Example: If you inputted the numbers `1, 2, 3, 4, 5, 6`, your script would print `[(1, 2), (3, 4), (5, 6)]`. If you inputted the numbers `1, 2, 3, 4, 5`, your script would print `[(1, 2), (3, 4)]`.

 **Hint**: Check out the [zip](https://docs.python.org/2/library/functions.html#zip) function.

### Part 2 - Practice with Dictionaries

1. Write a script that prompts the user to input numbers separated by dashes ( - ). Your script will take make and print a dictionary where the keys are the inputted numbers and the values are the squares of those numbers. 

 Example: If you inputted the numbers `1 - 5 - 8 - 10`, your script would print `{8: 64, 1: 1, 10: 100, 5: 25}`.

2. Write a script that prompts the user for a state name. It then checks against a dictionary it has written below to give back the capital of that state. However, it doesn't know the capitals for all the states. If the user inputs the name of a state that isn't in the dictionary your script should print that the capital is unknown.

```python
    state_dictionary = {'Colorado': 'Denver', 'Alaska': 'Juneau', 'California': 'Sacramento',
                        'Georgia': 'Atlanta', 'Kansas': 'Topeka', 'Nebraska': 'Lincoln', 
                        'Oregon': 'Salem', 'Texas': 'Austin', 'New York': 'Albany'}
```

 Example: If you inputted the state name `Kansas` your script would print `Topeka`. If you inputted the state name `Washington` your script would print `Capital unknown`.
  
  How could you make it so that your script isn't sensitive to the case of the inputted state? (**Hint**: one of the easiest ways is by changing the state dictionary slightly and using a method on your input string.)
