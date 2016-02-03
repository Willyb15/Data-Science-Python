## Instructions 

Tonight we'll be working through problems designed to get your hands on everything you learned tonight - strings and lists (and their methods), along with iteration using for loops. The goal of tonight is to get more comfortable with Python, and working with its data structures. We're also going to work on getting more familiar with some of the methods that are available to us for interacting with strings and lists. Remember that from the IPython terminal, we can find any of the methods that are available on an object via tab completion. That should come in handy tonight! 

### Assignment Questions 

#### Part 1 - Practice with `For` Loops

For the first part here, take a couple of the scripts we wrote in the `intro_python_assignment.md` in Week 1, Day 2, and change them from using `while` loops to using `for` loops. Start out and just do the first two (for extra practice you could do this with the rest of the problems we worked through):  

1. Write a script that computes and prints the factorial of a user inputted number.
2. Write a script that determines whether or not a user inputted number is a prime and prints 'The number you inputted is a prime/ not a prime number.' depending on what your script finds.

Remember, the goal is to write these by using `for` loops. 

#### Part 2 - Practice with Strings

Now you're going to work with strings, along with your knowledge of `for` loops and iteration. Remember that you can tab complete to find helpful methods that you can use to operate on strings! For some of these problems, you may not use anything new, but for others, there may be a helpful string method. As a last note, just like with many programming problems, there will be multiple ways to solve these problems. 

1. Write a script that obtains the count of a user inputted letter in a user inputted string (**Hint**: Use `raw_input()` twice to get both of the user inputs). Make sure to build this in such a way that it ignores the case of the inputted string and letter. 
2. Write a script that checks if a user inputted string ends in an exclamation point. **If it does**, then print the string in all capital letters. **If it doesn't**, print the string in all lowercase letters.  
3. Write a script that removes all of the vowels in a user inputted string.
4. Write a script that makes every other letter of a user inputted string capitalized. 

#### Part 3 - Practice with Lists 

1. Write a script that creates a list of only the even numbers between 0 and a user inputted number. 
2. Write a script that creates a list of only numbers divisible by a user inputted number that are between 0 and a user inputted number (**Hint**: Use `raw_input()` twice to get both of the user inputs). 
3. Given the list `[0, 3, 6, 9, 10, 2, 5]` and `[2, 6, 4, 7, 8, 1, 15]`, write a script that finds the common elements between them. Store them in a list, and print that list, sorted, as the final output (if you'd like you can go ahead and hard code those lists in your script).  
4. For a user inputted number, write a script that outputs a list of multiples of that number from 0 up to another user inputted number. For example, given the numbers 4 and 20, your script should print the numbers 4, 8, 12, and 16.

#### Extra Credit

Alter your script in Part 3, Question 3 to accept arbitrary lists. Build it such that the user has to enter 8 numbers (each separated by an enter at the command line) for each list. 
