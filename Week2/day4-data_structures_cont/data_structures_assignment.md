# Instructions

As with your previous assignment, tonight's will get you practice with the data structures that you learned about in lecture. While most of the problems will be centered around tuples, dictionaries, and sets, they will also build on the structures that you've already learned about. 

# Assignment Questions

### Part 1 - Practice with Tuples

1. Write a script that prompts the user to input numbers separated by commas. Your script will then take these inputted numbers numbers and store them as a list of tuples, two at a time. Finally, your script will print that list of tuples to the user. If the user inputs an odd number of numbers, then only make a list of the largest number of pairs of two that are possible.
 
 Example: If you inputted the numbers `1, 2, 3, 4, 5, 6`, your script should print `[(1, 2), (3, 4), (5, 6)]`. If you inputted the numbers `1, 2, 3, 4, 5`, your script should print `[(1, 2), (3, 4)]`.

 **Hint**: Check out the [zip](https://docs.python.org/2/library/functions.html#zip) function. While you don't have to use it, it could things easier. 

### Part 2 - Practice with Dictionaries

1. Write a script that prompts the user to input numbers separated by dashes ( - ). Your script will take those numbers, and print a dictionary where the keys are the inputted numbers, and the values are the squares of those numbers. 

 Example: If you inputted the numbers `1 - 5 - 8 - 10`, your script should print `{8: 64, 1: 1, 10: 100, 5: 25}` (remember that dictionaries are unordered, which is why the script might print out the key-value pairs in a different order than the user inputted the numbers). 

2. Write a script that prompts the user for a state name. It will then check that state name against the dictionary below to give back the capital of that state. However, you'll notice that the dictionary doesn't know the capitals for all the states. If the user inputs the name of a state that isn't in the dictionary, your script should print that the capital is unknown.

 ```python
    state_dictionary = {'Colorado': 'Denver', 'Alaska': 'Juneau', 'California': 'Sacramento',
                        'Georgia': 'Atlanta', 'Kansas': 'Topeka', 'Nebraska': 'Lincoln', 
                        'Oregon': 'Salem', 'Texas': 'Austin', 'New York': 'Albany'}
 ```

 Example: If you inputted the state name `Kansas`, your script should print `Topeka`. If you inputted the state name `Washington`, your script should print `Capital unknown`.
  
  How could you make it so that your script isn't sensitive to the case of the inputted state? (**Hint**: one of the easiest ways is by changing the state dictionary slightly and using a method on your input string.)

3. Write a script that will continually prompt the user for a set of three things to be separated by commas. The first two things will be (x, y) coordinates of the word that follows (the word will be the third thing). So the user will input a string that is formatted like `x, y, word`. Your script will use the string to build a dictionary with the first two inputs (i.e. the (x, y)) from each string as keys to a dictionary, and the third input (the word) as the value for that key. The script will continually prompt the user to input strings in this format until the user inputs nothing (i.e. hits enter with no input).

 After building the dictionary, your script should allow the user to query the dictionary it built by accepting strings of the format `x, y`. It should check if the coordinate is in the dictionary, and if it is return the corresponding word. If it isn't, it should print `Coordinate not found`. This should continue until the user inputs the letter `q`, at which point the script should exit.

 Example usage:
 ```
 Please enter a coordinate-word pair in the format (x, y, word): 1, 2, hello
 Please enter a coordinate-word pair in the format (x, y, word): 2, 3, world 
 Please enter a coordinate-word pair in the format (x, y, word): 
 Please enter a coordinate to look up: 2, 3  
 world
 Please enter a coordinate to look up: 3, 4
 Coordinate not found
 Please enter a coordinate to look up: q
 ```

### Part 3 - Practice with Sets

1. Write a script that prompts the user to input a list of numbers separated by commas, and then does so again. It should then print those numbers that were common in both entries.

 Example: If you inputted the numbers `1, 2, 3, 5, 6` first, and `2, 3, 4, 6, 7` second, your script should print `2, 3, 6`. Make sure to use sets, as they are optimal for this problem. 
 
 **Hint**: For the output to be formatted in the prescribed way you could use the `join()` method available on strings.

2. Write a script that prompts a user to input a list of words separated by commas, and then prints out the unique words in the list. 

 Example: If you inputted the words `hello, there, how, are, you, hello, you`, your script would print `how, you, there, hello, are`.

3. Write a script that continually accepts words from the user. As it goes does it will add words to a set. If the user enters the letter `v` your script will display all the known words, it's vocabulary. This will continue until the user enters the letter `q` which will quit the program.

 Example usage:
 ```
 Enter a word to add to the vocabulary: thing 
 Enter a word to add to the vocabulary: stuff 
 Enter a word to add to the vocabulary: v
 thing stuff
 Enter a word to add to the vocabulary: hello
 Enter a word to add to the vocabulary: v
 thing stuff hello
 Enter a word to add to the vocabulary: q
 ```
