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
                line = file_line
    if not line:
        copies_of_line = 'There weren't {} lines in the document'.format(line_num)
    else:
        copies_of_line = [line for _ in range(num_copies)]
    return copies_of_line
 ```
