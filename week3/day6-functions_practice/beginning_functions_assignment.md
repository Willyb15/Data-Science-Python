# Instructions

Tonight you are going to get some practice writing functions that work together. Much of what we do is programming requires us to break down problems into smaller pieces. So tonight's assignment is aimed at getting you practice doing just that; working on breaking problems down to solve them with functions.

To start off you will be given already completed functions and be asked to break them into smaller ones. The next part of the assignment will outline problems, and describe the functions for you to write to solve them. This outline of breaking down the problem into smaller problems will get you used to thinking about the top-down process. Finally, you will get a set of problems to solve with a top-down approach on your own. Let's get started!

# Assignment

### Part 1 - Breaking Code Apart

For this section you will be given a functions that have a decent amount of code in them. You task is to break them apart into more than one function. The first will have the same definition as the one given to you, but now it will call another function that you are going to write. For example, say I have the function below:

```python
def my_function(n):
    if n > 10:
        for _ in range(n - 9):
            print('I love Python!!!')
    else:
        for _ in range(n):
            print('I love Python so much!!!')
```

One way that you could break up this function up is to have a separate function that performs a loop over the print statements. This function could then accept a range and a string to print. Check it out.

```python
def print_n_string(print_times, print_string):
    for _ in range(print_times):
        print(print_string)

def my_function(n):
    if n > 10:
        print_times = n - 9
        print_n_string(n - 9, 'I love Python!!!')
    else:
        print_times = n
        print_n_string(n, 'I love Python so much!!!')
```

Notice how the this new implementation of `my_function()` only has a single `for` loop written. This is great since we want to employ DRY programming as much as possible. Also, we can easily see what we are changing in each case in `if`-block. This makes the code a little more readable.

You're going to do this for all of the functions given to you in this section. One thing to keep in mind is that it's usually very useful to understand what the code is doing before you break it apart. So, make sure to read the code, or even better come up with a test for it and go through, line by line what each function is doing before you break it apart.

1. Break apart the function:
  
 ```python
 def update_library(books, library):
     '''
     Input:  List - book names, Set - books already in library
     Output: List - books that weren't in the library
     '''
     new_books = []
     for book in books:
         if book in library:
             print('The book, {} is new!'.format(book))
             new_books.append(book)
         library.add(book)
     print library    
     return new_books
 ```
 
2. Break apart the function:
 
 ```python
 def play_rock_paper_scissors(n_rounds):
     '''
     Input:  Int - number of rounds to play rock paper scissors for
     '''
     for _ in range(n_rounds):
         player_1 = raw_input('Player 1 play (r/p/s): ')
         player_2 = raw_input('Player 2 play (r/p/s): ')
         if player_1 == player_2:
             print("It's a tie!")
         elif player_1 == 'r' and player_2 == 's':
             print('Player 1 wins!')
         elif player_1 == 'r' and player_2 == 'p':
             print('Player 2 wins!')
         elif player_1 == 'p' and player_2 == 'r':
             print('Player 1 wins!')
         elif player_1 == 'p' and player_2 == 's':
             print('Player 2 wins!')
         elif player_1 == 's' and player_2 == 'r':
             print('Player 2 wins!')
         elif player_1 == 's' and player_2 == 'p':
             print('Player 1 wins!')
         else:
             print('Someone didn't play right!')
 ```
 
3. Break apart the function:

 ```python
 def repeat_list_of_file_line(file_name, line_num, num_copies):
     '''
     Input:  Str - path to file, 
             Int - number of line to copy from file, 
             Int - number of times to copy line into list
     Output: List - filled with num_copies of line_num in file_name
     '''
     line = None
     with open(file_name) as f:
         for i, file_line in enumerate(f, 1):
             if i == line_num:
                 line = file_line.strip()
     if not line:
         copies_of_line = 'There were not {} lines in the document'.format(line_num)
     else:
         copies_of_line = [line for _ in range(num_copies)]
     return copies_of_line
 ```
4. Break apart the function:

 ```python
 import this
 
 def decode_zen_of_python():
     zen_decoder = this.d
     coded_zen = this.s
     print coded_zen
     decoded_chars = []
     for char in coded_zen:
         if char.isalpha():
             decoded_chars.append(zen_decoder[char])
         else:
             decoded_chars.append(char)
     decoded_text = ''.join(decoded_chars)
     print '\n' + decoded_text
 ```

