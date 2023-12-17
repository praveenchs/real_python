"""
*** Regular Expressions ***

In Python, we have the re module. 
The applications for regular expressions are wide-spread, but they are fairly complex, 
so when contemplating using a regex for a certain task, think about alternatives, and come to regexes as a last resort.

An example regex is : "^(From|To|Cc).*?python-list@python.org"

^(caret) = matches text at the begining of the line
(From|To|Cc) = means the line has to start with either "From or To or Cc" seperated by the | (pipe). OR operator
.*? = .(dot) regular expression generally matches any single chartacter

example :
a.b = aab or a1b or axb will be a match 

*(asterisk) = is a quantifier that matches preceding element (character or group)
example:
ab* = abx or abd
if you want more character after ab then

ab.* = abc or abdced or ab12thea


Non-Greedy
In regular expressions, a quantifier is considered "greedy" by default, meaning it will match as much as possible while still allowing the overall pattern to match. However, if you add a ? after the quantifier, it becomes "non-greedy" or "lazy," and it will match as little as possible.

Let's illustrate the concept with an example. Suppose you have the input string:

php
Copy code
<abc><def><ghi>
And you want to extract the content between the angle brackets. If you use the greedy quantifier .* without the ?, the pattern would be:

regex
Copy code
<.*>
This greedy pattern would match the entire string from the first < to the last >:

php
Copy code
<abc><def><ghi>
However, if you make the quantifier non-greedy by adding ?:

regex
Copy code
<.*?>
This non-greedy pattern would match each pair of angle brackets separately:

<abc>
<def>
<ghi>
In the non-greedy version, the .*? part will match as little as possible, stopping at the first > encountered.

"""