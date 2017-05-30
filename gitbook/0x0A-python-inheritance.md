# 0x0A. Python - Inheritance

## Readme

* [Inheritance](https://docs.python.org/3.4/tutorial/classes.html#inheritance) & [Multiple inheritance](https://docs.python.org/3.4/tutorial/classes.html#multiple-inheritance)
* [Inheritance in Python](https://www.packtpub.com/books/content/inheritance-python)
* Watch [Learn to Program 10 : Inheritance Magic Methods](https://www.youtube.com/watch?v=d8kCdLCi6Lk)

_Tip from_[_Justin Marsh_](https://twitter.com/dogonthecircuit): Read more books, Chapter 3, p59-66

---

9.5. Inheritance

Of course, a language feature would not be worthy of the name “class” without supporting inheritance. The syntax for a derived class definition looks like this:

```py
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```

The name`BaseClassName`must be defined in a scope containing the derived class definition. In place of a base class name, other arbitrary expressions are also allowed. This can be useful, for example, when the base class is defined in another module:

```py
class DerivedClassName(modname.BaseClassName):
```

Execution of a derived class definition proceeds the same as for a base class. When the class object is constructed, the base class is remembered. This is used for resolving attribute references: if a requested attribute is not found in the class, the search proceeds to look in the base class. This rule is applied recursively if the base class itself is derived from some other class.

There’s nothing special about instantiation of derived classes:`DerivedClassName()`creates a new instance of the class. Method references are resolved as follows: the corresponding class attribute is searched, descending down the chain of base classes if necessary, and the method reference is valid if this yields a function object.

Derived classes may override methods of their base classes. Because methods have no special privileges when calling other methods of the same object, a method of a base class that calls another method defined in the same base class may end up calling a method of a derived class that overrides it. \(For C++ programmers: all methods in Python are effectively`virtual`.\)

An overriding method in a derived class may in fact want to extend rather than simply replace the base class method of the same name. There is a simple way to call the base class method directly: just call`BaseClassName.methodname(self,arguments)`. This is occasionally useful to clients as well. \(Note that this only works if the base class is accessible as`BaseClassName`in the global scope.\)

Python has two built-in functions that work with inheritance:

* Use [`isinstance()`](https://docs.python.org/3.4/library/functions.html#isinstance) to check an instance’s type: `isinstance(obj,` `int)`
  will be `True`only if `obj.__class__`is [`int`](https://docs.python.org/3.4/library/functions.html#int) or some class derived from [`int`](https://docs.python.org/3.4/library/functions.html#int).
* Use [`issubclass()`](https://docs.python.org/3.4/library/functions.html#issubclass) to check class inheritance: `issubclass(bool, int)`is `True`
  since [`bool`](https://docs.python.org/3.4/library/functions.html#bool) is a subclass of [`int`](https://docs.python.org/3.4/library/functions.html#int) . However, `issubclass(float, int)`is `False`
  since [`float`](https://docs.python.org/3.4/library/functions.html#float) is not a subclass of [`int`](https://docs.python.org/3.4/library/functions.html#int).

---

### 9.5.1. Multiple Inheritance

Python supports a form of multiple inheritance as well. A class definition with multiple base classes looks like this:

```Python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

For most purposes, in the simplest cases, you can think of the search for attributes inherited from a parent class as depth-first, left-to-right, not searching twice in the same class where there is an overlap in the hierarchy. Thus, if an attribute is not found in`DerivedClassName`, it is searched for in`Base1`, then \(recursively\) in the base classes of`Base1`, and if it was not found there, it was searched for in`Base2`, and so on.

In fact, it is slightly more complex than that; the method resolution order changes dynamically to support cooperative calls to[`super()`](https://docs.python.org/3.4/library/functions.html#super). This approach is known in some other multiple-inheritance languages as call-next-method and is more powerful than the super call found in single-inheritance languages.

Dynamic ordering is necessary because all cases of multiple inheritance exhibit one or more diamond relationships \(where at least one of the parent classes can be accessed through multiple paths from the bottommost class\). For example, all classes inherit from[`object`](https://docs.python.org/3.4/library/functions.html#object), so any case of multiple inheritance provides more than one path to reach[`object`](https://docs.python.org/3.4/library/functions.html#object). To keep the base classes from being accessed more than once, the dynamic algorithm linearizes the search order in a way that preserves the left-to-right ordering specified in each class, that calls each parent only once, and that is monotonic \(meaning that a class can be subclassed without affecting the precedence order of its parents\). Taken together, these properties make it possible to design reliable and extensible classes with multiple inheritance. For more detail, see[https://www.python.org/download/releases/2.3/mro/](https://www.python.org/download/releases/2.3/mro/).

---

# Basic inheritance

Technically, every class we create uses inheritance. All Python classes are subclasses of the special class named object. This class provides very little in terms of data and behaviors \(those behaviors it does provide are all double-underscore methods intended for internal use only\), but it does allow Python to treat all objects in the same way.

If we don't explicitly inherit from a different class, our classes will automatically inherit from object. However, we can openly state that our class derives from object using the following syntax:

```py
class MySubClass(object):
    pass
```

This is inheritance! Since Python 3 automatically inherits from object if we don't explicitly provide a different superclass. A **superclass**, or parent class, is a class that is being inherited from. A **subclass **is a class that is inheriting from a superclass. In this case, the superclass is object, and MySubClass is the subclass. A subclass is also said to be **derived **from its parent class or that the subclass **extends **the parent.

As you've probably figured out from the example, inheritance requires a minimal amount of extra syntax over a basic class definition. Simply include the name of the parent class inside a pair of parentheses after the class name, but before the colon terminating the class definition. This is all we have to do to tell Python that the new class should be derived from the given superclass.

How do we apply inheritance in practice? The simplest and most obvious use of inheritance is to add functionality to an existing class. Let's start with a simple contact manager that tracks the name and e-mail address of several people. The contact class is responsible for maintaining a list of all contacts in a class variable, and for initializing the name and address, in this simple class:

```python
class Contact:
  all_contacts = []

  def __init__(self, name, email):
    self.name = name
    self.email = email
    Contact.all_contacts.append(self)
```

This example introduces us to class variables. Theall\_contactslist, because it is part of the class definition, is actually shared by all instances of this class. This means that there is only**one**Contact.all\_contactslist, and if we callself.all\_contactson any one object, it will refer to that single list. The code in the initializer ensures that whenever we create a new contact, the list will automatically have the new object added. Be careful with this syntax, for if you ever set the variable usingself.all\_contacts, you will actually be creating a**new**instance variable on the object; the class variable will still be unchanged and accessible asContact.all\_contacts.

This is a very simple class that allows us to track a couple pieces of data about our contacts. But what if some of our contacts are also suppliers that we need to order supplies from? We could add anordermethod to theContactclass, but that would allow people to accidentally order things from contacts who are customers or family friends. Instead, let's create a newSupplierclass that acts like aContact, but has an additionalordermethod:

```python
class Supplier(Contact):
 def order(self, order):
  print("If this were a real system we would send "
            "{} order to {}".format(order, self.name)
```

# 

```

```

Now, if we test this class in our trusty interpreter, we see that all contacts, including suppliers, accept a name and e-mail address in their\_\_init\_\_, but only suppliers have a functional order method:

```python
>>> c = Contact("Some Body", "somebody@example.net")
>>> s = Supplier("Sup Plier", "supplier@example.net")
>>> print(c.name, c.email, s.name, s.email)
Some Body somebody@example.net Sup Plier supplier@example.net
>>> c.all_contacts
[<__main__.Contact object at 0xb7375ecc>,
<__main__.Supplier object at 0xb7375f8c>]
>>> c.order("Ineed pliers")
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'Contact' object has no attribute 'order'
>>> s.order("I need pliers")
If this were a real system we would send I need pliers order to
Supplier
>>>
```

So now ourSupplierclass can do everything aContactcan do \(including adding itself to the list ofall\_contacts\) and all the special things it needs to handle as a supplier. This is the beauty of inheritance.

One of the most interesting uses of this kind of inheritance is adding functionality to built-in classes. In theContactclass seen earlier, we are adding contacts to a list of all contacts. What if we also wanted to search that list by name? Well, we could add a method on theContactclass to search it, but it feels like this method actually belongs on the list itself. We can do this using inheritance:

```python
class ContactList(list):
 def search(self, name):
   '''Return all contacts that contain the search value
     in their name.'''
   matching_contacts = []
   for contact in self:
     if name in contact.name:
      matching_contacts.append(contact)
   return matching_contacts

class Contact:
 all_contacts = ContactList()

 def __init__(self, name, email):
   self.name = name
   self.email = email
   self.all_contacts.append(self)
```

Instead of instantiating a normal list as our class variable, we create a new `ContactList`class that extends the built-in list. Then we instantiate this subclass as our `all_contacts`list. We can test the new search functionality as follows:

```python
>>> c1 = Contact("John A", "johna@example.net")
>>> c2 = Contact("John B", "johnb@example.net")
>>> c3 = Contact("Jenna C", "jennac@example.net")
>>> [c.name for c in Contact.all_contacts.search('John')]
['John A', 'John B']
>>>
```

Are you wondering how we changed the built-in syntax \[\] into something we can inherit from? Creating an empty list with \[\] is actually a shorthand for creating an empty list using list\(\); the two syntaxes are identical:

```python

```

So, thelistdata type is like a class that we can extend, not unlikeobject.

As a second example, we can extend thedictclass, which is the long way of creating a dictionary \(the{:}syntax\).

```python
class LongNameDict(dict):
 def longest_key(self):
  longest = None
  for key in self:
    if not longest or len(key) > len(longest):
      longest = key
    return longest
```

This is easy to test in the interactive interpreter:

```python
>>> longkeys = LongNameDict()
>>> longkeys['hello'] = 1
>>> longkeys['longest yet'] = 5
>>> longkeys['hello2'] = 'world'
>>> longkeys.longest_key()
'longest yet'
```

Most built-in types can be similarly extended. Commonly extended built-ins areobject,list,set,dict,file, andstr. Numerical types such asintandfloatare also occasionally inherited from.

So inheritance is great for adding new behavior to existing classes, but what about changing behavior? Ourcontactclass allows only a name and an e-mail address. This may be sufficient for most contacts, but what if we want to add a phone number for our close friends?

We can do this easily by just setting a phone attribute on the contact after it is constructed. But if we want to make this third variable available on initialization, we have to**override**\_\_init\_\_. Overriding is altering or replacing a method of the superclass with a new method \(with the same name\) in the subclass. No special syntax is needed to do this; the subclass's newly created method is automatically called instead of the superclass's method. For example:

```python
class Friend(Contact):
 def __init__(self, name, email, phone):
   self.name = name
   self.email = email
   self.phone = phone
```

Any method can be overridden, not just\_\_init\_\_. Before we go on, however, we need to correct some problems in this example. OurContactandFriendclasses have duplicate code to set up thenameandemailproperties; this can make maintenance complicated, as we have to update the code in two or more places. More alarmingly, ourFriendclass is neglecting to add itself to theall\_contactslist we have created on theContactclass.

What we really need is a way to call code on the parent class. This is what thesuperfunction does; it returns the object as an instance of the parent class, allowing us to call the parent method directly:

```python
class Friend(Contact):
 def __init__(self, name, email, phone):
   super().__init__(name, email)
   self.phone = phone
```

This example first gets the instance of the parent object using super, and calls \_\_init\_\_ on that object, passing in the expected arguments. It then does its own initialization, namely setting the phone attribute.

A super\(\) call can be made inside any method, not just \_\_init\_\_ . This means all methods can be modified via overriding and calls to super . The call to super can also be made at any point in the method; we don't have to make the call as the first line in the method. For example, we may need to manipulate the incoming parameters before forwarding them to the superclass.