### Part 2 - Beginning to Write Top-Down

1. Fill in the following stub code so that the functions operate in the way prescribed by their doc strings.
 
 ```python
 def get_month_season(month):
     '''
     Input:  Str - Abbreviation of month
     Output: Str - Season of inputted month
     '''
     pass
 
 def month_info(month, category):
     '''
     Input:  Str - Abbreviation of month, Str - information category to get for month
     Output: Str - category information for the specified month
 
     Categories supported: 'full name'   ex: month_info('jan', 'full_name') -----> 'January'
                           'num_month'   ex: month_info('may', 'num_month') ----->  5
                           'birth_stone' ex: month_info('jul', 'birth_stone') ---> 'Ruby' 
                           'season'      ex: month_info('oct', 'season') --------> 'Fall'
     '''
     full_names = {'jan': 'January', 'feb': 'February', 'mar': 'March', 'apr': 'April',
                   'may': 'May', 'jun': 'June', 'jul': 'July', 'aug': 'August',
                   'sep': 'September', 'oct': 'October', 'nov': 'November', 'dec': 'December'}

     month_nums = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6, 
                   'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}

     birth_stones = {'jan': 'Garnet', 'feb': 'Amethyst', 'mar': 'Aquamarine', 'apr': 'Diamond',
                     'may': 'Emerald', 'jun': 'Pearl', 'jul': 'Ruby', 'aug': 'Peridot',
                     'sep': 'Sapphire', 'oct': 'Opal', 'nov': 'Topaz', 'dec': 'Turquoise'}
 
     # Depending on the category get information about month from correct source and return 
 ```

2. Fill in the following stub code so that the functions operate in the way prescribed by their doc strings.

 ```python
 def perfect_square(num):
     '''
     Input:  Int
     Output: Bool
 
     Return True if num is a perfect square, e.g. 9 = 3 x 3. Return False if num is not
     a perfect square, 8 isn't any integer multiplied by itself.
     '''
 def next_perfect_square(num):
     '''
     Input:  Int
     Output: Int
 
     Returns the next perfect square, a number that is the sqaure of an integer (e.g. 81 = 9 x 9)
     greater than the inputted number. If the inputted number is not a perfect square, return -1.
     A.k.a. the inputted number must also be a perfect square.
     '''
 ```

3. Fill in the following stub code so that the functions operate in the way prescribed by their doc strings.

 ```python
 import random
 
 def flip_coin():
     '''
     Input:  None
     Output: Str - 'H' for head or 'T' for tail
 
     Perform an "experiment" using random.random(), return 'H' if result is above .5, 'T' otherwise.
     '''
     pass
 
 def roll_die():
     '''
     Input:  None
     Output: Int - Between 1 and 6
 
     Using random.randint() perform a die roll and return the number that "comes up".
     '''
     pass
 
 def flip_coin_roll_die(n_times):
     '''
     Input:  Int - number of times to flip a coin and roll a die
     Output: List - of tuples, length n_times, with the outcomes 
                    of flips and rolls from each time
     '''
     pass
 ```

### Part 3 - Tying it All Together

For this part of the assignment you are going to be coding up your own functions, no training wheels! Most of the time, when programming, all we have is a problem; and it will be your job to create functions to solve these problems. This may sound daunting, but don't worry, you've been practicing a lot in the previous sections getting your mind used to thinking about splitting up problems into smaller parts. Now you're going to do it all on your own.

1. Write a function that rolls two sets of dice to model players playing a game with dice. It will accept two arguments, the number of dice to roll for the first player, and the number of dice to roll for the second player. The function will model rolling the appropriate number of dice for each player and sum the total values of the corresponding dice rolls. The function will then print which player rolled the higher total. Finally it will return the total sum of each players rolls in a tuple. Here's how we would call it:

 ```python
 In [1]: player_rolls = model_dice_rolls(3, 2)
 Player 1 wins!
 In [2]: player_rolls
 Out[2]: (13, 7)
 ```

 Remember, you already have some code that does solves part of this problem. Feel free to use whatever code you have written previously, that's part of the reason we use functions. Hopefully you're beginning to see the advantages of using functions!

2. Things and Stuff 
