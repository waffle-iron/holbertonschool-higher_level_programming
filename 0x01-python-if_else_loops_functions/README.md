# 0x01. Python - if/else, loops, functions
![image](https://www.holbertonschool.com/assets/holberton-logo-1cc451260ca3cd297def53f2250a9794810667c7ca7b5fa5879a569a457bf16f.png)

**Author: [Elaine Yeung](https://twitter.com/egsy)**

*Holberton School | January 2017 Batch 2*

## Synopsis
This project is completed as an introduction to the Python programming language.
![image](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/233/code.png)

### What students should learn from this project

At the end of this project we are expected to be able to explain to anyone, without the help of Google:
- Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
- Why indentation is so important in Python
- How to use the `if`, `if ... else` statements
- How to use comments
- How to affect values to variables
- How to use the `while` and `for` loops
- How is the Python's `for` different from the `C's`?
- How to use the `break` and `continues` statements
- How to use `else` clauses on loops
- What does the `pass` statement do, and when to use it
- How to use `range`
- What is a function and how do you use functions
- What does return a function that does not use any `return` statement
- Scope of variables
- What's a traceback
- What are the arithmetic operators and how to use them

### Requirements for Python scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `PEP 8` style
- All your files must be executable
- The length of your files will be tested using `wc`

### Resources
- Read the chapter [More Control Flow Tools](https://docs.python.org/3.4/tutorial/controlflow.html) of [The Python tutorial](https://docs.python.org/3.4/tutorial/index.html). Read until 4.6. Defining Functions included (you do not have to read '4.7. More on Defining Functions').
- Also, read these resources: [Myths about Indentation](http://www.secnetix.de/olli/Python/block_indentation.hawk) and [Indentation Error](https://www.youtube.com/watch?v=1QXOd2ZQs-Q).
- Watch: [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt) and [Learn to Program 2 : Looping](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt).
- Python's got style! [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/).
...and of course, last but not least: `man python3`

## Project Breakdown
| Task # | Type | Short description | File name and link |
| ---: | --- | --- | --- |
|0| **Mandatory**  | <p>This program will assign a random signed number to the variable <code>number</code> each time it is executed. Complete the source code in order to print whether the number stored in the variable <code>number</code> is positive or negative.</p>    <ul>  <li>You can find the source code <a href="https://github.com/holbertonschool/0x01.py/blob/master/0-positive_or_negative_py">here</a></li>  <li>The variable <code>number</code> will store a different value every time you will run this program</li>  <li>You don&#39;t have to understand what <code>import</code>, <code>random. randint</code> do. Please do not touch this code</li>  <li>The output of the program should be:    <ul>  <li>The number, followed by    <ul>  <li>if the number is greater than 0: <code>is positive</code></li>  <li>if the number is 0: <code>is zero</code></li>  <li>if the number is less than 0: <code>is negative</code></li>  </ul></li>  <li>followed by a new line</li>  </ul></li>  </ul> | File: [0-positive_or_negative.py](./0-positive_or_negative.py)|
|1| **Mandatory**  | <p>This program will assign a random signed number to the variable <code>number</code> each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable <code>number</code>.</p><ul><li>You can find the source code <a href="https://github.com/holbertonschool/0x01.py/blob/master/1-last_digit_py">here</a></li><li>The variable <code>number</code> will store a different value every time you will run this program</li><li>You don&#39;t have to understand what <code>import</code>, <code>random. randint</code> do. Please do not touch this code</li><li>The output of the program should be:<ul><li>The string <code>Last digit of</code>, followed by</li><li>the number, followed by</li><li>the string <code>is</code>, followed by<ul><li>if the number is greater than 5: the string <code>and is greater than 5</code></li><li>if the number is 0: the string <code>and is 0</code></li><li>if the number is less than 6 and not 0: the string <code>and is less than 6 and not 0</code></li></ul></li><li>followed by a new line</li></ul></li></ul> | File: [1-last_digit.py](./1-last_digit.py)|
|2| **Mandatory**  | <p>Write a program that prints the alphabet, in lowercase, not followed by a new line.</p><ul><li>You can only use one <code>print</code> function with string format</li><li>You can only use one loop in your code</li><li>You are not allowed to store characters in a variable</li><li>You are not allowed to import any module</li></ul>| File: [2-print_alphabet.py](./2-print_alphabet.py)|
|3| **Mandatory**  |  <p>Write a program that prints the alphabet, in lowercase, not followed by a new line.</p><ul><li>Print all the letters except <code>q</code> and <code>e</code></li><li>You can only use one <code>print</code> function with string format</li><li>You can only use one loop in your code</li><li>You are not allowed to store characters in a variable</li><li>You are not allowed to import any module</li></ul>| File: [3-print_alphabt.py](./3-print_alphabt.py)|
|4| **Mandatory**  |  <p>Write a program that prints all numbers from <code>0</code> to <code>98</code> in decimal and in hexadecimal (as in the following example)</p><ul><li>You can only use one <code>print</code> function with string format</li><li>You can only use one loop in your code</li><li>You are not allowed to store numbers or strings in a variable</li><li>You are not allowed to import any module</li></ul>| File: [4-print_hexa.py](./4-print_hexa.py)|
|5| **Mandatory**  |  <p>Write a program that prints numbers from <code>0</code> to <code>99</code>.</p><ul><li>Numbers must be separated by <code>,</code>, followed by a space</li><li>Numbers should be printed in ascending order, with two digits</li><li>The last number should be followed by a new line</li><li>You can only use no more than 2 <code>print</code> functions with string format</li><li>You can only use one loop in your code</li><li>You are not allowed to store numbers or strings in a variable</li><li>You are not allowed to import any module</li></ul>| File: [5-print_comb2.py](./5-print_comb2.py)|
|6| **Mandatory**  |  <p>Write a program that prints all possible different combinations of two digits.</p><ul><li>Numbers must be separated by <code>,</code>, followed by a space</li><li>The two digits must be different</li><li><code>01</code> and <code>10</code> are considered the same combination of the two digits <code>0</code> and <code>1</code></li><li>Print only the smallest combination of two digits</li><li>Numbers should be printed in ascending order, with two digits</li><li>The last number should be followed by a new line</li><li>You can only use no more than 3 <code>print</code> functions with string format</li><li>You can only use no more than 2 loops in your code</li><li>You are not allowed to store numbers or strings in a variable</li><li>You are not allowed to import any module</li></ul>| File: [6-print_comb3.py](./6-print_comb3.py)|
|7| **Mandatory**  | <p>Write a function that checks for lowercase character. </p><ul><li>Prototype: <code>def islower(c):</code></li><li>Returns <code>True</code> if <code>c</code> is lowercase</li><li>Returns <code>False</code> otherwise</li><li>You are not allowed to import any module</li><li>You are not allowed to use <code>str.upper()</code> and <code>str.isupper()</code></li><li><a href="https://docs.python.org/3.4/library/functions.html?highlight=ord#ord">Tips: ord()</a></li></ul><p>You don&#39;t need to understand <code>__import__</code></p> | File: [7-islower.py](./7-islower.py)|
|8| **Mandatory**  |  <p>Write a function that print a string in uppercase followed by a new line.</p><ul><li>Prototype: <code>def uppercase(str):</code></li><li>You can only use no more than 2 <code>print</code> functions with string format</li><li>You can only use one loop in your code</li><li>You are not allowed to import any module</li><li>You are not allowed to use <code>str.upper()</code> and <code>str.isupper()</code></li><li><a href="https://docs.python.org/3.4/library/functions.html?highlight=ord#ord">Tips: ord()</a></li></ul><p>You don&#39;t need to understand <code>__import__</code></p>| File: [8-uppercase.py](./8-uppercase.py)|
|9| **Mandatory**  |  <p>Write a function that prints the last digit of a number.</p>    <ul>  <li>Prototype: <code>def print_last_digit(number):</code></li>  <li>Returns the value of the last digit</li>  <li>You are not allowed to import any module</li>  </ul> <p>You don&#39;t need to understand <code>__import__</code></p>| File: [9-print_last_digit.py](./9-print_last_digit.py)|
|10| **Mandatory**  |  <p>Write a function that adds two integers and returns the result.</p>    <ul>  <li>Prototype: <code>def add(a, b):</code></li>  <li>Returns the value of <code>a + b</code></li>  <li>You are not allowed to import any module</li>  </ul>    <p>You don&#39;t need to understand <code>__import__</code></p>    | File: [10-add.py](./10-add.py)|
|11| **Mandatory**  |<p>Write a function that computes <code>a</code> to the power of <code>b</code> and return the value.</p><ul><li>Prototype: <code>def pow(a, b):</code></li><li>Returns the value of <code>a ^ b</code></li><li>You are not allowed to import any module</li></ul><p>You don&#39;t need to understand <code>__import__</code></p>| File: [11-pow.py](./11-pow.py)|
|12| **Mandatory**  |  <p>Write a function that prints the numbers from 1 to 100 separated by a space. </p><ul><li>For multiples of three print <code>Fizz</code> instead of the number and for multiples of five print <code>Buzz</code>. </li><li>For numbers which are multiples of both three and five print <code>FizzBuzz</code>.</li><li>Prototype: <code>def fizzbuzz():</code></li><li>Each element should be followed by a space</li><li>You are not allowed to import any module</li></ul><p>You don&#39;t need to understand <code>__import__</code></p>| File: [12-fizzbuzz.py](./12-fizzbuzz.py)|
13 | *Advanced* |<p>Write a program that prints the alphabet, in reverse order, alternating lowercase and uppercase (<code>z</code> in lowercase and <code>Y</code> in uppercase) , not followed by a new line.</p><ul><li>You can only use one <code>print</code> function with string format</li><li>You can only use one loop in your code</li><li>You are not allowed to store characters in a variable</li><li>You are not allowed to import any module</li></ul> | File: [100-print_tebahpla.py](./100-print_tebahpla.py) |
14 | *Advanced* | <p>Write a function that creates a copy of the string, removing the character at the position <code>n</code> (not the Python way, the &quot;C array index&quot;).</p>    <ul>  <li>Prototype: <code>def remove_char_at(str, n):</code></li>  <li>You are not allowed to import any module</li>  </ul>    <p>You don&#39;t need to understand <code>__import__</code></p>  | File: [101-remove_char_at.py](./101-remove_char_at.py)
15 | *Advanced* | <p>Write the Python function <code>def magic_calculation(a, b, c):</code> that does exactly the same as the below Python bytecode </p> | File: [102-magic_calculation.py](./102-magic_calculation.py)

#### Python Bytecode
<pre><code>
3           0 LOAD_FAST                0 (a)
            3 LOAD_FAST                1 (b)
            6 COMPARE_OP               0 (&lt;)
            9 POP_JUMP_IF_FALSE       16
										  
4          12 LOAD_FAST                2 (c)
           15 RETURN_VALUE
														 
5     &gt;&gt;   16 LOAD_FAST                2 (c)
19 LOAD_FAST                1 (b)
22 COMPARE_OP               4 (&gt;)
25 POP_JUMP_IF_FALSE       36

6          28 LOAD_FAST                0 (a)
31 LOAD_FAST                1 (b)
34 BINARY_ADD
35 RETURN_VALUE
																																		   
7     &gt;&gt;   36 LOAD_FAST                0 (a)
39 LOAD_FAST                1 (b)
42 BINARY_MULTIPLY
43 LOAD_FAST                2 (c)
46 BINARY_SUBTRACT
47 RETURN_VALUE
</code></pre>
