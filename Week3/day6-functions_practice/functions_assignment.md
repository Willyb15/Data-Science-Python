# Instructions

Tonight you're going to be writing a program that does something cool! You're going to write a script that allows two people to play tic-tac-toe! This is a much more involved problem than any you've seen in this class so far. In general you should be thinking about how to break up your solution, as you write it, into smaller parts. In addition you should be giving all your functions good names good names as you separate your code out. 

The assignment will give suggestions on how to write this program. But remember, there's always more than one solution to any programming problem. So, if you want to do something that's not suggested by the assignment, by all means, give it a try! If you want to talk with someone about what you're thinking about implementing talk an instructor or one of your peers. Frequently, talking about the problem will help you get a better handle on it, and therefore, how to solve it.

# Assignment Suggestions

### Part 1: Getting Started

One of the first things I always do when writing a script is start a main block. In side of the main block you'll be calling the function that is going to run your game. This puts you in the mindset of programming top down. It also makes it so that it's easy to test your code, since running your script should start the main entry point into your code running.

What are your going to call the function that runs your program? It should be a name that describes what it does. Other than that, you have free reign.

### Part 2: Set Up the Game

A simple way to store a tic-tac-toe board is with a list of three lists, each three elements long. You'll want to initialize the board to something in the beginning. I suggest that you have the coordinates of the squares that players could play in to begin with. This will make it easier for users to specify where they want to play later.

It also makes sense to print this initial board. Since you'll probably want to print the board after any play is made it would make sense to make a function that takes the list of lists, the board, and prints it in a friendly way to the screen. Here's what the solution's board looks like:

```
[(0, 0), (1, 0), (2, 0)]
[(0, 1), (1, 1), (2, 1)]
[(0, 2), (1, 2), (2, 2)]
```
