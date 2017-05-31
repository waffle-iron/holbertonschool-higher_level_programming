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

#### 11.2.4 Closing Files

#### 11.2.5 Closing Files Automatically

#### 11.2.6 Reading Data One Line At A Time

### 11.3 Writing to Text Files

#### 11.3.1 Character Encoding Again

### 11.4 Binary Files



