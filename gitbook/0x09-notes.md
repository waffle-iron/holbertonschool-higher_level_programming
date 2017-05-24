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

In Python, all variables _refer _to things. When you write `x = 3`, you are making `x` refer to `3`. You could depict this by drawing an arrow from the name `x` to the value `3`, like this:

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

If we want to modify a list and also keep a copy of the original, we need to be able to make a copy of the list itself, not just the reference. This process is sometimes called**cloning**, to avoid the ambiguity of the word copy.

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



