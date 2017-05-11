# 0x04. Python - More Data Structures: Set, Dictionary
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
<p>Read or watch <a href="https://docs.python.org/3.4/tutorial/datastructures.html">Data structures</a> from <a href="https://docs.python.org/3.4/tutorial/index.html">The Python tutorial</a>, <a href="http://www.python-course.eu/python3_lambda.php">Lambda, filter, reduce and map</a> and <a href="https://www.youtube.com/watch?v=1GAC6KQUPeg">Learn to Program 12 Lambda Map Filter Reduce</a>.</p>
<p>man: <code>python3</code></p>

### What students should learn from this project

At the end of this project we are expected to be able to explain to anyone, without the help of Google:
<p>At the end of this project you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>
<li>Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))</li>
<li>What are set and how to use them</li>
<li>What are the most common methods of set and how to use them</li>
<li>When to use sets versus lists</li>
<li>How to iterate into a set</li>
<li>What are dictionary and how to use them</li>
<li>When to use dictionaries versus lists or sets</li>
<li>What is a key in a dictionary</li>
<li>How to iterate into a dictionary</li>
<li>What is a lambda function</li>
<li>What is map, reduce and map functions</li>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS using <code>python3</code> (version 3.4.3)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>PEP 8</code> style</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>


- Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
- What are set and how to use them
- What are the most common methods of set and how to use them
- When to use sets versus lists
- How to iterate into a set
- What are dictionary and how to use them
- When to use dictionaries versus lists or sets
- What is a key in a dictionary
- How to iterate into a dictionary
- What is a lambda function
- What is map, reduce and map functions

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
0-square_matrix_simple.py
1-search_replace.py
2-uniq_add.py
3-common_elements.py
4-only_diff_elements.py
5-number_keys.py
6-print_sorted_dictionary.py
7-update_dictionary.py
8-simple_delete.py
9-multiply_by_2.py
10-best_score.py
11-mutiply_list_map.py

| Task # | Type | Short description | File name and link |
| ---: | --- | --- | --- |
|0| **Mandatory**  | | File: [0-print_list_integer.py](./print_list_integer.py)
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

<p>Write a function that computes the square value of all integers of a matrix.</p><li>Prototype: <code>def square_matrix_simple(matrix=[]):</code></li><li><code>matrix</code> is a 2 dimensional array</li><li>Returns a new matrix:<li>Same size as <code>matrix</code></li><li>Each value should be the square of the value of the input</li><li>Initial matrix should not be modified</li><li>You are not allowed to import any module</li><li>You are allow to use regular loops, <code>map</code>, etc.</li><li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li><li>Directory: <code>0x04-python-more_data_structures</code></li><li>File: <code>0-square_matrix_simple.py</code></li>

<p>Write a function that replaces all occurrences of an element by another in a new list.</p><li>Prototype: <code>def search_replace(my_list, search, replace):</code></li><li><code>list</code> is the initial list</li><li><code>search</code> is the element to replace in the list</li><li><code>replace</code> is the new element</li><li>You are not allowed to import any module</li><li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li><li>Directory: <code>0x04-python-more_data_structures</code></li><li>File: <code>1-search_replace.py</code></li>

<p>Write a function that makes the addition of all unique integers in a list.</p><li>Prototype: <code>def uniq_add(my_list=[]):</code></li><li>You are not allowed to import any module</li><li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li><li>Directory: <code>0x04-python-more_data_structures</code></li><li>File: <code>2-uniq_add.py</code></li>

<p>Write a function that returns a set of common elements in two sets.</p><li>Prototype: <code>def common_elements(set_1, set_2):</code></li><li>You are not allowed to import any module</li><li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li><li>Directory: <code>0x04-python-more_data_structures</code></li><li>File: <code>3-common_elements.py</code></li>

<p>Write a function that returns a set of all elements present in only one set.</p><li>Prototype: <code>def only_diff_elements(set_1, set_2):</code></li><li>You are not allowed to import any module</li><li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li><li>Directory: <code>0x04-python-more_data_structures</code></li><li>File: <code>4-only_diff_elements.py</code></li>

<p>Write a function that returns the number of keys in a dictionary.</p><li>Prototype: <code>def number_keys(my_dict):</code></li><li>You are not allowed to import any module</li><li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li><li>Directory: <code>0x04-python-more_data_structures</code></li><li>File: <code>5-number_keys.py</code></li>

<p>Write a function that prints a dictionary by ordered keys.</p><li>Prototype: <code>def print_sorted_dictionary(my_dict):</code></li><li>You can assume that all keys are string</li><li>Keys should be sorted by alphabetic order</li><li>Only sort keys of the first level (don&#39;t sort keys of a dictionary inside the main dictionary)</li><li>Dictionary values can have any type</li><li>You are not allowed to import any module</li><li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li><li>Directory: <code>0x04-python-more_data_structures</code></li><li>File: <code>6-print_sorted_dictionary.py</code></li>

<p>Write a function that replace or add key/value in a dictionary.</p>
<li>Prototype: <code>def update_dictionary(my_dict, key, value):</code></li>
<li><code>key</code> argument will be always a string</li>
<li><code>value</code> argument will be any type</li>
<li>If a key exists in the dictionary, the value will be replaced</li>
<li>If a key doesn&#39;t exist in the dictionary, it will be created</li>
<li>You are not allowed to import any module</li>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>0x04-python-more_data_structures</code></li>
<li>File: <code>7-update_dictionary.py</code></li>

<p>Write a function that deletes a key in a dictionary.</p>
<li>Prototype: <code>def simple_delete(my_dict, key=&quot;&quot;):</code></li>
<li><code>key</code> argument will be always a string</li>
<li>If a key doesn&#39;t exist, the dictionary won&#39;t change</li>
<li>You are not allowed to import any module</li>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>0x04-python-more_data_structures</code></li>
<li>File: <code>8-simple_delete.py</code></li>

<p>Write a function that returns a new dictionary with all values multiplied by 2</p>
<li>Prototype: <code>def multiply_by_2(my_dict):</code></li>
<li>You can assume that all values are only integers</li>
<li>Returns a new dictionary</li>
<li>You are not allowed to import any module</li>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>0x04-python-more_data_structures</code></li>
<li>File: <code>9-multiply_by_2.py</code></li>

<p>Write a function that returns a key with the biggest integer value.</p>
<li>Prototype: <code>def best_score(my_dict):</code></li>
<li>You can assume that all values are only integers</li>
<li>If no score found, return <code>None</code></li>
<li>You are not allowed to import any module</li>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>0x04-python-more_data_structures</code></li>
<li>File: <code>10-best_score.py</code></li>

<p>Write a function that returns a list with all values multiplied by a number without using any loops.</p>
<li>Prototype: <code>def mutiply_list_map(my_list=[], number=0):</code></li>
<li>Returns a new list:
<li>Same length as <code>my_list</code></li>
<li>Each value should be multiplied by <code>number</code></li>
<li>Initial list should not be modified</li>
<li>You are not allowed to import any module</li>
<li>You have to use <code>map</code></li>
<li>Your file should be max 3 lines</li>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>0x04-python-more_data_structures</code></li>
<li>File: <code>11-mutiply_list_map.py</code></li>
