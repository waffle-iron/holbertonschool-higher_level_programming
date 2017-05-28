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
	
# Multiple inheritance

Multiple inheritance is a touchy subject. In principle, it's very simple: a subclass that inherits from more than one parent class is able to access functionality from both of them. In practice, this is much less useful than it sounds and many expert programmers recommend against using it. So we'll start with a warning:

> As a rule of thumb, if you think you need multiple inheritance, you're probably wrong, but if you know you need it, you're probably right.

The simplest and most useful form of multiple inheritance is called a mixin. A mixin is generally a superclass that is not meant to exist on its own, but is meant to be inherited by some other class to provide extra functionality. For example, let's say we wanted to add functionality to our Contact class that allows sending an e-mail to self.email. Sending e-mail is a common task that we might want to use on many other classes. So we can write a simple mixin class to do the e-mailing for us:

``` python
class MailSender:
 def send_mail(self, message):
   print("Sending mail to " + self.email)
     # Add e-mail logic here
```

For brevity, we won't include the actual e-mail logic here; if you're interested in studying how it's done, see the smtplib module in the Python standard library.

This class doesn't do anything special (in fact, it can barely function as a stand-alone class), but it does allow us to define a new class that is both a Contact and a MailSender, using multiple inheritance:

``` python
class EmailableContact(Contact, MailSender):
pass
```
The syntax for multiple inheritance looks like a parameter list in the class definition. Instead of including one base class inside the parenthesis, we include two (or more), separated by a comma. We can test this new hybrid to see the mixin at work:

``` python
>>> e = EmailableContact("John Smith", "jsmith@example.net")
>>> Contact.all_contacts
[<__main__.EmailableContact object at 0xb7205fac>]
>>> e.send_mail("Hello, test e-mail here")
Sending mail to jsmith@example.net
```

The Contact initializer is still adding the new contact to the all_contacts list, and the mixin is able to send mail to self.email so we know everything is working.

That wasn't so hard, and you're probably wondering what the dire warnings about multiple inheritance are. We'll get into the complexities in a minute, but let's consider what options we had, other than using a mixin here:


  * We could have used single inheritance and added the send_mail function to the subclass. The disadvantage here is that the e-mail functionality then has to be duplicated for any other classes that need e-mail.  
  * We can create a stand-alone Python function for sending mail, and just call that, with the correct e-mail address supplied as a parameter, when e-mail needs to be sent.
  * We could monkey-patch the Contact class to have a send_mail method after the class has been created. This is done by defining a function that accepts the self argument, and setting it as an attribute on an existing class.

Multiple inheritance works all right when mixing methods from different classes, but it gets very messy when we have to work with calling methods on the superclass. Why? Because there are multiple superclasses. How do we know which one to call? How do we know what order to call them in?

Let's explore these questions by adding a home address to our Friend class. What are some ways we could do this? An address is a collection of strings representing the street, city, country, and other related details of the contact. We could pass each of these strings as parameters into the Friend class's __init__ method. We could also store these strings in a tuple or dictionary and pass them into __init__ as a single argument. This is probably the best course of action if there is no additional functionality that needs to be added to the address.

Another option would be to create a new Address class to hold those strings together, and then pass an instance of this class into the __init__ in our Friend class. The advantage of this solution is that we can add behavior (say, a method to give directions to that address or to print a map) to the data instead of just storing it statically. Composition is a perfectly viable solution to this problem and allows us to reuse Address classes in other entities such as buildings, businesses, or organizations.

However, inheritance is also a viable solution, and that's what we want to explore, so let's add a new class that holds an address. We'll call this new class AddressHolder instead of Address, because inheritance defines an "is a" relationship. It is not correct to say a Friend is an Address, but since a friend can have an Address, we can argue that a Friend is an AddressHolder. Later, we could create other entities (companies, buildings) that also hold addresses. Here's our AddressHolder class:

``` python
class AddressHolder:
	def __init__(self, street, city, state, code):
		self.street = street
		self.city = city
		self.state = state
		self.code = code
```

Very simple; we just take all the data and toss it into instance variables upon initialization.

But how can we use this in our existing Friend class, which is already inheriting from Contact? Multiple inheritance, of course. The tricky part is that we now have two parent __init__ methods that both need to be initialized. And they need to be initialized with different arguments. How do we do that? Well, we could start with the naïve approach:

``` python
class Friend(Contact, AddressHolder):
	def __init__(self, name, email, phone,
        street, city, state, code):
	Contact.__init__(self, name, email)
	AddressHolder.__init__(
		self, street, city, state, code)
	self.phone = phone
```

In this example, we directly call the __init__ function on each of the superclasses and explicitly pass the self argument. This example technically works; we can access the different variables directly on the class. But there are a few problems.

