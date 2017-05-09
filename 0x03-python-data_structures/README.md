# 0x03. Python - Data Structures: Lists, Tuples
![image](https://www.holbertonschool.com/assets/holberton-logo-1cc451260ca3cd297def53f2250a9794810667c7ca7b5fa5879a569a457bf16f.png)

**Author: [Elaine Yeung](https://twitter.com/egsy)**

*Holberton School | January 2017 Batch 2*

## Synopsis
This project is completed as an introduction to the Python programming language.

### Resources
- Read the chapter <a href="https://docs.python.org/3.4/tutorial/modules.html">Modules</a> from <a href="https://docs.python.org/3.4/tutorial/index.html">The Python tutorial</a> and <a href="https://docs.python.org/3.4/tutorial/stdlib.html#command-line-arguments">Command line arguments</a>.
- Python's got style! [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/).
...and of course, last but not least: `man python3`
 <p>Read or watch <a href="https://docs.python.org/3.4/tutorial/introduction.html#lists">3.1.3. Lists</a>, <a href="https://docs.python.org/3.4/tutorial/datastructures.html">Data structures</a> (until <code>5.3. Tuples and Sequences</code> included) from <a href="https://docs.python.org/3.4/tutorial/index.html">The Python tutorial</a> and <a href="https://www.youtube.com/watch?v=A1HUzrvS-Pw">Learn to Program 6 : Lists</a>.</p>

### What students should learn from this project

At the end of this project we are expected to be able to explain to anyone, without the help of Google:
- Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
- What are lists and how to use them
- What are the differences and similarities between strings and lists
- What are the most common methods of lists and how to use them
- How to use lists as stacks and queues
- What are list comprehensions and how to use them
- What are tuples and how to use them
- When to use tuples versus lists
- What is a sequence
- What is tuple packing
- What is sequence unpacking
- What is the <code>del</code> statement and how to use it

### Requirements for Python scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `PEP 8` style
- All your files must be executable
- The length of your files will be tested using `wc`

## Project Breakdown
| Task # | Type | Short description | File name and link |
| ---: | --- | --- | --- |
|0| **Mandatory**  |<p>Write a function that prints all integers of a list.</p>     <ul><li>Prototype: <code>def print_list_integer(my_list=[]):</code></li><li>Format: one integer per line. See example</li><li>You are not allowed to import any module</li><li>You can assume that the list only contains integers</li><li>You are not allowed to cast integers into strings</li><li>You have to use <code>str.format()</code> to print integers</li></ul> | File: [0-print_list_integer.py](./-print_list_integer.py)
|1| **Mandatory**  | | File: [1-element_at.py](./1-element_at.py)
|2| **Mandatory**  | | File: [2-replace_in_list.py](./2-replace_in_list.py)
|3| **Mandatory**  | | File: [3-print_reversed_list_integer.py](./3-print_reversed_list_integer.py)
|4| **Mandatory**  | | File: [4-new_in_list.py](./4-new_in_list.py)
|5| **Mandatory**  | | File: [5-no_c.py](./5-no_c.py)
|6| **Mandatory**  | | File: [6-print_matrix_integer.py](./6-print_matrix_integer.py)
|7| **Mandatory**  | | File: [7-add_tuple.py](./7-add_tuple.py)
|8| **Mandatory**  | | File: [8-multiple_returns.py](./8-multiple_returns.py)
|9| **Mandatory**  | | File: [9-max_intege r.py](./9-max_intege r.py)
|10| **Mandatory**  | | File: [10-divisible_by_2.py](./10-divisible_by_2.py)
|11| **Mandatory**  | | File: [11-delete_at.py](./11-delete_at.py)
|12| **Mandatory**  | | File: [12-switch.py](./12-switch.py)


     <p>Write a function that retrieves an element from a list.</p>
     <ul>
<li>Prototype: <code>def element_at(my_list, idx):</code></li>
<li>If <code>idx</code> is out of range, the function should return <code>None</code> </li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>try/except</code></li>
     <ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>0x03-python-data_structures</code></li>
<li>File: <code>1-element_at.py</code></li>
     <p>Write a function that replaces an element of a list at a specific position.</p>
     <ul>
<li>Prototype: <code>def replace_in_list(my_list, idx, element):</code></li>
<li>If <code>idx</code> is out of range, the function should not modify anything, and returns the original list</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>try/except</code></li>
     <ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>0x03-python-data_structures</code></li>
<li>File: <code>2-replace_in_list.py</code></li>
     <p>Write a function that prints all integers of a list, in reverse order.</p>
     <ul>
<li>Prototype: <code>def print_reversed_list_integer(my_list=[]):</code></li>
<li>Format: one integer per line. See example</li>
<li>You are not allowed to import any module</li>
<li>You can assume that the list only contains integers</li>
<li>You are not allowed to cast integers into strings</li>
<li>You have to use <code>str.format()</code> to print integers</li>
     <ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>0x03-python-data_structures</code></li>
<li>File: <code>3-print_reversed_list_integer.py</code></li>
     <p>Write a function that replaces an element in a list at a specific position without modifying the original list.</p>
     <ul>
<li>Prototype: <code>def new_in_list(my_list, idx, element):</code></li>
<li>If <code>idx</code> is out of range, the function should return a copy of the original <code>list</code></li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>try/except</code></li>
     <ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>0x03-python-data_structures</code></li>
<li>File: <code>4-new_in_list.py</code></li>
     <p>Write a function that removes all characters <code>c</code> and <code>C</code> from a string.</p>
     <ul>
<li>Prototype: <code>def no_c(my_string):</code></li>
<li>The function shoud return the new string</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>str.replace()</code></li>
     <ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>0x03-python-data_structures</code></li>
<li>File: <code>5-no_c.py</code></li>
     <p>Write a function that prints a matrix of integers.</p>
     <ul>
<li>Prototype: <code>def print_matrix_integer(matrix=[[]]):</code></li>
<li>Format: see example</li>
<li>You are not allowed to import any module</li>
<li>You can assume that the list only contains integers</li>
<li>You are not allowed to cast integers into strings</li>
<li>You have to use <code>str.format()</code> to print integers</li>
     <ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>0x03-python-data_structures</code></li>
<li>File: <code>6-print_matrix_integer.py</code></li>
     <p>Write a function that adds 2 tuples.</p>
     <ul>
<li>Prototype: <code>def add_tuple(tuple_a=(), tuple_b=()):</code></li>
<li>Returns a tuple with 2 integers:
  <ul>
    <li>The first element should be the addition of the first element of each argument</li>
    <li>The second element should be the addition of the second element of each argument</li>
<li>You are not allowed to import any module</li>
<li>You can assume that the two tuples will only contain integers</li>
<li>If a tuple is smaller than 2, use the value <code>0</code> for each missing integer</li>
<li>If a tuple is bigger than 2, use only the first 2 integers</li>
     <ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>0x03-python-data_structures</code></li>
<li>File: <code>7-add_tuple.py</code></li>
     <p>Write a function that returns a tuple with the length of a string and its first character.</p>
     <ul>
<li>Prototype: <code>def multiple_returns(sentence):</code></li>
<li>If the sentence is empty, the first character should be equal to <code>None</code></li>
<li>You are not allowed to import any module</li>
     <ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>0x03-python-data_structures</code></li>
<li>File: <code>8-multiple_returns.py</code></li>
     <p>Write a function that finds the biggest integer of a list. </p>
     <ul>
<li>Prototype: <code>def max_integer(my_list=[]):</code></li>
<li>If the list is empty, return <code>None</code></li>
<li>You can assume that the list only contains integers</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use the builtin <code>max()</code></li>
     <ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>0x03-python-data_structures</code></li>
<li>File: <code>9-max_integer.py</code></li>
     <p>Write a function that finds all multiples of 2 in a list.</p>
     <ul>
<li>Prototype: <code>def divisible_by_2(my_list=[]):</code></li>
<li>Return a new list with <code>True</code> or <code>False</code>, depending on wether the integer at the same position in the original list is a multiple of 2</li>
<li>The new list should have the same size as the original list</li>
<li>You are not allowed to import any module</li>
     <ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>0x03-python-data_structures</code></li>
<li>File: <code>10-divisible_by_2.py</code></li>
     <p>Write a function that deletes the item at a specific position in a list.</p>
     <ul>
<li>Prototype: <code>def delete_at(my_list=[], idx=0):</code></li>
<li>You are not allowed to use <code>pop()</code></li>
<li>You are not allowed to import any module</li>
     <ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>0x03-python-data_structures</code></li>
<li>File: <code>11-delete_at.py</code></li>
     <p>Complete the source code in order to switch value of <code>a</code> and <code>b</code></p>
     <ul>
<li>You can find the source code <a href="https://github.com/holbertonschool/0x03.py/blob/master/12-switch_py">here</a></li>
<li>Your code should be inserted where the comment is (line 4)</li>
<li>Your program should be exactly 5 lines long</li>
     <ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>0x03-python-data_structures</code></li>
<li>File: <code>12-switch.py</code></li>
