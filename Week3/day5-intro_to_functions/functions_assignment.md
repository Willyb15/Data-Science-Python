# Instructions 

Tonight we'll be working through solving more problems, but this time by building functions.  For each of the problems that you work through tonight, you should build a function into your solution. While we'll discuss general workflow in the next class, tonight you can just build each function into it's own file, and then call it with some arguments right after you define it. For example, pretend all of the following is the solution to one of the problems, written in a function first and then called (for testing purposes) below. 

```python 
def my_func(param1, param2, param3): 
    # Function code to solve the problem

print my_func(param11, param21, param31)
print my_func(param12, param22, param32)
print my_func(param13, param23, param33)
print my_func(param14, param24, param34)
print my_func(param15, param25, param35)
```

Note above that I called my function five times after I defined it (and I put a print in front of it so that when I call the script from the command line it'll print the results) - this is to test out that it works correctly with different sets of arguments. You should aim to test yours at least 5 times tonight after you write it. 

# Assignment Questions 

### Part 1 - Basic Practice 

For the first part of the assignment, we're going to get some practice taking something we've already written and translating it to a function. In continuation of prior assignments, let's work with a couple of the scripts that we wrote in `intro_python_assignment.md` in Week 1, Day 2, and then re-worked in `strings_lsts_assignments.md` in Week 2, Day 1. Let's start out and just move the first two into functions (for extra practice you could do this with the rest of the problems that we worked through in those assignments): 

1. Write a function that computes the factorial for an inputted number.  
2. Write a function that determines whether or not an inputted number is a prime, and then prints 'The number you inputted is a prime/ not a prime number.' depending on what your script finds (Note that this means putting a `print` in front of the function when testing it will be redundant for this case). 

### Part 2 - Advanced Practice 

Now we're going to work our problem solving and programming chops even more by coding up functions to solve new problems. For each of the problems below, I would suggest coding it up in a similar way to how you did the other two (building the function, and then calling it some number of times (5) to test it out after that). 

1. Write a function that counts the number of words in an inputted string, where we consider spaces to be word separators. 
2. Write a function that counts the number of words in an inputted string, where we consider words to be separated by an inputted delimiter (so you're function should accept two arguments), where the default delimiter used is a space.  
3. Write a function that takes in a string, and returns a list that holds the length of each word in the phrase, separated by an inputted delimiter (so you're function should accept two arguments), where the default delimiter used is a space. For an example here, if the arguments to your function were `This is a test string` (and nothing else), your function should return `[4, 2, 1, 4, 6]`.   
4. Write a function that returns all the prime numbers up to an inputted number (**Hint**: It might be helpful to use/modify the prime function you wrote earlier.    
5. Write a function that takes in a list of numbers, as well as an additional number (i.e. two arguments), and returns a list of `yes` or `no` as to whether each number in the list is divisible by the additional number. For example, if I input `[10, 25, 36, 12, 20]` as the list of numbers, and `5` as the additional number, your function should return `['yes', 'yes', 'no', 'no', 'yes']`.
6. Write a function that takes in a list of strings, as well as an inputted letter, and returns a list of only those strings from the list that end with that letter. For example, if I input `['I', 'am', 'in', 'love', 'with', 'python']` as the list of strings, and `n` as the inputted letter, your function should return `['in', 'python']`.
7. Write a function that takes in a list of strings, as well as an inputted substring (i.e. another string), and returns a list of the indices of the strings that contain that inputted substring. For example, if I input `['This', 'is, 'an' , 'example']` as the list of strings, and `is` as the substring, your function should return `[0, 1]`.

### Extra Credit

1. Let's build a calculator for figuring out how much I owe in taxes (and by calculator, I mean function). Write a function that takes in a dictionary and an income. In the dictionary, the keys will hold the top dollar limit for some tax range, and the values will hold the tax rate for that tax range. You need to build a calculator that will calculate the tax for all income up to each key value (if it goes up that high) for the given tax rate.  

For example, let's say my tax dictionary is `{50000: 0.08, 100000: 0.10, 150000: 0.15}`. This means that the first 50k of income is taxed at 8%, the second 50k at 10%, and the rest at 15%. So, if the inputted income was 70k, then my taxes would be 50 * 0.08 + 20 * 0.10 = 6k. You should write your function to be generalized and accept any kind of tax dictionary and any inputted income. 
