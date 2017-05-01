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

|2 | **Mandatory**  | <br><br> | File: [](./) |
|2 | **Mandatory**  | <br><br> | File: [](./) |
|2 | **Mandatory**  | <br><br> | File: [](./) |
|2 | **Mandatory**  | <br><br> | File: [](./) |
|4 | *Advanced* | Write a 64-bit program in assembly that prints Hello, Holberton, followed by a new line. | File: [101-hello_holberton.asm](./101-hello_holberton.asm) |
