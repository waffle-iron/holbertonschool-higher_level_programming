# 0x0B. Python - Input/Output
## Readme

- <a href="https://docs.python.org/3.4/tutorial/inputoutput.html#reading-and-writing-files">7.2. Reading and Writing Files</a>
- <a href="https://docs.python.org/3.4/tutorial/errors.html#predefined-clean-up-actions">8.7. Predefined Clean-up Actions</a>
- <a href="http://www.diveintopython3.net/files.html">Files</a> read until <strong>11.4 Binary Files</strong> included
- <a href="https://docs.python.org/3.4/library/json.html">JSON encoder and decoder</a>
- Watch <a href="https://www.youtube.com/watch?v=EukxMIsNeqU">Learn to Program 8 : Reading / Writing Files</a>
<p><em>Tip from <a href="https://twitter.com/dogonthecircuit">Justin Marsh</a></em>: Read more books! <a href="https://automatetheboringstuff.com/">Automate the Boring Stuff with Python</a> ch. 8 p 180-183 and ch. 14 p 326-333.</p>

## 7.2. Reading and Writing Files
`open()` returns a file object, and is most commonly used with two arguments: `open(filename, mode)`.

``` python
>>>
>>> f = open('workfile', 'w')
```

The first argument is a string containing the filename. The second argument is another string containing a few characters describing the way in which the file will be used. mode can be 'r' when the file will only be read, 'w' for only writing (an existing file with the same name will be erased), and 'a' opens the file for appending; any data written to the file is automatically added to the end. 'r+' opens the file for both reading and writing. The mode argument is optional; 'r' will be assumed if it’s omitted.

Normally, files are opened in text mode, that means, you read and write strings from and to the file, which are encoded in a specific encoding. If encoding is not specified, the default is platform dependent (see open()). 'b' appended to the mode opens the file in binary mode: now the data is read and written in the form of bytes objects. This mode should be used for all files that don’t contain text.

In text mode, the default when reading is to convert platform-specific line endings (\n on Unix, \r\n on Windows) to just \n. When writing in text mode, the default is to convert occurrences of \n back to platform-specific line endings. This behind-the-scenes modification to file data is fine for text files, but will corrupt binary data like that in JPEG or EXE files. Be very careful to use binary mode when reading and writing such files.



## 8.7. Predefined Clean-up Actions
Some objects define standard clean-up actions to be undertaken when the object is no longer needed, regardless of whether or not the operation using the object succeeded or failed. Look at the following example, which tries to open a file and print its contents to the screen.

``` python
for line in open("myfile.txt"):
    print(line, end="")
```

The problem with this code is that it leaves the file open for an indeterminate amount of time after this part of the code has finished executing. This is not an issue in simple scripts, but can be a problem for larger applications. The `with` statement allows objects like files to be used in a way that ensures they are always cleaned up promptly and correctly.
	
``` python
	with open("myfile.txt") as f:
	    for line in f:
		        print(line, end="")
```

After the statement is executed, the file f is always closed, even if a problem was encountered while processing the lines. Objects which, like files, provide predefined clean-up actions will indicate this in their documentation.

## Chapter 11. Files: Diving In

My Windows laptop had 38,493 files before I installed a single application. Installing Python 3 added almost 3,000 files to that total. Files are the primary storage paradigm of every major operating system; the concept is so ingrained that most people would have trouble imagining an alternative. Your computer is, metaphorically speaking, drowning in files.

### 11.2 Reading From Text Files

Before you can read from a file, you need to open it. Opening a file in Python couldn’t be easier:

``` python
a_file = open('examples/chinese.txt', encoding='utf-8')
```

Python has a built-in `open()` function, which takes a filename as an argument. Here the filename is `'examples/chinese.txt'`. There are five interesting things about this filename:

1. It’s not just the name of a file; it’s a combination of a directory path and a filename. A hypothetical file-opening function could have taken two arguments — a directory path and a filename — but the open() function only takes one. In Python, whenever you need a “filename,” you can include some or all of a directory path as well.
2. The directory path uses a forward slash, but I didn’t say what operating system I was using. Windows uses backward slashes to denote subdirectories, while Mac OS X and Linux use forward slashes. But in Python, forward slashes always Just Work, even on Windows.
3. The directory path does not begin with a slash or a drive letter, so it is called a relative path. Relative to what, you might ask? Patience, grasshopper.
4. It’s a string. All modern operating systems (even Windows!) use Unicode to store the names of files and directories. Python 3 fully supports non-ascii pathnames.
5. It doesn’t need to be on your local disk. You might have a network drive mounted. That “file” might be a figment of an entirely virtual filesystem. If your computer considers it a file and can access it as a file, Python can open it.

