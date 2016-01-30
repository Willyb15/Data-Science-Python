## More On Python Classes

### Intro

Last class we learned about the programming paradigm known as OOP and we got some practice writing simple classes in Python. Today we are going to build on that knowledge and discuss a number of important things regarding classes and their use:

    * Python classes magic methods.
    * How everything in Python is actually an object (instantiated class)!
    * How to analyze when to use classes.

### Magic Methods

There are a number of things that we have been taking for granted in our use of Python so far. Let's dive into an example of where we were using some functionality built into Python but didn't think too much about how it was working.

```python
In [1]: my_list = [1, 2, 3]

In [2]: my_dict = {1: 'first', 2: 'second'}

In [3]: len(my_list)
Out[3]: 3

In [4]: len(my_dict)
Out[4]: 2
```

Here we are using the `len()` function, a Python built-in and passing it both a list and a dictionary. This might seem fairly natural now, if you take a moment to think about how this works you may run into some logical stops. One thing that my come to mind is, considering our knowledge of how functions work, how are we passing two different data structures to `len()` and Python is still able to know what we're asking, number one, and number two, reason about how "long" these decidedly different data structures are?

What's really happening under the hood when we pass a data structure to the `len()` function is that Python is going to that object and running its `__len__()` method. Ok, that sounds cool, but what does it all mean? This is an example of a **magic method** and we will dive into them shortly. For now, know that magic methods allow us, as creators of custom classes, to give them more robust functionality in terms of interacting with Python. So, just as the `__len__()` method was called when both a list and a dictionary was passed to the `len()` function, we can define a `__len__()` method on our custom classes so that Python knows what to do when you pass an instance of that class to the `len()` method; in addition, how Python gets a "length" from your class is entirely up to you!

#### Polymorphism Detour

The above example is a great example of polymorphism, that idea we quickly discussed last class. Let's take a moment to get a better handle on this idea. Polymorphism is defined as the provision of the same interface for entities of different types.

We see that idea in direct action in the above example. Though we were passing different types of entities to the `len()` function, because it implements the `__len__()` method on whatever object was passed to it, and any object can implement that method, we this notion of the same interface. And, even further, we see the benefits of setting up a paradigm with this design principle implemented. To make something work with `len()` all you have to do is make sure it defines the `__len()__` method. And, tada! The general structure of the interface, polymorphism in action, takes care of the rest.

Speaking of which. How do we define these "magic" methods?? End detour.

#### Defining a Magic Method

Defining a magic method is as easy as defining any other method in a class. We actually did it last time with the `__init__()` method, so all you have to do is start with a def and then the name of the magic with the double underscores. **Note**: All methods with names beginning and ending with double underscores are magic methods, this naming convention is reserved for them.

Let's take a look at this with the `OurClass` class we created last time. I'm going to add a `__len__()` implementation to the code from last lecture. Considering that the, logically, the `len()` function should return a number of something it seems reasonable to have it return the number of questions asked we have stored. Instead of putting our code directly into IPython, this time we're going to store it in a script, `lecture.py`, and get some practice importing. Let's take a look.

```python
class OurClass(): 
    
    def __init__(self, name, location, size=0): 
        self.name = name
        self.location = location
        self.size = size
        self.questions_asked = []
        if self.size >= 20: 
            self.at_capacity = True
        else: 
            self.at_capacity = False

    def __len__(self):
        return len(self.questions_asked)

    def add_question_asked(self, question): 
        self.questions_asked.append(question)
    
    def add_class_members(self, num): 
        self.size += num

        if self.size >= 20: 
            print 'Capacity Reached!!'
            self.at_capacity = True

    def check_if_at_capacity(self): 
        return self.at_capacity
```

Now we can have `len()` interact with instances of `OurClass`.

```python
In [1]: from lecture import OurClass

In [2]: our_class = OurClass('Intro Python', 'Platte', 15)

In [3]: len(our_class)
Out[3]: 0

In [4]: our_class.add_question_asked("What's he going to show?")

In [5]: our_class.add_question_asked('Do you know the answer?')

In [6]: len(our_class)
Out[6]: 2
```

Just as we'd expect if we want to get the number of questions when calling `len()`. For reference, check out what would happen if we hadn't defined an implementation for `__len__()`.

```python
In [1]: from lecture import OurClass

In [2]: our_class = OurClass('Intro Python', 'Platte', 15)

In [3]: len(our_class)
___________________________________________________________________________
TypeError                                 Traceback (most recent call last)
<ipython-input-3-ae0663a04767> in <module>()
    > 1 len(our_class)

TypeError: object of type 'OurClass' has no len()
```

An error! At least Python lets us know that it's related to having no length, a problem that we now know how to fix!

### Using Classes Pragmatically

One question that comes up frequently in languages like Python that don't fall into a single [paradigm](https://en.wikipedia.org/wiki/Programming_paradigm) is learning when to use the different features of the language. As applied to our current circumstance, when should we be making classes instead of just using functions?

