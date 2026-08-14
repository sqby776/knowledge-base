---
title: csv — CSV 文件读写
created: 2026-06-18
updated: 2026-07-03
tags: [knowledge-base, python, csv, data-io]
status: archived
sources: [https://docs.python.org/3/library/csv.html]
confidence: low
trust_score: 0.17
---
# csv — CSV 文件读写

> 摘自 Python 官方文档 [csv — CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)，2026-07-03 更新

        # ... process CSV file contents here ...
    

The `csv` module defines the following constants:

csv.QUOTE_ALL¶
    

Instructs `writer` objects to quote all fields.

csv.QUOTE_MINIMAL¶
    

Instructs `writer` objects to only quote those fields which contain special characters such as _delimiter_ , _quotechar_ , `'\r'`, `'\n'` or any of the characters in _lineterminator_.

csv.QUOTE_NONNUMERIC¶
    

Instructs `writer` objects to quote all non-numeric fields.

Instructs `reader` objects to convert all non-quoted fields to type [`float`](functions.html#float "float").

Note

Some numeric types, such as [`bool`](functions.html#bool "bool"), [`Fraction`](fractions.html#fractions.Fraction "fractions.Fraction"), or [`IntEnum`](enum.html#enum.IntEnum "enum.IntEnum"), have a string representation that cannot be converted to [`float`](functions.html#float "float"). They cannot be read in the `QUOTE_NONNUMERIC` and `QUOTE_STRINGS` modes.

csv.QUOTE_NONE¶
    

Instructs `writer` objects to never quote fields. When the current _delimiter_ , _quotechar_ , _escapechar_ , `'\r'`, `'\n'` or any of the characters in _lineterminator_ occurs in output data it is preceded by the current _escapechar_ character. If _escapechar_ is not set, the writer will raise `Error` if any characters that require escaping are encountered. Set _quotechar_ to `None` to prevent its escaping.

Instructs `reader` objects to perform no special processing of quote characters.

csv.QUOTE_NOTNULL¶
    

Instructs `writer` objects to quote all fields which are not `None`. This is similar to `QUOTE_ALL`, except that if a field value is `None` an empty (unquoted) string is written.

Instructs `reader` objects to interpret an empty (unquoted) field as `None` and to otherwise behave as `QUOTE_ALL`.

Added in version 3.12.

csv.QUOTE_STRINGS¶
    

Instructs `writer` objects to always place quotes around fields which are strings. This is similar to `QUOTE_NONNUMERIC`, except that if a field value is `None` an empty (unquoted) string is written.

Instructs `reader` objects to interpret an empty (unquoted) string as `None` and to otherwise behave as `QUOTE_NONNUMERIC`.

Added in version 3.12.

The `csv` module defines the following exception:

_exception _csv.Error¶
    

Raised by any of the functions when an error is detected.

## Dialects and Formatting Parameters¶

To make it easier to specify the format of input and output records, specific formatting parameters are grouped together into dialects. A dialect is a subclass of the `Dialect` class containing various attributes describing the format of the CSV file. When creating `reader` or `writer` objects, the programmer can specify a string or a subclass of the `Dialect` class as the dialect parameter. In addition to, or instead of, the _dialect_ parameter, the programmer can also specify individual formatting parameters, which have the same names as the attributes defined below for the `Dialect` class.

Dialects support the following attributes:

Dialect.delimiter¶
    

A one-character string used to separate fields. It defaults to `','`.

Dialect.doublequote¶
    

Controls how instances of _quotechar_ appearing inside a field should themselves be quoted. When [`True`](constants.html#True "True"), the character is doubled. When [`False`](constants.html#False "False"), the _escapechar_ is used as a prefix to the _quotechar_. It defaults to `True`.

On output, if _doublequote_ is [`False`](constants.html#False "False") and no _escapechar_ is set, `Error` is raised if a _quotechar_ is found in a field.

Dialect.escapechar¶
    

A one-character string used by the writer to escape characters that require escaping:

>   * the _delimiter_ , the _quotechar_ , `'\r'`, `'\n'` and any of the characters in _lineterminator_ are escaped if _quoting_ is set to `QUOTE_NONE`;
> 
>   * the _quotechar_ is escaped if _doublequote_ is [`False`](constants.html#False "False");
> 
>   * the _escapechar_ itself.
> 
> 


On reading, the _escapechar_ removes any special meaning from the following character. It defaults to [`None`](constants.html#None "None"), which disables escaping.

Changed in version 3.11: An empty _escapechar_ is not allowed.

Dialect.lineterminator¶
    

The string used to terminate lines produced by the `writer`. It defaults to `'\r\n'`.

Note

The `reader` is hard-coded to recognise either `'\r'` or `'\n'` as end-of-line, and ignores _lineterminator_. This behavior may change in the future.

Dialect.quotechar¶
    

A one-character string used to quote fields containing special characters, such as the _delimiter_ or the _quotechar_ , or which contain new-line characters (`'\r'`, `'\n'` or any of the characters in _lineterminator_). It defaults to `'"'`. Can be set to `None` to prevent escaping `'"'` if _quoting_ is set to `QUOTE_NONE`.

Changed in version 3.11: An empty _quotechar_ is not allowed.

Dialect.quoting¶
    

Controls when quotes should be generated by the writer and recognised by the reader. It can take on any of the QUOTE_* constants and defaults to `QUOTE_MINIMAL` if _quotechar_ is not `None`, and `QUOTE_NONE` otherwise.

Dialect.skipinitialspace¶
    

When [`True`](constants.html#True "True"), spaces immediately following the _delimiter_ are ignored. The default is [`False`](constants.html#False "False"). When combining `delimiter=' '` with `skipinitialspace=True`, unquoted empty fields are not allowed.

Dialect.strict¶
    

When `True`, raise exception `Error` on bad CSV input. The default is `False`.

## Reader Objects¶

Reader objects (`DictReader` instances and objects returned by the `reader()` function) have the following public methods:

csvreader.__next__()¶
    

Return the next row of the reader’s iterable object as a list (if the object was returned from `reader()`) or a dict (if it is a `DictReader` instance), parsed according to the current `Dialect`. Usually you should call this as `next(reader)`.

Reader objects have the following public attributes:

csvreader.dialect¶
    

A read-only description of the dialect in use by the parser.

csvreader.line_num¶
    

The number of lines read from the source iterator. This is not the same as the number of records returned, as records can span multiple lines.

DictReader objects have the following public attribute:

DictReader.fieldnames¶
    

If not passed as a parameter when creating the object, this attribute is initialized upon first access or when the first record is read from the file.

## Writer Objects¶

`writer` objects (`DictWriter` instances and objects returned by the `writer()` function) have the following public methods. A _row_ must be an iterable of strings or numbers for `writer` objects and a dictionary mapping fieldnames to strings or numbers (by passing them through [`str()`](stdtypes.html#str "str") first) for `DictWriter` objects. Note that complex numbers are written out surrounded by parens. This may cause some problems for other programs which read CSV files (assuming they support complex numbers at all).

csvwriter.writerow(_row_ , _/_)¶
    

Write the _row_ parameter to the writer’s file object, formatted according to the current `Dialect`. Return the return value of the call to the _write_ method of the underlying file object.

Changed in version 3.5: Added support of arbitrary iterables.

csvwriter.writerows(_rows_ , _/_)¶
    

Write all elements in _rows_ (an iterable of _row_ objects as described above) to the writer’s file object, formatted according to the current dialect.

Writer objects have the following public attribute:

csvwriter.dialect¶
    

A read-only description of the dialect in use by the writer.

DictWriter objects have the following public method:

DictWriter.writeheader()¶
    

Write a row with the field names (as specified in the constructor) to the writer’s file object, formatted according to the current dialect. Return the return value of the `csvwriter.writerow()` call used internally.

Added in version 3.2.

Changed in version 3.8: `writeheader()` now also returns the value returned by the `csvwriter.writerow()` method it uses internally.

## Examples¶

The simplest example of reading a CSV file:
    
    
    import csv
    with open('some.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
    

Reading a file with an alternate format:
    
    
    import csv
    with open('passwd', newline='') as f:
        reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
        for row in reader:
            print(row)
    

The corresponding simplest possible writing example is:
    
    
    import csv
    with open('some.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(someiterable)
    

Since [`open()`](functions.html#open "open") is used to open a CSV file for reading, the file will by default be decoded into unicode using the system default encoding (see [`locale.getencoding()`](locale.html#locale.getencoding "locale.getencoding")). To decode a file using a different encoding, use the `encoding` argument of open:
    
    
    import csv
    with open('some.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
    

The same applies to writing in something other than the system default encoding: specify the encoding argument when opening the output file.

Registering a new dialect:
    
    
    import csv
    csv.register_dialect('unixpwd', delimiter=':', quoting=csv.QUOTE_NONE)
    with open('passwd', newline='') as f:
        reader = csv.reader(f, 'unixpwd')
    

A slightly more advanced use of the reader — catching and reporting errors:
    
    
    import csv, sys
    filename = 'some.csv'
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        try:
            for row in reader:
                print(row)
        except csv.Error as e:
            sys.exit(f'file {filename}, line {reader.line_num}: {e}')
    

And while the module doesn’t directly support parsing strings, it can easily be done:
    
    
    import csv
    for row in csv.reader(['one,two,three']):
        print(row)
    

Footnotes

[1] (1,2)

If `newline=''` is not specified, newlines embedded inside quoted fields will not be interpreted correctly, and on platforms that use `\r\n` line endings on write an extra `\r` will be added. It should always be safe to specify `newline=''`, since the csv module does its own ([universal](../glossary.html#term-universal-newlines)) newline handling.

### [Table of Contents](../contents.html)

  * `csv` — CSV File Reading and Writing
    * Module Contents
    * Dialects and Formatting Parameters
    * Reader Objects
    * Writer Objects
    * Examples


#### Previous topic

[File Formats](fileformats.html "previous chapter")

#### Next topic

[`configparser` — Configuration file parser](configparser.html "next chapter")

### This page

  * [Report a bug](../bugs.html)
  * [Improve this page](../improve-page-nojs.html)
  * [Show source ](https://github.com/python/cpython/blob/main/Doc/library/csv.rst?plain=1)


«

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](configparser.html "configparser — Configuration file parser") |
  * [previous](fileformats.html "File Formats") |
  * ![Python logo](../_static/py.svg)
  * [Python](https://www.python.org/) »
  *   *   * [3.14.6 Documentation](../index.html) » 
  * [The Python Standard Library](index.html) »
  * [File Formats](fileformats.html) »
  * [`csv` — CSV File Reading and Writing]()
  * | 
  * Theme AutoLightDark |


© [Copyright](../copyright.html) 2001 Python Software Foundation.   
This page is licensed under the Python Software Foundation License Version 2.   
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.   
See [History and License](/license.html) for more information.  
  
The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)   
  
Last updated on Jul 02, 2026 (18:40 UTC). [Found a bug](/bugs.html)?   
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3. 
  *[/]: Positional-only parameter separator (PEP 570)


---

*最后更新：2026-07-03*
