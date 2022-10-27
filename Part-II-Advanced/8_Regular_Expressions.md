# 8 Regular Expressions
## 8.1 Basics
- link to the reg ex doc: https://docs.python.org/3/library/re.html
- to search a string for a specified pattern regular expression is used
> there are other ways but a realization of this in an object oriented manner is very complicated to use and to understand therefor "regular expression" has established itself as the standard

## 8.2 re module
- in python the regular expression is implemented in the "built-in" module "re"
- be aware that besides "re.findall()" all searching stops if there is a match
- in general if there is no match "None" will be returned (besides findall)
- re converts teh search patern into a magic that only it understands however this process takes time, if a pattern has to be searched multiple times the "re.complile" method should be used

## 8.3 special characters
- ``[]``: matches a given set of chars => ``[a-t]``
- ``\``: signals a special sequence/ escape special chars => ``\d`` for decimal chars (see 9.8.4) or used to escape the special characters
- ``.``: matches any char (except new-line) => ``he..o`` would match hello and henio
- ``^``: searchs only at the start => ``^regarding``
- ``$``: matches only at the end => ``sincerly``
- ``*``: zero or more occurrences of the previous char => ``l*``
- ``+``: one or more occurences of the previous char => ``l+``
- ``?``: zero or one match of the previous char => ``l?`` 
- ``{}``: specify the number occurances IS MOST USED WITH SEQUENCES => ``(sbc){2}``
- ``|``: either or => ``falls|stays``
- ``()``: capture and group

## 8.4 special sequences:
- ``\A``: returns the match if the specified char is at the beginning => ``\AThe``
- ``\b``: the bginning or end of a word can be specified => ``\BThe``, ``end\B`` (remember to escape the backslash)
- ``\B``: returns a match when the pattern is not in the beginning nor in the end of a word => ``\Bend``
- ``\d``: returns the part of the string that has digits (0-9) => ``\d``
- ``\D``: returns the part of the string that has no digit => ``\D``
- ``\n``: returns a match at a new-line char
- ``\s``: returns the part where the string has a white space => ``\s``
- ``\S``: returns the part where the string does not have a whitespce = ``\S``
- ``\t``: returns a match at the tab char
- ``\w``: returns the part where the string contains (a-z) or (0-9) or ``_`` => ``\w``
- ``\W``: returns the part where the string does not contain (a-z) or (0-9) or ``_`` => ``\W``
- ``\Z``: returns a match where the pattern is at the end of the string

## 8.5 sets
- in brackets groups of chars can be specified
- ``[arn]``: returns a match where a,r, or n is present
- ``[a-n]``: returns a match for any lower case char from a to n
- ``[^arn]``: returns a match for any char besides a,r, or n
- ``[0123]``: returns the match where the specified digits are present
- ``[0-9]``: returns the match for any digit
- ``[05][09]``: returns a match for any two digit in the form of xy where x is a digit from 0 to 5 and y is a digit from 0 to 9
- ``[a-zA-Z]``: returns a match for any char from a to z and A to Z
- ``[+]``: has no special meaning in sets

## 8.6 Functions
- ``match(pattern, string)``: returns a match object for the first match in the beginning of the string (search ends on new line)
- ``search(pattern, string)``: returns a match object if there is a match in the string
- ``findall(pattern, string)``: returns a list of all matches, empty matches will be included
- ``split(pattern, string)``: returns a list with parts of the string cut by the pattern, "maxsplit" parameter defines the numbers of parts
- ``sub(pattern1, pattern2, string)``: returns a string where the pattern1 is replaced by teh pattern2, number of replacements can be specified with the parameter "count"
### 8.6.1 flags
	- every function accepts flags
	- "re.A"/"re.ASCII": ascii only (only til 127 unicode)
	- "re.I"/"re.IGNORECASE": case sensitivity off
	- "re.M"/"re.MULTILINE": matches newline
	- "re.S"/"re.DORALL": the special char "." will match really everything, including new-line and so on
	- "re.X"/"re.VERBOSE": allow comments in regex
	- "re.L"/"re.LOCALE": only to use with bytepatterns  turns on the local case sensitivity

### 8.6.2 Match Object methods
- ``span()``: returns the tuple with start-index and end-index of the match
- ``string()``: returns the searched string
- ``group()``: returns the whole word where the match was found
- ``groups()``: splits the match and stores it in a list

# 8.7 example
- domainsearch in an emailadress: ``re.search("^[a-zA-Z]+@([a-z]*\.[a-z]+)$", email_adress).groups()``