But that call to the `open()` function didn’t stop at the filename. There’s another argument, called `encoding`. Oh dear, that sounds dreadfully familiar.


#### 11.2.1 Character Encoding Rears Its Ugly Head
Bytes are bytes; characters are an abstraction. A string is a sequence of Unicode characters. But a file on disk is not a sequence of Unicode characters; a file on disk is a sequence of bytes. So if you read a “text file” from disk, how does Python convert that sequence of bytes into a sequence of characters? It decodes the bytes according to a specific character encoding algorithm and returns a sequence of Unicode characters (otherwise known as a string).

``` python
# This example was created on Windows. Other platforms may
# behave differently, for reasons outlined below.
>>> file = open('examples/chinese.txt')
>>> a_string = file.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    File "C:\Python31\lib\encodings\cp1252.py", line 23, in decode
	    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
		UnicodeDecodeError: 'charmap' codec can't decode byte 0x8f in position 28: character maps to <undefined>
>>> 		
```
What just happened? You didn’t specify a character encoding, so Python is forced to use the default encoding. What’s the default encoding? If you look closely at the traceback, you can see that it’s dying in cp1252.py, meaning that Python is using CP-1252 as the default encoding here. (CP-1252 is a common encoding on computers running Microsoft Windows.) The CP-1252 character set doesn’t support the characters that are in this file, so the read fails with an ugly UnicodeDecodeError.

But wait, it’s worse than that! The default encoding is platform-dependent, so this code might work on your computer (if your default encoding is utf-8), but then it will fail when you distribute it to someone else (whose default encoding is different, like CP-1252).

> If you need to get the default character encoding, import the locale module and call locale.getpreferredencoding(). On my Windows laptop, it returns 'cp1252', but on my Linux box upstairs, it returns 'UTF8'. I can’t even maintain consistency in my own house! Your results may be different (even on Windows) depending on which version of your operating system you have installed and how your regional/language settings are configured. This is why it’s so important to specify the encoding every time you open a file.

#### 11.2.2 Stream Objects

So far, all we know is that Python has a built-in function called open(). 

The open() function returns a stream object, which has methods and attributes for getting information about and manipulating a stream of characters.

```Python
>>> a_file = open('examples/chinese.txt', encoding='utf-8')
>>> a_file.name                                              ①
'examples/chinese.txt'
>>> a_file.encoding                                          ②
'utf-8'
>>> a_file.mode                                              ③
'r'
```
1. The name attribute reflects the name you passed in to the open() function when you opened the file. It is not normalized to an absolute pathname.
2. Likewise, encoding attribute reflects the encoding you passed in to the open() function. If you didn’t specify the encoding when you opened the file (bad developer!) then the encoding attribute will reflect locale.getpreferredencoding().
3. The mode attribute tells you in which mode the file was opened. You can pass an optional mode parameter to the open() function. You didn’t specify a mode when you opened this file, so Python defaults to 'r', which means “open for reading only, in text mode.” As you’ll see later in this chapter, the file mode serves several purposes; different modes let you write to a file, append to a file, or open a file in binary mode (in which you deal with bytes instead of strings).

> The documentation for the open() function lists all the possible file modes.

#### 11.2.3 Reading Data From A Text File

After you open a file for reading, you’ll probably want to read from it at some point.

```Python
>>> a_file = open('examples/chinese.txt', encoding='utf-8')
>>> a_file.read()                                            ①
'Dive Into Python 是为有经验的程序员编写的一本 Python 书。\n'
>>> a_file.read()                                            ②
''
```
1. Once you open a file (with the correct encoding), reading from it is just a matter of calling the stream object’s read() method. The result is a string.
2. Perhaps somewhat surprisingly, reading the file again does not raise an exception. Python does not consider reading past end-of-file to be an error; it simply returns an empty string.

What if you want to re-read a file?

``` Python
# continued from the previous example
>>> a_file.read()                      ①
''
>>> a_file.seek(0)                     ②
0
>>> a_file.read(16)                    ③
'Dive Into Python'
>>> a_file.read(1)                     ④
' '
>>> a_file.read(1)
'是'
>>> a_file.tell()                      ⑤
20
```
  1. Since you’re still at the end of the file, further calls to the stream object’s read() method simply return an empty string.

  2. The seek() method moves to a specific byte position in a file.

  3. The read() method can take an optional parameter, the number of characters to read.

  4. If you like, you can even read one character at a time.

  5. 16 + 1 + 1 = … 20?
  
Let’s try that again.