First, it is possible for a superclass to go uninitialized if we neglect to explicitly call the initializer. This is not bad in this example, but it could cause bad program crashes in common scenarios. Imagine, for example, trying to insert data into a database that has not been connected to.

Second, and more sinister, is the possibility of a superclass being called multiple times, because of the organization of the class hierarchy. Look at this inheritance diagram:


The __init__ method from the Friend class first calls __init__ on Contact which implicitly initializes the object superclass (remember, all classes derive from object). Friend then calls __init__ on AddressHolder, which implicitly initializes the object superclass... again. The parent class has been set up twice. In this case, that's relatively harmless, but in some situations, it could spell disaster. Imagine trying to connect to a database twice for every request! The base class should only be called once. Once, yes, but when? Do we call Friend then Contact then Object then AddressHolder? Or Friend then Contact then AddressHolder then Object?

Let's look at a second contrived example that illustrates this problem more clearly. Here we have a base class that has a method named call_me. Two subclasses override that method, and then another subclass extends both of these using multiple inheritance. This is called diamond inheritance because of the diamond shape of the class diagram:






Diamonds are what makes multiple inheritance tricky. Technically, all multiple inheritance in Python 3 is diamond inheritance, because all classes inherit from object. The previous diagram, using object.__init__ is also such a diamond.

Converting this diagram to code, this example shows when the methods are called:

``` python
class BaseClass:
  num_base_calls = 0
  def call_me(self):
  print("Calling method on Base Class")
  self.num_base_calls += 1
			
class LeftSubclass(BaseClass):
	num_left_calls = 0
	def call_me(self):
	BaseClass.call_me(self)
	print("Calling method on Left Subclass")
	self.num_left_calls += 1
							
class RightSubclass(BaseClass):
	num_right_calls = 0
	def call_me(self):
	BaseClass.call_me(self)
	print("Calling method on Right Subclass")
	self.num_right_calls += 1
											
class Subclass(LeftSubclass, RightSubclass):
	num_sub_calls = 0
	def call_me(self):
		LeftSubclass.call_me(self)
		RightSubclass.call_me(self)
		print("Calling method on Subclass")
		self.num_sub_calls += 1
```

This example simply ensures each overridden call_me method directly calls the parent method with the same name. Each time it is called, it lets us know by printing the information to the screen, and updates a static variable on the class to show how many times it has been called. If we instantiate one Subclass object and call the method on it once, we get this output:

>>> s = Subclass()
>>> s.call_me()
Calling method on Base Class
Calling method on Left Subclass
Calling method on Base Class
Calling method on Right Subclass
Calling method on Subclass
>>> print(s.num_sub_calls, s.num_left_calls, s.num_right_calls,
s.num_base_calls)
1 1 1 2
>>>

The base class's call_me method has been called twice. This isn't expected behavior and can lead to some very difficult bugs if that method is doing actual work—like depositing into a bank account twice.

The thing to keep in mind with multiple inheritance is that we only want to call the "next" method in the class hierarchy, not the "parent" method. In fact, that next method may not be on a parent or ancestor of the current class. The super keyword comes to our rescue once again. Indeed, super was originally developed to make complicated forms of multiple inheritance possible. Here is the same code written using super:


class BaseClass:
  num_base_calls = 0
    def call_me(self):
	    print("Calling method on Base Class")
		    self.num_base_calls += 1
			
			class LeftSubclass(BaseClass):
			  num_left_calls = 0
			    def call_me(self):
				    super().call_me()
					    print("Calling method on Left Subclass")
						    self.num_left_calls += 1
							
							class RightSubclass(BaseClass):
							  num_right_calls = 0
							    def call_me(self):
								    super().call_me()
									    print("Calling method on Right Subclass")
										    self.num_right_calls += 1
											
											class Subclass(LeftSubclass, RightSubclass):
											  num_sub_calls = 0
											    def call_me(self):
												    super().call_me()
													    print("Calling method on Subclass")
														    self.num_sub_calls += 1
															
The change is pretty minor; we simply replaced the naïve direct calls with calls to super(). This is simple enough, but look at the difference when we execute it:

>>> s = Subclass()
>>> s.call_me()
Calling method on Base Class
Calling method on Right Subclass
Calling method on Left Subclass
Calling method on Subclass
>>> print(s.num_sub_calls, s.num_left_calls, s.num_right_calls,
s.num_base_calls)
1 1 1 1

Looks good, our base method is only being called once. But what is super() actually doing here? Since the print statements are executed after the super calls, the printed output is in the order each method is actually executed. Let's look at the output from back to front to see who is calling what.