Part of the confusion in answering this question frequently stems from an incomplete understanding OOP's purpose in life, to take advantage of the ideas of inheritance, encapsulation and polymorphism.With this in mind let's discuss classes at a high level and see what kinds of problem attributes lend themselves to being solved with functions, procedurally, vs with OOP.

Similarly to one of the motivations for functions, abstraction, we see the idea of encapsulation espoused by OOP. Encapsulation is very much like abstraction in that it hides implementation details; however, with it we see the distinction that many functions, abstractions, can be bundled up together in a class. In addition we also see anther aspect of abstraction introduced, abstraction of the data itself. While we can instantiate a class with whatever properties we dictate, often these will specify the nature of the data (though sometimes it wont), we have the bundled methods that act on the data which are designed to keep us from caring about the exact state of that data. Sometimes this can be good and sometimes not so much.

Consider an example. You have a dictionary with keys as country names and values as list of all historical presidents for that country. You want to have the ability to see what presidents names start with a given letter. You could easily write a function for this. Maybe it looks like:

```python
def presidents_by_letter(country_pres_dict, letter):
    letter_pres = []
    for pres_list in country_pres_dict.values():
        for pres in pres_list:
            if pres[0].lower() == letter:
                letter_pres.append(pres)
    return letter_pres 
```

This seems really reasonable. But we could also make a class for this task. It would contain the dictionary of countries and presidents. And have a method that does the same thing as `presidents_by_letter()` above. Maybe it looks like:

```python
class CountiesPresidents():
    def __init__(self, country_pres_dict):
        self.country_pres_dict = country_pres_dict

    def presidents_by_letter(self, letter):
        letter_pres = []
        for pres_list in self.country_pres_dict.values():
            for pres in pres_list:
                if pres[0].lower() == letter:
                    letter_pres.append(pres)
        return letter_pres 
```

So. Which is better, the function or the class??

#### Function or Class?

In the case outlined above there is a pretty strong case for not going with the more heavy-weight option of a class and stick with a simple function. Is there a rule then, that governs when you should use one over the other? Kinda and no...but we do have a good solution to the problem. So let's discuss that.

Generally with think of use cases for classes as ones that align with the principles of OOP, the inheritance, encapsulation and polymorphism. If we think that we are in a situation where encapsulation, having multiple layers of abstraction that between the user and their data, all of which make sense to bundle together, then using classes makes sense.

Yes. This all seems a little hand wavy, but the method of reasoning is quite sound. In addition we have access to another amazing tool to make our decision process easier, **refactoring**. Refactoring is the process of restructuring your code without changing it's behavior. When we took advantage of function abstraction in the other lecture and changed the internals of `update_counts()` we were actually refactoring.

Refactoring can also be a more overhauling process, wherein you change the entire structure of your programs. To illustrate this lets look at a problem that extends the one we solved when learning how to make functions work together, the `create_report()` project. Along the way we will discuss why the problem would be solved with functions and then talk about when an extension/refactor to a class would be appropriate.

### Python's Multi-paradigmatic Toolbox For the Win

Let's start this gedanken with a refresher of the `create_report()` project. We had our "boss" come to us and ask for a program that takes the path for a text file and tells you the number of sentences, words, and characters in that file. Below is the code we came up with for this project.

```python
def update_counts(line, counts_dict):
    for char in line:
        counts_dict['characters'] += 1
        if char == '.':
            counts_dict['sentences'] += 1
        elif char == ' ':
            counts_dict['words'] += 1
    counts_dict['words'] += 1


def create_report(file_path):
    counts_dict = {'sentences': 0, 'words': 0, 'characters': 0}
    with open(file_path) as txt_file:
        for line in txt_file:
            update_counts(line, counts_dict)
    return counts_dict
```

We went through a couple of iterations improving on this code to get it where it is and our boss seemed pleased with the result. Now he's back, though. He wants more functionality built into our solution. This time he asks us to expand our program so that we can easily create reports as it did before, but also keep an aggregated count of all the reports produced, abililty to produce a summary of those counts (mean, median, mode) and a library of words from all the documents.

Alright! Well, that's certainly a bit more functionality. How are we going to solve this? Simple answer, one step at a time. Ok that's wasn't particularly specific...what's the first step then?? As before we are going to embrace an iterative approach to developing functionality. As it's frequently hard to see the forest through the trees, one of the best starting places is identifying a tree and working on that one, slowly building the forest up. First task then, we want to be able to produce a bunch of reports so lets create a function for that.

If we want to the same thing repeatedly while programming, what tool do we use? A loop! Ok, that's awesome, we already have an idea how we're going to approach this problem, so what are we going to loop over? An obvious answer is a list of file paths. Let's take a look at some psuedo code that will achieve this.

```python
def create_reports(file_paths):
    for file_path in file_paths:
        create_report(file_path)
```

This skeleton makes some sense, for each file path we want to create a report. However, the current way that we have `create_report()` set up returns a dictionary of counts. What are we going to do with these? How are we going to collect all the counts together so that we can create summary statistics? Further, how are we going to create a library of words contained in all the documents??