``` Python
# continued from the previous example
>>> a_file.seek(17)                    ①
17
>>> a_file.read(1)                     ②
'是'
>>> a_file.tell()                      ③
20
```

  1. Move to the 17th byte.

  2. Read one character.

  3. Now you’re on the 20th byte.
  
Do you see it yet? The seek() and tell() methods always count bytes, but since you opened this file as text, the read() method counts characters. Chinese characters require multiple bytes to encode in utf-8. The English characters in the file only require one byte each, so you might be misled into thinking that the seek() and read() methods are counting the same thing. But that’s only true for some characters.

But wait, it gets worse!

``` Python
>>> a_file.seek(18)                         ①
18
>>> a_file.read(1)                          ②
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
      a_file.read(1)
  File "C:\Python31\lib\codecs.py", line 300, in decode
  (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf8' codec can't decode byte 0x98 in position 0: unexpected code byte			
```
	1. Move to the 18th byte and try to read one character. 
	2. Why does this fail? Because there isn’t a character at the 18th byte. The nearest character starts at the 17th byte (and goes for three bytes). Trying to read a character from the middle will fail with a UnicodeDecodeError.
	




#### 11.2.4 Closing Files
Open files consume system resources, and depending on the file mode, other programs may not be able to access them. It’s important to close files as soon as you’re finished with them.

``` Python
# continued from the previous example
>>> a_file.close()
```

Well that was anticlimactic.

The stream object a_file still exists; calling its close() method doesn’t destroy the object itself. But it’s not terribly useful.

``` Python
# continued from the previous example
>>> a_file.read()                           ①
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
      a_file.read()
ValueError: I/O operation on closed file.
>>> a_file.seek(0)                          ②
Traceback (most recent call last):
	File "<pyshell#25>", line 1, in <module>
		a_file.seek(0)
ValueError: I/O operation on closed file.
>>> a_file.tell()                           ③
	Traceback (most recent call last):
		File "<pyshell#26>", line 1, in <module>
			a_file.tell()
	ValueError: I/O operation on closed file.
>>> a_file.close()                          ④
>>> a_file.closed                           ⑤
	True
```

1. You can’t read from a closed file; that raises an IOError exception.

2. You can’t seek in a closed file either.

3. There’s no current position in a closed file, so the tell() method also fails.

4. Perhaps surprisingly, calling the close() method on a stream object whose file has been closed does not raise an exception. It’s just a no-op.

5. Closed stream objects do have one useful attribute: the closed attribute will confirm that the file is closed.

#### 11.2.5 Closing Files Automatically
Stream objects have an explicit `close()` method, but what happens if your code has a bug and crashes before you call `close()`? That file could theoretically stay open for much longer than necessary. While you’re debugging on your local computer, that’s not a big deal. On a production server, maybe it is.

Python 2 had a solution for this: the try..finally block. That still works in Python 3, and you may see it in other people’s code or in older code that was ported to Python 3. But Python 2.6 introduced a cleaner solution, which is now the preferred solution in Python 3: the `with` statement.

``` Python
with open('examples/chinese.txt', encoding='utf-8') as a_file:
    a_file.seek(17)
	a_character = a_file.read(1)
	print(a_character)
```


  * This code calls `open()`, but it never calls `a_file.close()`. The `with` statement starts a code block, like an `if` statement or a `for` loop. 
  
  * Inside this code block, you can use the variable `a_file` as the stream object returned from the call to `open()`. 
  
  * All the regular stream object methods are available — `seek()`, `read()`, whatever you need. When the `with` block ends, Python calls `a_file.close()` automatically.
			
Here’s the kicker: no matter how or when you exit the `with` block, Python will close that file… even if you “exit” it via an unhandled exception. That’s right, even if your code raises an exception and your entire program comes to a screeching halt, that file will get closed. Guaranteed.

> In technical terms, the with statement creates a runtime context. In these examples, the stream object acts as a context manager. Python creates the stream object a_file and tells it that it is entering a runtime context. When the with code block is completed, Python tells the stream object that it is exiting the runtime context, and the stream object calls its own close() method. See Appendix B, “Classes That Can Be Used in a with Block” for details.

There’s nothing file-specific about the with statement; it’s just a generic framework for creating runtime contexts and telling objects that they’re entering and exiting a runtime context. If the object in question is a stream object, then it does useful file-like things (like closing the file automatically). But that behavior is defined in the stream object, not in the with statement. There are lots of other ways to use context managers that have nothing to do with files. You can even create your own, as you’ll see later in this chapter.

#### 11.2.6 Reading Data One Line At A Time

