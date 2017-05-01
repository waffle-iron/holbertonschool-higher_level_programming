<img src="https://www.holbertonschool.com/assets/holberton-logo-1cc451260ca3cd297def53f2250a9794810667c7ca7b5fa5879a569a457bf16f.png" alt="Holberton logo">

# 0x00. Python - Hello, World

### Author: Elaine Yeung

## Synopsis
This project is completed as an introduction to the Python programming language.

![image](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/231/48a9fdbd67c84a328a9df9ec8d93b9ac2458ac37721d7d53e51a27fb2bdc5263.jpg)
### What students should learn from this project

At the end of this project you are expected to be able to explain to anyone, without the help of Google:
- Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
- Who created Python
- Who is Guido van Rossum
- Where does the name 'Python' come from
- What is the Zen of Python
- How to use the Python interpreter
- How to print text and variables using print
- How to use strings
- What are indexing and slicing in Python
- What is the official Holberton Python coding style and how to check your code with PEP 8

### Requirements for Python scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style
- All your files must be executable
- The length of your files will be tested using wc

### Requirements for Shell scripts
- Allowed editors: vi, vim, emacs
- All your scripts will be tested on Ubuntu 14.04 LTS
- All your scripts should be exactly two lines long (wc -l file should print 2)
- All your files should end with a new line
- The first line of all your files should be exactly #!/bin/bash
- All your files must be executable

### Resources
- Read the first three chapters of [The Python tutorial](https://docs.python.org/3.4/tutorial/index.html): [Whetting Your Appetite](https://docs.python.org/3.4/tutorial/appetite.html), [Using the Python Interpreter](https://docs.python.org/3.4/tutorial/interpreter.html) and [An Informal Introduction to Python](https://docs.python.org/3.4/tutorial/introduction.html). For this last chapter (An Informal Introduction to Python), read until 3.1.2. Strings included (you do not have to read '3.1.3 Lists').
- Watch: [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt).
- Python's got style! [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/).
- install it: `sudo apt-get install python3-pep8 (version 1.7)`
 - alternative install using `pip3` (Python3 version of `pip`): [Install](https://pep8.readthedocs.io/en/release-1.7.x/intro.html#installation)
 - If /usr/bin/pep8 doesn’t exist, pep8 is located here /usr/local/lib/python3.4/dist-packages/pep8.py or /usr/lib/python3.4/dist-packages/pep8.py (cp /usr/local/lib/python3.4/dist-packages/pep8.py /usr/bin/pep8 && chmod u+x /usr/bin/pep8 or cp /usr/lib/python3.4/dist-packages/pep8.py /usr/bin/pep8 && chmod u+x /usr/bin/pep8)
- use it: pep8 file.py
... and of course, last but not least: `man python3`

## Project Breakdown
| Task # | Type | Short description | File name and link |
| ---: | --- | --- | --- |
|0 | **Mandatory**  | Write a Shell script that runs a Python script.<br><br>The Python file name will be saved in the environment variable `$PYFILE`| File: [0-run](./0-run) |
|1 | **Mandatory**  | Write a Shell script that runs Python code.<br><br>The Python code will be saved in the environment variable `$PYCODE`| File: [1-run_inline](./1-run_inline) |
|2 | **Mandatory**  | Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.<br><br>Use the function print | File: [2-print.py](./2-print.py) |
|3 | **Mandatory**  | Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.<ul><li>The output of the script should be:</li><ul><li>the number, followed by Battery street,</li><li>followed by a new line</li></ul><li>You are not allowed to cast the variable number into a string</li><li>Your code must be 3 lines long</li><li>You have to use the new print numbers tips</li></ul> | File: [3-print_number.py](./3-print_number.py) |
|4 | **Mandatory**  | Complete the source code in order to print the float stored in the variable `number` with a precision of 2 digits.<br><br> | File: [4-print_float.py](./4-print_float.py) |
|5 | **Mandatory**  | Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable `str`, followed by its first 9 characters.<br><br> | File: [5-print_string.py](./5-print_string.py) |
|6 | **Mandatory**  | Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py) to print `Welcome to Holberton School!`<br><br> | File: [6-concat.py](./6-concat.py) |
|7 | **Mandatory**  | Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py)<br><br><ul><li>You are not allowed to use any loops or conditional statements</li><li>Your program should be exactly 8 lines long</li><li>`word_first_3` should contain the first 3 letters of the variable `word`</li><li>`word_last_2` should contain the last 2 letters of the variable `word`</li><li>`middle_word` should contain the value of the variable `word` without the first and last letters</li></ul> | File: [7-edges.py](./7-edges.py) |
|8 | **Mandatory**  | Complete this source code to print object-oriented programming with Python, followed by a new line.<br><br> | File: [8-concat_edges.py](./8-concat_edges.py) |
|9 | **Mandatory**  | Write a Python script that prints "The Zen of Python", by Tim Peters, followed by a new line.<br><br>Your script should be maximum 98 characters long (please check with `wc -m 9-easter_egg.py`) | File: [9-easter_egg.py](./9-easter_egg.py) |
10 | *Advanced* | ? | File: [](./) |
11 | *Advanced* | ? | File: [](./) |
12 | *Advanced* | ? | File: [](./) |
13 | *Advanced* | ? | File: [](./) |
