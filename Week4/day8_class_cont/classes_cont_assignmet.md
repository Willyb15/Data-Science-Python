# Instructions

Did you ever have the thought during our discussion of classes that the tic-tac-toe game we created would be better in a class (or a couple of classes)? Well, if you did, you're in luck! Tonight's assignment is going to be to move that game in to a class, or rather, a couple of classes. We'll give you some ideas for classes you should construct, and what attributes and methods these should have, and let you dive in. 

As a final note, it might be worth it to read over the entire assignment to get an idea of everything that you are tasked with doing, and then take a little bit of time to plan out how you are going to approach this task. While code can always be refactored, an extra 10-15 minutes of planning upfront is usually worth it.

## The `Board` Class

The first class that I would build would be the `Board` class, as this is the centerpiece of the game. I would imagine that it has two attributes - the `board_size` and the actual `board` itself. In terms of methods, the `Board` is probably going to need methods to handle some of the logic that occurs during the game - checking if certain coordinates on the board are taken and/or valid given it's size, actually filling a spot on the board when a player inputs valid coordinates, and then determining whether or not anybody has won. Also, it'd be nice if the `Board` has a method that displays what it looks like.    

Some notes: 

* While you can imagine that you could simply get the `board_size` by taking the `len()` of the board, it might make sense to store the `board_size` as an attribute, since you will want to know it pretty frequently (this way we avoid having to call `len()` over and over again when we want to get the size of the board). 
* In terms of breaking up some of the logic when a player inputs coordinates, I imagine this to happen in two steps: (1) Checking to see if the inputs are valid, regardless of the board - this check looks at whether or not **two numbers** were inputted, and (2) Checking to see if the inputs are valid, **given** the board - this check looks at what spots are currently taken on the board, and if the inputted coordinates are valid given the board size. In an OOP framework, we like to try to think about the logical location of checks like these. Since `(1)` doesn't involve the board, I would think that it shouldn't be done in the `Board` class. `(2)` does involve the `Board` class, though, and so I can imagine that it should be done in the `Board` class.  