These are great questions and to answer them we need to think hard about the structure of our program. If we want to aggregate all of the counts together we could have a seperate dictionary devoted to that task. Now the question would be, where should that dictionary be created and where will updates to it be made?

Questions like this one go a long way to directing decisions on how to structure your programs. Things to think about when you're answering these questions are that functions should be resuable, meaning that if it's, for example, creating and returning data structures within it's scope it's potentially less generaly than if it accepts an existing data structure as a parameter. However you need to think about needlessly passing around objects that might just be best stored in a class with the functions being made into methods for that class. This brings up an important point, Python has both functions and classes, so you can choose the one that suits your needs! What's important is that you're aware of both and are concious about thinking over the costs and benefits of each when you're writing your programs.

How do we apply all of this to our current problem? Well, we know that we're going to want to have some sort of object storing all of our counts and our vocabulary, so this is starting to sound like maybe we should create a class. Keep in mind that this decision, to make the jump to class usage, can happen at any time during your process, and you can always go back! (**Note**: frequently you'll want to try out a change, be it large, a huge refactor, or small, a tiny implementation change, but not want to affect all of your current work. This happens so frequently that there is amazing functionality to solve this exact problem built into your version control system, git, called branches. [Here](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) is a great into to branching and, what is known as, merging from the git docs if you want to learn about this amazing feature.)

Let's make the jump to classes then!

#### Functions to Classes

When you're thinking about refactoring your function based code to classes you frequently have an idea what the methods are going to do, you have already written some functions, so need to think about what the class' attributes will look like. For us it's not too bad, we know that we're going to need a dictionary to hold our master counts and a place to store our vocabulary. In this case a set makes the most sense since we don't need repeats of words. If instead we wanted to keep track of all the documents a word was found in we could do that with a dictionary. Let's start setting up the structure our our class now including the `create_reports()` function we started earlier.

```python
class ReportCreator():
    def __init__(self):
        self.vocabulary = set()
        self.master_counts_dict = {'sentences': 0, 'words': 0, 'characters': 0}

    def create_reports(self, file_paths):
        for file_path in file_paths:
            pass
```

Nice and easy. So now we want to transition our functions to methods so that they will be accessible within the class. Remember that we need to pass `self` as the first parameter to methods.

```python
class ReportCreator():
    def __init__(self):
        self.vocabulary = set()
        self.master_counts_dict = {'sentences': 0, 'words': 0, 'characters': 0}

    def create_reports(self, file_paths):
        for file_path in file_paths:
            pass

    def create_report(self, file_path):
        counts_dict = {'sentences': 0, 'words': 0, 'characters': 0}
        with open(file_path) as txt_file:
            for line in txt_file:
                self._update_counts(line, counts_dict)
        return counts_dict

    def _update_counts(self, line, count_dict):
        for char in line:
            counts_dict['characters'] += 1
            if char == '.':
                counts_dict['sentences'] += 1
            elif char == ' ':
                counts_dict['words'] += 1
        counts_dict['words'] += 1
```

Now we've got access to the functionality we had in our old functions within the class. Let's talk about two things quickly. One, you might have noticed that `update_counts()` was changed to `_update_counts()`. The leading underscore is a single to Python users that this particular method is for use internal to the class only, similar to the double underscores we see with the magic methods, it also makes the method hidden when tab completing on instances of this class unless you start with an understore. e.g. In IPython type `<instance of ReportCreator>._<tab>`. It makes sense to make this a hidden method because, realistically, a user of this class will never need to update the counts of a single counts dictionary with a single line. Two, we see that we'll have to change what happens in the `_update_counts()` method so that we can keep track of all the words our class has seen.

This second part forces us to rethink how we will loop over each line. Currently we don't store anything about the characters we're looping over but now we need to store them and add logic to figure out when to add a word to our vocabulary. Check out the implementation below.

```python
class ReportCreator():
    ...

    def _update_counts(self, line, counts_dict):
        word = ''
        for char in line:
            counts_dict['characters'] += 1
            if char in '?.!':
                counts_dict['sentences'] += 1
            elif char == ' ':
                counts_dict['words'] += 1
                self.vocabulary.add(word)
                word = ''
            else:
                word += char.lower()
        counts_dict['words'] += 1
        self.vocabulary.add(word)
```

Notice how this solution isn't robust to random puncutation characters like @ or &, but we can deal with that later if we find, during testing or usage, it necessary. Ahhhh, abstraction. At least we're considering other ways for sentences to end with `if char in '?.!'`. Also, it seems that we are actually repeating the lines `counts_dict['words'] += 1` and `self.vocabulary.add(word)` in one of our conditions and at the end of the function. In the name of the DRY methodology we could consider putting this into a funciton and calling it twice in place of those 4 lines.

Now that we have figured out how `_update_counts()` is going to work we need to decide how to make `create_reports()` is going to interact with `create_report()`. As mentioned earlier, it's best to keep functions/methods specialized, this means that if we wanted to create reports and update our class with a list of file paths the functionality should be the same as if we wanted to create a single report and update the class with a single file path except for a single one. This means that we should be doing updates to `master_counts_dict` from within `create_report()`.

### Everything in Python is an Object!
