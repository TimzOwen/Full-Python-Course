
### Regex Pattern matching:

This is the description of a pattern in a text

uses the __re__ module in python when creating  a regex object

__symbols__:

    \d----> represents a digit form 0-9

__Keywords__:

    re.compile---> returns a matched pattern 

Always start by __importing re__ module before writing you code

    import re ---> import the module yo allow you to perform the regex search and pattern matching.

    phone_number = re.compile(r'---strings of words here--') --> raw is used for make sure its raw string to escape special characters

    final_output = phone_number.search()---the specified format of strings.

    return the .group()---. to return the matched string pattern 

#### more deep dive on regex pattern matching

__pipe__ ---> '|' -->used to return a match one of many expression.




### Character classes

__\d__: --> Anu numeric digit from 0-9

__\D__: ---> Any character that is not numeric from 0-9

__\w__: ---> Any letter, numeric digit, or the underscore character.

        Think of it as matching "Word" character

__\W__: ---> Any character that is not numeric, letter or underscore        

__\s__: ---> Any space, tab on new line.

        Think of it as matching "space" characters

__\S__: ---> Any character that is not space,tab or new line
