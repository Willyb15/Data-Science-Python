## Reverse Polish Notation Calculator

Your assignment today is to implement a program that functions as a calculator; but not just any calculator, a reverse polish notation calculator. There's a good chance you've never heard of this particular flavor of calculator so here's a quick overview.

### Reverse Polish Notation

Many of us are solely used to entering computations into a calculator by putting an operation between two values. E.g.

|:-----:|:---------:|:-----:|
|   3   |     +     |   4   |
| value | operation | value |

However there are other notations that can be used to express mathematical operations, prefix, also known as Polish, notation and postfix, also know as Reverse Polish, notation. Today we will be implementing a calculator that implements Reverse Polish Notation ([RPN](https://en.wikipedia.org/wiki/Reverse_Polish_notation)). E.g.

|:-----:|:-----:|:---------:|
|   3   |   4   |     +     |
| value | value | operation |

This method of inputting computations actually makes it easier to write logic, for the computer, to perform the operations. This is because the format lends itself to storing computations in a [stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)). A stack is a specific type of queue (know as last in, first out, LIFO)  which only supports two types of operations, pushing and popping.

You can think of a stack as a list with less functionality. (**Note**: the [deque](https://docs.python.org/2/library/collections.html#collections.deque) class is the closest native Python class to a stack. When you go to implement you're version of a RPN calculator today you can choose to use this class instead of a list as it will technically give you speed gains on the pushing and popping operations you will need to perform over the same functionality being implemented with a list.) What a RPN calculator does is accept input one element at a time, these elements can either be values or operations, and pushes them, in turn, onto the stack; in Python list lingo, appends them to a list. When the user wants to perform an operation the correct number values necessary to perform the operation are [popped](https://docs.python.org/2/tutorial/datastructures.html) off the stack, in turn. The value resulting from that operation is then pushed back onto the stack. If it is the last value on the stack then that value is returned, else the process starts over again.

### RPN Example

Say we want to calculate, in infix notation, the value resulting from the calculation: `6 + ((5 + 3) / 4) - 3`. In RPN that calculation is written: `6 5 3 + 4 / + 3 −`. To input this calculation into a RPN calculator one would enter those elements, in turn, and the corresponding operations would occur in the following order.

| Input |  Operation   |    Stack    |                   Other                   |
|:-----:|:------------:|:-----------:|:-----------------------------------------:|
|   6   |  Push Value  | [ 6 ]       |                                           |
|   5   |  Push Value  | [ 6, 5 ]    |                                           |
|   3   |  Push Value  | [ 6, 5, 3 ] |                                           |
|   +   |     Add      | [ 6, 8 ]    | Pop two values (3 then 5), push result, 8 |
|   4   |  Push Value  | [ 6, 8, 4 ] |                                           |
|   /   |    Divide    | [ 6, 2 ]    | Pop two values (8 then 4), push result, 2 |
|   +   |     Add      | [ 8 ]       | Pop two values (2 then 6), push result, 8 |
|   3   |  Push Value  | [ 8, 3 ]    |                                           |
|   -   |   Subtract   | [ 5 ]       | Pop two values (3 then 8), push result  5 |
|       |    Return    |   5         |                                           |

If you want to play around with a RPN calculator to get a feel for them and how they operate check out [this](http://www.meta-calculator.com/learning-lab/reverse-polish-notation-calculator.php) link.