First call_me of Subclass calls super().call_me(), which happens to refer to LeftSubclass.call_me(). LeftSubclass.call_me() then calls super().call_me(), but in this case, super() is referring to RightSubclass.call_me(). Pay particular attention to this; the super call is not calling the method on the superclass of LeftSubclass (which is BaseClass), it is calling RightSubclass, even though it is not a parent of LeftSubclass! This is the next method, not the parent method. RightSubclass then calls BaseClass and the super calls have ensured each method in the class hierarchy is executed once.

Can you see how this is going to make things complicated when we return to our Friend multiple inheritance example? In the __init__ method for Friend, we were originally calling __init__ for both parent classes, with different sets of arguments:

``` python
Contact.__init__(self, name, email)
AddressHolder.__init__(self, street, city, state, code)
```

How can we convert this to using super? We don't necessarily know which class super is going to try to initialize first. Even if we did, we need a way to pass the "extra" arguments so that subsequent calls to super, on other subclasses, have the right arguments.

Specifically, if the first call to super passes the name and email arguments to Contact.__init__, and Contact.__init__ then calls super, it needs to be able to pass the address related arguments to the "next" method, which is AddressHolder.__init__.

This is a problem whenever we want to call superclass methods with the same name, but different sets of arguments. Most often, the only time you would want to call a superclass with a completely different set of arguments is in __init__, as we're doing here. Even with regular methods, though, we may want to add optional parameters that only make sense to one subclass or a set of subclasses.

Sadly, the only way to solve this problem is to plan for it from the beginning. We have to design our base class parameter lists so that they accept keyword arguments for any argument that is not required by every subclass implementation. We also have to ensure the method accepts arguments it doesn't expect and pass those on in its super call, in case they are necessary to later methods in the inheritance order.

Python's function parameter syntax provides all the tools we need to do this, but it makes the overall code cumbersome. Have a look at the proper version of the Friend multiple inheritance code:

Python's function parameter syntax provides all the tools we need to do this, but it makes the overall code cumbersome. Have a look at the proper version of the Friend multiple inheritance code:

``` python
class Contact:
  all_contacts = []
  
def __init__(self, name='', email='', **kwargs):
	super().__init__(**kwargs)
	self.name = name
	self.email = email
	self.all_contacts.append(self)
					
class AddressHolder:
	def __init__(self, street='', city='', state='', code='',
	**kwargs):
	super().__init__(**kwargs)
	self.street = street
	self.city = city
	self.state = state
	self.code = code

class Friend(Contact, AddressHolder):
	def __init__(self, phone='', **kwargs):
	super().__init__(**kwargs)
	self.phone = phone															   
```

We've changed all arguments to keyword arguments by giving them an empty string as a default value. We've also ensured that a **kwargs parameter is included to capture any additional parameters that our particular method doesn't know what to do with. It passes these parameters up to the next class with the super call.

If you aren't familiar with the **kwargs syntax, it basically collects any keyword arguments passed into the method that were not explicitly listed in the parameter list. These arguments are stored in a dictionary named kwargs (we can call the variable whatever we like, but convention suggests kw, or kwargs). When we call a different method (for example: super().__init__) with a **kwargs syntax, it unpacks the dictionary and passes the results to the method as normal keyword arguments.

The previous example does what it is supposed to do. But it's starting to look messy, and it has become difficult to answer the question, "What arguments do we need to pass into Friend.__init__?" This is the foremost question for anyone planning to use the class, so a docstring should be added to the method to explain what is happening.

Further, even this implementation is insufficient if we want to "reuse" variables in parent classes. When we pass the **kwargs variable to super, the dictionary does not include any of the variables that were included as explicit keyword arguments. For example, in Friend.__init__, the call to super does not have phone in the kwargs dictionary. If any of the other classes need the phone parameter, we need to ensure it is in the dictionary that is passed. Worse, if we forget to do that, it will be tough to debug, because the superclass will not complain, but will simply assign the default value (in this case, an empty string) to the variable.

There are a few ways to ensure that the variable is passed upwards. Assume the Contact class does, for some reason, need to be initialized with a phone parameter, and the Friend class will also need access to it. We can do any of the following:

* Don't include phone as an explicit keyword argument. Instead, leave it in the kwargs dictionary. Friend can look it up using the syntax kwargs['phone']. When it passes **kwargs to the super call, phone will still be in the dictionary.
* Make phone an explicit keyword argument but update the kwargs dictionary before passing it to super, using the standard dictionary syntax kwargs['phone'] = phone.
* Make phone an explicit keyword argument, but update the kwargs dictionary using the kwargs.update method. This is useful if you have several arguments to update. You can create the dictionary passed into update using either the dict(phone=phone) constructor, or the dictionary syntax {'phone': phone}.
* Make phone an explicit keyword argument, but pass it to the super call explicitly with the syntax super().__init__(phone=phone, **kwargs).

