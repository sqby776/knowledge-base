---
title: json — JSON 编码与解码
created: 2026-06-18
updated: 2026-07-03
tags: [knowledge-base, python, json, data-io]
status: needs-review
sources: [https://docs.python.org/3/library/json.html]
confidence: low
trust_score: 0.21
---
# json — JSON 编码与解码

> 摘自 Python 官方文档 [json — JSON encoder and decoder](https://docs.python.org/3/library/json.html)，2026-07-03 更新

## Encoders and Decoders¶

_class _json.JSONDecoder(_*_ , _object_hook =None_, _parse_float =None_, _parse_int =None_, _parse_constant =None_, _strict =True_, _object_pairs_hook =None_)¶
    

Simple JSON decoder.

Performs the following translations in decoding by default:

JSON | Python  
---|---  
object | dict  
array | list  
string | str  
number (int) | int  
number (real) | float  
true | True  
false | False  
null | None  
  
It also understands `NaN`, `Infinity`, and `-Infinity` as their corresponding `float` values, which is outside the JSON spec.

_object_hook_ is an optional function that will be called with the result of every JSON object decoded and its return value will be used in place of the given [`dict`](stdtypes.html#dict "dict"). This can be used to provide custom deserializations (e.g. to support [JSON-RPC](https://www.jsonrpc.org) class hinting).

_object_pairs_hook_ is an optional function that will be called with the result of every JSON object decoded with an ordered list of pairs. The return value of _object_pairs_hook_ will be used instead of the [`dict`](stdtypes.html#dict "dict"). This feature can be used to implement custom decoders. If _object_hook_ is also defined, the _object_pairs_hook_ takes priority.

Changed in version 3.1: Added support for _object_pairs_hook_.

_parse_float_ is an optional function that will be called with the string of every JSON float to be decoded. By default, this is equivalent to `float(num_str)`. This can be used to use another datatype or parser for JSON floats (e.g. [`decimal.Decimal`](decimal.html#decimal.Decimal "decimal.Decimal")).

_parse_int_ is an optional function that will be called with the string of every JSON int to be decoded. By default, this is equivalent to `int(num_str)`. This can be used to use another datatype or parser for JSON integers (e.g. [`float`](functions.html#float "float")).

_parse_constant_ is an optional function that will be called with one of the following strings: `'-Infinity'`, `'Infinity'`, `'NaN'`. This can be used to raise an exception if invalid JSON numbers are encountered.

If _strict_ is false (`True` is the default), then control characters will be allowed inside strings. Control characters in this context are those with character codes in the 0–31 range, including `'\t'` (tab), `'\n'`, `'\r'` and `'\0'`.

If the data being deserialized is not a valid JSON document, a `JSONDecodeError` will be raised.

Changed in version 3.6: All parameters are now [keyword-only](../glossary.html#keyword-only-parameter).

decode(_s_)¶
    

Return the Python representation of _s_ (a [`str`](stdtypes.html#str "str") instance containing a JSON document).

`JSONDecodeError` will be raised if the given JSON document is not valid.

raw_decode(_s_)¶
    

Decode a JSON document from _s_ (a [`str`](stdtypes.html#str "str") beginning with a JSON document) and return a 2-tuple of the Python representation and the index in _s_ where the document ended.

This can be used to decode a JSON document from a string that may have extraneous data at the end.

_class _json.JSONEncoder(_*_ , _skipkeys =False_, _ensure_ascii =True_, _check_circular =True_, _allow_nan =True_, _sort_keys =False_, _indent =None_, _separators =None_, _default =None_)¶
    

Extensible JSON encoder for Python data structures.

Supports the following objects and types by default:

Python | JSON  
---|---  
dict | object  
list, tuple | array  
str | string  
int, float, int- & float-derived Enums | number  
True | true  
False | false  
None | null  
  
Changed in version 3.4: Added support for int- and float-derived Enum classes.

To extend this to recognize other objects, subclass and implement a `default()` method with another method that returns a serializable object for `o` if possible, otherwise it should call the superclass implementation (to raise [`TypeError`](exceptions.html#TypeError "TypeError")).

If _skipkeys_ is false (the default), a [`TypeError`](exceptions.html#TypeError "TypeError") will be raised when trying to encode keys that are not [`str`](stdtypes.html#str "str"), [`int`](functions.html#int "int"), [`float`](functions.html#float "float"), [`bool`](functions.html#bool "bool") or `None`. If _skipkeys_ is true, such items are simply skipped.

If _ensure_ascii_ is true (the default), the output is guaranteed to have all incoming non-ASCII and non-printable characters escaped. If _ensure_ascii_ is false, all characters will be output as-is, except for the characters that must be escaped: quotation mark, reverse solidus, and the control characters U+0000 through U+001F.

If _check_circular_ is true (the default), then lists, dicts, and custom encoded objects will be checked for circular references during encoding to prevent an infinite recursion (which would cause a [`RecursionError`](exceptions.html#RecursionError "RecursionError")). Otherwise, no such check takes place.

If _allow_nan_ is true (the default), then `NaN`, `Infinity`, and `-Infinity` will be encoded as such. This behavior is not JSON specification compliant, but is consistent with most JavaScript based encoders and decoders. Otherwise, it will be a [`ValueError`](exceptions.html#ValueError "ValueError") to encode such floats.

If _sort_keys_ is true (default: `False`), then the output of dictionaries will be sorted by key; this is useful for regression tests to ensure that JSON serializations can be compared on a day-to-day basis.

If _indent_ is a non-negative integer or string, then JSON array elements and object members will be pretty-printed with that indent level. An indent level of 0, negative, or `""` will only insert newlines. `None` (the default) selects the most compact representation. Using a positive integer indent indents that many spaces per level. If _indent_ is a string (such as `"\t"`), that string is used to indent each level.

Changed in version 3.2: Allow strings for _indent_ in addition to integers.

If specified, _separators_ should be an `(item_separator, key_separator)` tuple. The default is `(', ', ': ')` if _indent_ is `None` and `(',', ': ')` otherwise. To get the most compact JSON representation, you should specify `(',', ':')` to eliminate whitespace.

Changed in version 3.4: Use `(',', ': ')` as default if _indent_ is not `None`.

If specified, _default_ should be a function that gets called for objects that can’t otherwise be serialized. It should return a JSON encodable version of the object or raise a [`TypeError`](exceptions.html#TypeError "TypeError"). If not specified, `TypeError` is raised.

Changed in version 3.6: All parameters are now [keyword-only](../glossary.html#keyword-only-parameter).

default(_o_)¶
    

Implement this method in a subclass such that it returns a serializable object for _o_ , or calls the base implementation (to raise a [`TypeError`](exceptions.html#TypeError "TypeError")).

For example, to support arbitrary iterators, you could implement `default()` like this:
    
    
    def default(self, o):
       try:
           iterable = iter(o)
       except TypeError:
           pass
       else:
           return list(iterable)
       # Let the base class default method raise the TypeError
       return super().default(o)
    

encode(_o_)¶
    

Return a JSON string representation of a Python data structure, _o_. For example:
    
    
    >>> json.JSONEncoder().encode({"foo": ["bar", "baz"]})
    '{"foo": ["bar", "baz"]}'
    

iterencode(_o_)¶
    

Encode the given object, _o_ , and yield each string representation as available. For example:
    
    
    for chunk in json.JSONEncoder().iterencode(bigobject):
        mysocket.write(chunk)
    

## Exceptions¶

_exception _json.JSONDecodeError(_msg_ , _doc_ , _pos_)¶
    

Subclass of [`ValueError`](exceptions.html#ValueError "ValueError") with the following additional attributes:

msg¶
    

The unformatted error message.

doc¶
    

The JSON document being parsed.

pos¶
    

The start index of _doc_ where parsing failed.

lineno¶
    

The line corresponding to _pos_.

colno¶
    

The column corresponding to _pos_.

Added in version 3.5.

## Standard Compliance and Interoperability¶

The JSON format is specified by [**RFC 7159**](https://datatracker.ietf.org/doc/html/rfc7159.html) and by [ECMA-404](https://ecma-international.org/publications-and-standards/standards/ecma-404/). This section details this module’s level of compliance with the RFC. For simplicity, `JSONEncoder` and `JSONDecoder` subclasses, and parameters other than those explicitly mentioned, are not considered.

This module does not comply with the RFC in a strict fashion, implementing some extensions that are valid JavaScript but not valid JSON. In particular:

  * Infinite and NaN number values are accepted and output;

  * Repeated names within an object are accepted, and only the value of the last name-value pair is used.


Since the RFC permits RFC-compliant parsers to accept input texts that are not RFC-compliant, this module’s deserializer is technically RFC-compliant under default settings.

### Character Encodings¶

The RFC requires that JSON be represented using either UTF-8, UTF-16, or UTF-32, with UTF-8 being the recommended default for maximum interoperability.

As permitted, though not required, by the RFC, this module’s serializer sets _ensure_ascii=True_ by default, thus escaping the output so that the resulting strings only contain printable ASCII characters.

Other than the _ensure_ascii_ parameter, this module is defined strictly in terms of conversion between Python objects and [`Unicode strings`](stdtypes.html#str "str"), and thus does not otherwise directly address the issue of character encodings.

The RFC prohibits adding a byte order mark (BOM) to the start of a JSON text, and this module’s serializer does not add a BOM to its output. The RFC permits, but does not require, JSON deserializers to ignore an initial BOM in their input. This module’s deserializer raises a [`ValueError`](exceptions.html#ValueError "ValueError") when an initial BOM is present.

The RFC does not explicitly forbid JSON strings which contain byte sequences that don’t correspond to valid Unicode characters (e.g. unpaired UTF-16 surrogates), but it does note that they may cause interoperability problems. By default, this module accepts and outputs (when present in the original [`str`](stdtypes.html#str "str")) code points for such sequences.

### Infinite and NaN Number Values¶

The RFC does not permit the representation of infinite or NaN number values. Despite that, by default, this module accepts and outputs `Infinity`, `-Infinity`, and `NaN` as if they were valid JSON number literal values:
    
    
    >>> # Neither of these calls raises an exception, but the results are not valid JSON
    >>> json.dumps(float('-inf'))
    '-Infinity'
    >>> json.dumps(float('nan'))
    'NaN'
    >>> # Same when deserializing
    >>> json.loads('-Infinity')
    -inf
    >>> json.loads('NaN')
    nan
    

In the serializer, the _allow_nan_ parameter can be used to alter this behavior. In the deserializer, the _parse_constant_ parameter can be used to alter this behavior.

### Repeated Names Within an Object¶

The RFC specifies that the names within a JSON object should be unique, but does not mandate how repeated names in JSON objects should be handled. By default, this module does not raise an exception; instead, it ignores all but the last name-value pair for a given name:
    
    
    >>> weird_json = '{"x": 1, "x": 2, "x": 3}'
    >>> json.loads(weird_json)
    {'x': 3}
    

The _object_pairs_hook_ parameter can be used to alter this behavior.

### Top-level Non-Object, Non-Array Values¶

The old version of JSON specified by the obsolete [**RFC 4627**](https://datatracker.ietf.org/doc/html/rfc4627.html) required that the top-level value of a JSON text must be either a JSON object or array (Python [`dict`](stdtypes.html#dict "dict") or [`list`](stdtypes.html#list "list")), and could not be a JSON null, boolean, number, or string value. [**RFC 7159**](https://datatracker.ietf.org/doc/html/rfc7159.html) removed that restriction, and this module does not and has never implemented that restriction in either its serializer or its deserializer.

Regardless, for maximum interoperability, you may wish to voluntarily adhere to the restriction yourself.

### Implementation Limitations¶

Some JSON deserializer implementations may set limits on:

  * the size of accepted JSON texts

  * the maximum level of nesting of JSON objects and arrays

  * the range and precision of JSON numbers

  * the content and maximum length of JSON strings


This module does not impose any such limits beyond those of the relevant Python datatypes themselves or the Python interpreter itself.

When serializing to JSON, beware any such limitations in applications that may consume your JSON. In particular, it is common for JSON numbers to be deserialized into IEEE 754 double precision numbers and thus subject to that representation’s range and precision limitations. This is especially relevant when serializing Python [`int`](functions.html#int "int") values of extremely large magnitude, or when serializing instances of “exotic” numerical types such as [`decimal.Decimal`](decimal.html#decimal.Decimal "decimal.Decimal").

## Command-line interface¶

**Source code:** [Lib/json/tool.py](https://github.com/python/cpython/tree/3.14/Lib/json/tool.py)

* * *

The `json` module can be invoked as a script via `python -m json` to validate and pretty-print JSON objects. The `json.tool` submodule implements this interface.

If the optional `infile` and `outfile` arguments are not specified, [`sys.stdin`](sys.html#sys.stdin "sys.stdin") and [`sys.stdout`](sys.html#sys.stdout "sys.stdout") will be used respectively:
    
    
    $ echo '{"json": "obj"}' | python -m json
    {
        "json": "obj"
    }
    $ echo '{1.2:3.4}' | python -m json
    Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
    

Changed in version 3.5: The output is now in the same order as the input. Use the `--sort-keys` option to sort the output of dictionaries alphabetically by key.

Changed in version 3.14: The `json` module may now be directly executed as `python -m json`. For backwards compatibility, invoking the CLI as `python -m json.tool` remains supported.

### Command-line options¶

infile¶
    

The JSON file to be validated or pretty-printed:
    
    
    $ python -m json mp_films.json
    [
        {
            "title": "And Now for Something Completely Different",
            "year": 1971
        },
        {
            "title": "Monty Python and the Holy Grail",
            "year": 1975
        }
    ]
    

If _infile_ is not specified, read from [`sys.stdin`](sys.html#sys.stdin "sys.stdin").

outfile¶
    

Write the output of the _infile_ to the given _outfile_. Otherwise, write it to [`sys.stdout`](sys.html#sys.stdout "sys.stdout").

\--sort-keys¶
    

Sort the output of dictionaries alphabetically by key.

Added in version 3.5.

\--no-ensure-ascii¶
    

Disable escaping of non-ascii characters, see `json.dumps()` for more information.

Added in version 3.9.

\--json-lines¶
    

Parse every input line as separate JSON object.

Added in version 3.8.

\--indent, \--tab, \--no-indent, \--compact¶
    

Mutually exclusive options for whitespace control.

Added in version 3.9.

-h, \--help¶
    

Show the help message.

Footnotes

[1]

As noted in [the errata for RFC 7159](https://www.rfc-editor.org/errata_search.php?rfc=7159), JSON permits literal U+2028 (LINE SEPARATOR) and U+2029 (PARAGRAPH SEPARATOR) characters in strings, whereas JavaScript (as of ECMAScript Edition 5.1) does not.

### [Table of Contents](../contents.html)

  * `json` — JSON encoder and decoder
    * Basic Usage
    * Encoders and Decoders
    * Exceptions
    * Standard Compliance and Interoperability
      * Character Encodings
      * Infinite and NaN Number Values
      * Repeated Names Within an Object
      * Top-level Non-Object, Non-Array Values
      * Implementation Limitations
    * Command-line interface
      * Command-line options


#### Previous topic

[`email.iterators`: Iterators](email.iterators.html "previous chapter")

#### Next topic

[`mailbox` — Manipulate mailboxes in various formats](mailbox.html "next chapter")

### This page

  * [Report a bug](../bugs.html)
  * [Improve this page](../improve-page-nojs.html)
  * [Show source ](https://github.com/python/cpython/blob/main/Doc/library/json.rst?plain=1)


«

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](mailbox.html "mailbox — Manipulate mailboxes in various formats") |
  * [previous](email.iterators.html "email.iterators: Iterators") |
  * ![Python logo](../_static/py.svg)
  * [Python](https://www.python.org/) »
  *   *   * [3.14.6 Documentation](../index.html) » 
  * [The Python Standard Library](index.html) »
  * [Internet Data Handling](netdata.html) »
  * [`json` — JSON encoder and decoder]()
  * | 
  * Theme AutoLightDark |


© [Copyright](../copyright.html) 2001 Python Software Foundation.   
This page is licensed under the Python Software Foundation License Version 2.   
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.   
See [History and License](/license.html) for more information.  
  
The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)   
  
Last updated on Jul 02, 2026 (18:40 UTC). [Found a bug](/bugs.html)?   
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3. 
  *[*]: Keyword-only parameters separator (PEP 3102)


---

*最后更新：2026-07-03*
