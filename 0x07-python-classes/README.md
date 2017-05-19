# 0x07. Python - Classes and Objects
![image](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/247/oop-meme.jpg)

**Author: [Elaine Yeung](https://twitter.com/egsy)**

*Holberton School | January 2017 Batch 2*

## Synopsis
This project is completed as an introduction to the Python programming language.

### Resources 
OOP is a totally new concept for all of you (especially those who think they know about it :)). It&#39;s VERY important that you read at least all the material that is listed bellow. As usual, make sure you type (and as usual never copy &amp; paste), test and understand all examples shown in the following links (including those in the video). The biggest and most important task of this project is the reading. The project itself will not take you more than 2/3 hours (tests excluded) if you take the time to read and understand everything.
- A simple introduction to <a href="https://python.swaroopch.com/oop.html">Object Oriented Programming</a> without going into much detail:
  - Read everything until the paragraph &quot;Inheritance&quot; excluded
  - You do NOT have to learn about class attributes, `classmethod` and `staticmethod` yet
- <a href="http://www.python-course.eu/python3_object_oriented_programming.php">Object-Oriented Programming</a>. Please <strong>be careful</strong>: in most of the following paragraphs, the author shows things the way you should not use or write a class, in order to make you better understand some concepts and how everything works in Python 3. Make sure you read everything. Read only the following paragraphs:
  - General Introduction
  - First-class Everything
  - A Minimal Class in Python
  - Attributes
  - You NOT have to learn about class attributes
  - Methods
  - The `__init__` Method
  - Data Abstraction, Data Encapsulation, and Information Hiding
  - Public- Protected- and Private Attributes
- <a href="http://www.python-course.eu/python3_properties.php">Properties vs. Getters and Setters</a>
- TL;DR; - A good wrap-up video about everything you need to know for this project: <a href="https://www.youtube.com/watch?v=1AGyBuVCTeE&amp;">Learn to Program 9 : Object Oriented Programming</a>

### What students should learn from this project
At the end of this project we are expected to be able to explain to anyone, without the help of Google:
- Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
- What is OOP
- &quot;first-class everything&quot;
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or instance
- What is an attribute
- What are and how to use public, protected and private attributes
- What is `self`
- What is a method
- What is the special `__init__` method and how to use it
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- What is the difference between an attribute and a property in Python
- What is the Pythonic way to write getters and setters in Python
*advanced*:
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is and what does contain `__dict__` of a class and of an instance of a class
- How does Python find the attributes of an object or class
- How to use the `getattr` function

### Requirements for Python scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `PEP 8` style
- All your files must be executable
- The length of your files will be tested using `wc`

### Requirements for Python test cases
- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- All your test files should be text files (extension: `.txt`)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation (`python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;`)
- All your classes should have a documentation (`python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;` and `python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;`)
- We strongly encourage you to work together on test cases, so that you don't miss any edge case


## Project Breakdown
0-square.py
1-square.py
2-square.py
3-square.py
4-square.py, tests/4-square.txt
5-square.py
6-square.py

| Task # | Type | Short description | File name and link |
| ---: | --- | --- | --- |
|0| **Mandatory**  | | File: [0-print_list_integer.py](./print_list_integer.py)
|1| **Mandatory**  | | File: [1-element_at.py](./1-element_at.py)
|2| **Mandatory**  | | File: [2-replace_in_list.py](./2-replace_in_list.py)
|3| **Mandatory**  | | File: [3-print_reversed_list_integer.py](./3-print_reversed_list_integer.py)
|4| **Mandatory**  | | File: [4-new_in_list.py](./4-new_in_list.py)
|5| **Mandatory**  | | File: [5-no_c.py](./5-no_c.py)
|6| **Mandatory**  | | File: [6-print_matrix_integer.py](./6-print_matrix_integer.py)


<p>Write an empty class `Square` that defines a square:</p>
<li>You are not allowed to import any module</li>

<p><strong>No test cases needed</strong></p>
<li>GitHub repository: `holbertonschool-higher_level_programming`</li>
<li>Directory: `0x07-python-classes`</li>
<li>File: `0-square.py`</li>

<p>Write a class `Square` that defines a square by: (based on `0-square.py`)</p>
<li>Private instance attribute: `size`</li>
<li>Instantiation with `size` (no type/value verification)</li>
<li>You are not allowed to import any module</li>

