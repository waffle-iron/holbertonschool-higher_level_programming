# 0x09. Python - Everything is object

Now that we understand that everything is object and have a little bit of knowledge, let's make a pause, and look a little bit closer at how Python works with different types of objects. BTW, have you ever modified a variable without knowing/wanting it? I mean:

```py
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>>
```

OK. But what about this?

```py
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>>
```

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/252/giphy-5.gif "Blow")

This project is a little bit different than usual projects. The first part is only questions about Python's specificity like "What should be the result of...". You should read all documentation first \(as usual :\)\), then take the time to think and brainstorm with your peers about what you think and why. Try to do this without coding anything for a few hours. Trying examples in the Python interpreter will give you most of the answers without having to think about it. Don't go this route. First read, then think, then brainstorm together. Only then you can test in the interpreter. It's important that you truly understand the reasons behind the answers of all those tasks so that you can apply the same logic to other variables and other variable types. The biggest mandatory task is the blog post and it will count for 50% of the total score of the project.

## RTFM

### [9.10. Objects and values](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#objects-and-values)

If we execute these assignment statements,

```py
a = "banana"
b = "banana"
```

we know that a and b will refer to a string with the letters"banana". But we don’t know yet whether they point to the \_same \_string.

There are two possible states:

![](http://www.openbookproject.net/thinkcs/python/english2e/_images/mult_references1.png "Two state diagrams for multiple references with strings")

In one case, a and b refer to two different things that have the same value. In the second case, they refer to the same thing. These things have names — they are called **objects**. An object is something a variable can refer to.

We can test whether two names have the same value using==:

```py
>>> a == b
True
```

We can test whether two names refer to the same object using the\_is\_operator:

```py
>>> a is b
True
```

This tells us that both a and b refer to the same object, and that it is the second of the two state diagrams that describes the relationship.

Since strings are_immutable_, Python optimizes resources by making two names that refer to the same string value refer to the same object.

This is not the case with lists:

```py
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a == b
True
>>> a is b
False
```

The state diagram here looks like this:

![](http://www.openbookproject.net/thinkcs/python/english2e/_images/mult_references2.png "State diagram for equal different lists")

a and b have the same value but do not refer to the same object.

### [9.11. Aliasing](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#aliasing)

Since variables refer to objects, if we assign one variable to another, both variables refer to the same object:

```Python
>>> a = [1, 2, 3]
>>> b = a
>>> a is b
True
```

In this case, the state diagram looks like this:

![](http://www.openbookproject.net/thinkcs/python/english2e/_images/mult_references3.png "State diagram for multiple references \(aliases\) to a list")

Because the same list has two different names, `a` and `b`, we say that it is **aliased**. Changes made with one alias affect the other:

```Python
>>> b[0] = 5
>>> print a
[5, 2, 3]
```

Although this behavior can be useful, it is sometimes unexpected or undesirable. In general, it is safer to avoid aliasing when you are working with mutable objects. Of course, for immutable objects, there’s no problem. That’s why Python is free to alias strings when it sees an opportunity to economize.

### [Immutable vs mutable types](http://stackoverflow.com/questions/8056130/immutable-vs-mutable-types)

What? Floats are immutable? But can't I do

```Python
x = 5.0
x += 7.0
print x # 12.0
```

Doesn't that "mut" x?

Well you agree strings are immutable right? But you can do the same thing.

```Python
s = 'foo'
s += 'bar'
print s # foobar
```

The value of the variable changes, but it changes by changing what the variable refers to. A mutable type can change that way, and it can\_also\_change "in place".

Here is the difference.

```
x = something # immutable type
print x
func(x)
print x # prints the same thing

x = something # mutable type
print x
func(x)
print x # might print something different

x = something # immutable type
y = x
print x
# some statement that operates on y
print x # prints the same thing

x = something # mutable type
y = x
print x
# some statement that operates on y
print x # might print something different
```

Concrete examples

```
x = 'foo'
y = x
print x # foo
y += 'bar'
print x # foo

x = [1, 2, 3]
y = x
print x # [1, 2, 3]
y += [3, 2, 1]
print x # [1, 2, 3, 3, 2, 1]

def func(val):
    val += 'bar'

x = 'foo'
print x # foo
func(x)
print x # foo

def func(val):
    val += [3, 2, 1]

x = [1, 2, 3]
print x # [1, 2, 3]
func(x)
print x # [1, 2, 3, 3, 2, 1]
```

### [Mutation](http://www-inst.eecs.berkeley.edu/~selfpace/cs9honline/Q2/mutation.html)

In Python, all variables \_refer \_to things. When you write `x = 3`, you are making `x` refer to `3`. You could depict this by drawing an arrow from the name `x` to the value `3`, like this:

![](http://www-inst.eecs.berkeley.edu/~selfpace/cs9honline/Q2/x-arrow-3.png)

Figure 1.

After `x = 3`, the name `x` refers to the value `3`.

Every time you use a variable name, you're telling Python to follow that arrow. For example, to evaluate the expression`x + 2`, Python follows the arrow from the`x`to the`3`, then adds 3 to 2. Simple enough, right?

When you assign the value of one variable to another variable, they both refer to the same thing. Suppose`a`refers to the list`[3, 4, 5]`, and then you say`b = a`:

![](http://www-inst.eecs.berkeley.edu/~selfpace/cs9honline/Q2/assign-a-b.png)

Figure 2.

After `b = a`, the name `b` refers to the same list as `a` does.

There's still_only one list_; it's just referred to by two different names.

Why does this matter? Well, look at what happens if you now say`a.append(1)`. An extra element is added to the end of the list.

![](http://www-inst.eecs.berkeley.edu/~selfpace/cs9honline/Q2/a-append-1.png)

Figure 3.

The contents of the list are changed. Both`a`and`b`still refer to the same list, which is now`[3, 4, 5, 1]`.

### [9.12. Cloning lists](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#cloning-lists)

If we want to modify a list and also keep a copy of the original, we need to be able to make a copy of the list itself, not just the reference. This process is sometimes called **cloning**, to avoid the ambiguity of the word copy.

The easiest way to clone a list is to use the slice operator:

```py
>>> a = [1,2,3]
>>> b = a[:]
>>> print b
[1, 2, 3]
```

Taking any slice of `a` creates a new list. In this case the slice happens to consist of the whole list.

Now we are free to make changes to `b` without worrying about `a`:

```py
>>> b[0] = 5
>>> print a
[1, 2, 3]
```

### [Python tuples: immutable but potentially changing](http://radar.oreilly.com/2014/10/python-tuples-immutable-but-potentially-changing.html)

Python tuples have a surprising trait: they are immutable, but their values may change. This may happen when a `tuple` holds a reference to any mutable object, such as a `list`. If you need to explain this to a colleague who is new to Python, a good first step is to debunk the common notion that variables are like boxes where you store data.

In 1997 I took a summer course about Java at MIT. The professor, Lynn Andrea Stein — an award-winning computer science educator — made the point that the usual “variables as boxes” metaphor actually hinders the understanding of reference variables in OO languages. Python variables are like reference variables in Java, so it’s better to think of them as labels attached to objects.

Here is an example inspired by Lewis Carroll’s_Through the Looking-Glass, and What Alice Found There_.

![](http://s.radar.oreilly.com/wp-files/2/2014/10/Tweedledum-Tweedledee_500x390.png "Tweedledum-Tweedledee\_500x390")

Tweedledum and Tweedledee are twins. From the book: “Alice knew which was which in a moment, because one of them had ‘DUM’ embroidered on his collar, and the other ‘DEE’.”

![](http://s.radar.oreilly.com/wp-files/2/2014/10/dum-dee.png "dum-dee")

We’ll represent them as tuples with the date of birth and a list of their skills:

```python
>>> dum = ('1861-10-23', ['poetry', 'pretend-fight'])
>>> dee = ('1861-10-23', ['poetry', 'pretend-fight'])
>>> dum == dee
True
>>> dum is dee
False
>>> id(dum), id(dee)
(4313018120, 4312991048)
```

It’s clear that `dum` and `dee` refer to objects that are equal, but not to the same object. They have distinct identities.

Now, after the events witnessed by Alice, Tweedledum decided to become a rapper, adopting the stage name T-Doom. This is how we can express this in Python:

```python
>>> t_doom = dum
>>> t_doom
('1861-10-23', ['poetry', 'pretend-fight'])
>>> t_doom == dum
True
>>> t_doom is dum
True
```

So,t\_doomanddumare equal — but Alice might complain that it’s foolish to say that, becauset\_doomanddumrefer to the same person:t\_doom is dum.

![](http://s.radar.oreilly.com/wp-files/2/2014/10/dum-t_doom-dee.png "dum-t\_doom-dee")

The namest\_doomanddumare aliases. I like that the official Python docs often refer to variables as “names”. Variables are names we give to objects. Alternate names are aliases. That helps freeing our mind from the idea that variables are like boxes. Anyone who thinks of variables as boxes can’t make sense of what comes next.

After much practice, T-Doom is now a skilled rapper. In code, this is what happened:



| 123456 | &gt;&gt;&gt;skills=t\_doom\[1\]&gt;&gt;&gt;skills.append\('rap'\)&gt;&gt;&gt;t\_doom\('1861-10-23',\['poetry','pretend-fight','rap'\]\)&gt;&gt;&gt;dum\('1861-10-23',\['poetry','pretend-fight','rap'\]\) |
| :--- | :--- |




T-Doom acquired the'rap'skill, and so did Tweedledum — of course, they are one and the same. Ift\_doomwas a box containing astrand alist, how could you explain that appending to the list int\_doomalso changes the list in thedumbox? However, it makes perfect sense if you see variables as labels.

The label analogy is much better because aliasing is explained simply as an object with two or more labels. In the example,t\_doom\[1\]andskillsare two names given to the same list object, just asdumandt\_doomare two names given to the same tuple object.

Below is an alternative depiction of the objects that represent Tweedledum. This figure emphasizes that a tuple holds references to objects.

![](http://s.radar.oreilly.com/wp-files/2/2014/10/dum-skills-references.png "dum-skills-references")

What is immutable is the physical content of a tuple, consisting of the object references only. The value of the list referenced bydum\[1\]changed, but the referenced object id is still the same. A tuple has no way of preventing changes to the values of its items, which are independent objects and may be reached through references outside of the tuple, like theskillsname we used earlier. Lists and other mutable objects inside tuples may change, but their ids will always be the same.

This highlights the difference between the concepts of identity and value, described in_Python Language Reference_[Data model](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types)chapter:

> Every object has an identity, a type and a value. An object’s identity never changes once it has been created; you may think of it as the object’s address in memory. The ‘is’ operator compares the identity of two objects; the id\(\) function returns an integer representing its identity.

After dum became a rapper, the twin brothers are no longer equal:

```python
>>> dum == dee
False
```

We have two tuples that were created equal, but now they are different.

The other built-in immutable collection type in Python,frozenset, does not suffer from the problem of being immutable yet potentially changing in value. That’s because afrozenset\(or a plainset, for that matter\) may only hold references to hashable objects, and the value of hashable objects may naver change, by definition.

Tuples are commonly used asdictkeys, and those must be hashable — just as set elements. So, are tuples hashable or not? The right answer is:**some**tuples are hashable. The value of a tuple holding a mutable object may change, and such a tuple is not hashable. To be used as adictkey or set element, the tuple must be made only of hashable objects. Our tuples nameddumanddeeare unhashable because each contains a list reference, and lists are unhashable.

Now let’s focus on the assignment statements at the heart of this whole exercise.

Assignment in Python never copies values. It only copies references. So when I wroteskills = t\_doom\[1\]I did not copy the list att\_doom\[1\], I only copied a reference to it, which I then used to change the list by doingskills.append\('rap'\).

Back at MIT, Prof. Stein spoke about assignment in a very deliberate way. For example, when talking about a seesaw object in a simulation, she would say: “Variablesis assigned to the seesaw”, but never “The seesaw is assigned to variables“. With reference variables it makes much more sense to say that the variable is assigned to an object, and not the other way around. After all, the object is created before the assignment.

In an assignment such asy = x \* 10, the right-hand side is evaluated first. This creates a new object or retrieves an existing one. Only after the object is constructed or retrieved, the name is assigned to it.

Here is proof in code. First we create aGizmoclass, and an instance of it:

```python
>>> class Gizmo:
...     def __init__(self):
...         print('Gizmo id: %d' % id(self))
...
>>> x = Gizmo()
Gizmo id: 4328764080
```

Note that the\_\_init\_\_method displays the id of the object just created. This will be important in the next demonstration.

Now let’s instantiate anotherGizmoand immediately try to perform an operation with it before binding a name to the result:

```python

>>> y = Gizmo() * 10
Gizmo id: 4328764360
Traceback (most recent call last):
  ...
TypeError: unsupported operand type(s) for *: 'Gizmo' and 'int'
>>> 'y' in globals()
False
```



This snippet shows that the new object was instantiated \(its id was4328764360\) but before theyname could be created, aTypeErroraborted the assignment. The'y' in globals\(\)check proves there is noyglobal name.

To wrap up: always read the right-hand side of an assignment first. That’s where the object is created or retrieved. After that, the name on the left is bound to the object, like a label stuck to it. Just forget about the boxes.

As for tuples, make sure they only hold references to immutable objects before trying to use them as dictionary keys or put them in sets.