A “line” of a text file is just what you think it is — you type a few words and press ENTER, and now you’re on a new line. A line of text is a sequence of characters delimited by… what exactly? Well, it’s complicated, because text files can use several different characters to mark the end of a line. Every operating system has its own convention. Some use a carriage return character, others use a line feed character, and some use both characters at the end of every line.

Now breathe a sigh of relief, because Python handles line endings automatically by default. If you say, “I want to read this text file one line at a time,” Python will figure out which kind of line ending the text file uses and and it will all Just Work.

> If you need fine-grained control over what’s considered a line ending, you can pass the optional newline parameter to the open() function. See the open() function documentation for all the gory details.

So, how do you actually do it? Read a file one line at a time, that is. It’s so simple, it’s beautiful.

``` Python
line_number = 0
with open('examples/favorite-people.txt', encoding='utf-8') as a_file:  ①
    for a_line in a_file:                                               ②
		line_number += 1
		print('{:>4} {}'.format(line_number, a_line.rstrip()))          ③
```

1. Using the with pattern, you safely open the file and let Python close it for you.

2. To read a file one line at a time, use a for loop. That’s it. Besides having explicit methods like read(), the stream object is also an iterator which spits out a single line every time you ask for a value.

3. Using the format() string method, you can print out the line number and the line itself. The format specifier {:>4} means “print this argument right-justified within 4 spaces.” The a_line variable contains the complete line, carriage returns and all. The rstrip() string method removes the trailing whitespace, including the carriage return characters.

``` Python
you@localhost:~/diveintopython3$ python3 examples/oneline.py
	1 Dora
    2 Ethan
	3 Wesley
	4 John
	5 Anne
	6 Mike
	7 Chris
	8 Sarah
	9 Alex
	10 Lizzie
```

Did you get this error?
	
``` Python
	you@localhost:~/diveintopython3$ python3 examples/oneline.py
	Traceback (most recent call last):
	File "examples/oneline.py", line 4, in <module>
	print('{:>4} {}'.format(line_number, a_line.rstrip()))
	ValueError: zero length field name in format
```

	If so, you’re probably using Python 3.0. You should really upgrade to Python 3.1.
	
	Python 3.0 supported string formatting, but only with explicitly numbered format specifiers. Python 3.1 allows you to omit the argument indexes in your format specifiers. Here is the Python 3.0-compatible version for comparison:
	
``` Python
	print('{0:>4} {1}'.format(line_number, a_line.rstrip()))
```



### 11.3 Writing to Text Files
You can write to files in much the same way that you read from them. First you open a file and get a stream object, then you use methods on the stream object to write data to the file, then you close the file.

To open a file for writing, use the open() function and specify the write mode. There are two file modes for writing:

“Write” mode will overwrite the file. Pass mode='w' to the open() function.
“Append” mode will add data to the end of the file. Pass mode='a' to the open() function.
Either mode will create the file automatically if it doesn’t already exist, so there’s never a need for any sort of fiddly “if the file doesn’t exist yet, create a new empty file just so you can open it for the first time” function. Just open a file and start writing.

You should always close a file as soon as you’re done writing to it, to release the file handle and ensure that the data is actually written to disk. As with reading data from a file, you can call the stream object’s close() method, or you can use the with statement and let Python close the file for you. I bet you can guess which technique I recommend.

``` Python
>>> with open('test.log', mode='w', encoding='utf-8') as a_file:  ①
...     a_file.write('test succeeded')                            ②
>>> with open('test.log', encoding='utf-8') as a_file:
...     print(a_file.read())                              
test succeeded
>>> with open('test.log', mode='a', encoding='utf-8') as a_file:  ③
...     a_file.write('and again')
>>> with open('test.log', encoding='utf-8') as a_file:
...     print(a_file.read())                              
test succeededand again                                           ④
```

1. You start boldly by creating the new file test.log (or overwriting the existing file), and opening the file for writing. The mode='w' parameter means open the file for writing. Yes, that’s all as dangerous as it sounds. I hope you didn’t care about the previous contents of that file (if any), because that data is gone now.

2. You can add data to the newly opened file with the write() method of the stream object returned by the open() function. After the with block ends, Python automatically closes the file.

3. That was so fun, let’s do it again. But this time, with mode='a' to append to the file instead of overwriting it. Appending will never harm the existing contents of the file.

4. Both the original line you wrote and the second line you appended are now in the file test.log. Also note that neither carriage returns nor line feeds are included. Since you didn’t write them explicitly to the file either time, the file doesn’t include them. You can write a carriage return with the '\r' character, and/or a line feed with the '\n' character. Since you didn’t do either, everything you wrote to the file ended up on one line.④③②①