<p><strong>No test cases needed</strong></p>
<li>GitHub repository: `holbertonschool-higher_level_programming`</li>
<li>Directory: `0x07-python-classes`</li>
<li>File: `1-square.py`</li>

<p>Write a class `Square` that defines a square by: (based on `1-square.py`)</p>
<li>Private instance attribute: `size`</li>
<li>Instantiation with optional `size`: `def __init__(self, size=0):`
	<li>`size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`<br></li>
	<li>if `size` is less than `0`, raise a `ValueError` exception with the message `size must be &gt;= 0`</li>
<li>You are not allowed to import any module</li>

<p><strong>No test cases needed</strong></p>
<li>GitHub repository: `holbertonschool-higher_level_programming`</li>
<li>Directory: `0x07-python-classes`</li>
<li>File: `2-square.py`</li>

<p>Write a class `Square` that defines a square by: (based on `2-square.py`)</p>
<li>Private instance attribute: `size`</li>
<li>Instantiation with optional `size`: `def __init__(self, size=0):`
	<li>`size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`<br></li>
	<li>if `size` is less than `0`, raise a `ValueError` exception with the message `size must be &gt;= 0`</li>
<li>Public instance method: `def area(self):` that returns the current square area</li>
<li>You are not allowed to import any module</li>

<p><strong>No test cases needed</strong></p>
<li>GitHub repository: `holbertonschool-higher_level_programming`</li>
<li>Directory: `0x07-python-classes`</li>
<li>File: `3-square.py`</li>

<p>Write a class `Square` that defines a square by: (based on `3-square.py`)</p>
<li>Private instance attribute: `size`:
	<li>property `def size(self):` to retrieve it</li>
	<li>property setter `def size(self, value):` to set it:
	<li>`size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`<br></li>
	<li>if `size` is less than `0`, raise a `ValueError` exception with the message `size must be &gt;= 0`</li>
<li>Instantiation with optional `size`: `def __init__(self, size=0):`</li>
<li>Public instance method: `def area(self):` that returns the current square area</li>
<li>You are not allowed to import any module</li>
<li>GitHub repository: `holbertonschool-higher_level_programming`</li>
<li>Directory: `0x07-python-classes`</li>
<li>File: `4-square.py, tests/4-square.txt`</li>

<p>Write a class `Square` that defines a square by: (based on `4-square.py`)</p>
<li>Private instance attribute: `size`:
	<li>property `def size(self):` to retrieve it</li>
	<li>property setter `def size(self, value):` to set it:
	<li>`size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`<br></li>
	<li>if `size` is less than `0`, raise a `ValueError` exception with the message `size must be &gt;= 0`</li>
<li>Instantiation with optional `size`: `def __init__(self, size=0):`</li>
<li>Public instance method: `def area(self):` that returns the current square area</li>
<li>Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
	<li>if `size` is equal to 0, print an empty line</li>
<li>You are not allowed to import any module</li>

<p><strong>No test cases needed</strong></p>
<li>GitHub repository: `holbertonschool-higher_level_programming`</li>
<li>Directory: `0x07-python-classes`</li>
<li>File: `5-square.py`</li>

<p>Write a class `Square` that defines a square by: (based on `5-square.py`)</p>
<li>Private instance attribute: `size`:
	<li>property `def size(self):` to retrieve it</li>
	<li>property setter `def size(self, value):` to set it:
	<li>`size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`<br></li>
	<li>if `size` is less than `0`, raise a `ValueError` exception with the message `size must be &gt;= 0`</li>
<li>Private instance attribute: `position`:
	<li>property `def position(self):` to retrieve it</li>
	<li>property setter `def position(self, value):` to set it:
	<li>`position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integers`<br></li>
<li>Instantiation with optional `size` and optional `position`: `def __init__(self, size=0, position=(0, 0)):`</li>
<li>Public instance method: `def area(self):` that returns the current square area</li>
<li>Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
	<li>if `size` is equal to 0, print an empty line</li>
	<li>`position` should be use by using space</li>
<li>You are not allowed to import any module</li>

<p><strong>No test cases needed</strong></p>
<li>GitHub repository: `holbertonschool-higher_level_programming`</li>
<li>Directory: `0x07-python-classes`</li>
<li>File: `6-square.py`</li>
