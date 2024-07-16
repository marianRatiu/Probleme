# One of the things that I like about the Ruby programming language is that it has a "Range" class. Ruby's "Range" objects operate similarly to the output from Python's "range" function, except that they work on more than just numbers. For example, in Ruby, I can iterate over the letters from 'm' to 'z' without having to specify them explicitly.
#
# This week, we're going to create an iterator called str_range that will implement just that: You'll call str_range similarly to how you call the built-in "range" function: With a starting value, an ending value, and an optional step value.  Note that you cannot imply the start of a string range, so the first two parameters are mandatory.  Also, as opposed to Python's numeric ranges, these will be up to and including the final point.
#
# For example, if you invoke str_range('j', 'm'), you'll get a generator back that produces each of the letters of another's book.
#
# Moreover, because we're using Python 3, it should be possible for the starting and ending characters to be in a non-Latin (or even non-alphabetic) script, although in such languages, the idea of "iterating over all characters" doesn't quite exist, and might end up giving you a very, very long series of outputs.

def str_ange(start: int, end: int, step=1):
    start_code = ord(start)
    end_code = ord(end)

    if step == 0:
        raise ValueError("step must be a non-zero value")
    if step > 0 and start_code > end_code:
        return
    if step < 0 and start_code < end_code:
        return

    current_code = start_code

    while (step > 0 and current_code <= end_code) or (step < 0 and current_code >= end_code):
        yield chr(current_code)
        current_code += step


for letter in str_ange('a', 'h'):
    print(letter)
