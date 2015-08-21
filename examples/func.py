# 
# These Python coding exercises wher taken from: http://www.ling.gu.se/~lager/python_exercises.html
#

'''
Define a function max() that takes two numbers as arguments 
and returns the largest of them. Use the if-then-else construct 
available in Python. (It is true that Python has the max() 
function built in, but writing it yourself is nevertheless a 
good exercise.)
'''
def max(value1, value2):
    if value1 > value2:
        return value1
    else:
        return value2

'''
Define a function max3() that takes three numbers as 
arguments and returns the largest of them.
'''
def max3(value1, value2, value3):
    return max(max(value1, value2), value3)

'''
Define a function maxn() that takes a list od numbers 
as an argument and returns the largest of them.

Assume all numbers are > 0 and list is not empty.
'''
def maxn(l):
    m = 0

    for n in l:
        if n > m:
            m = n
        #print n, m # debug

    return m

'''
Define a function reverse() that computes the reversal of 
a string. For example, reverse("I am testing") should return 
the string "gnitset ma I".
'''
def reverse(s):
    r = ''

    for c in list(s):
        r = c + r
        print r # debug

    return r

'''
Define a function repeat_chars() that takes an integer n and 
a character c and returns a string, n characters long. For 
example, repeat_chars(5,"x") should return the string "xxxxx". 
(Python is unusual in that you can actually write an expression 
5 * "x" that will evaluate to "xxxxx". For the sake of the 
exercise you should ignore that the problem can be solved in 
this manner.)
'''    
def repeat_chars(n, c):
    r = ''

    for i in range(n):
        r += c
        #print r # debug

    return r

'''
Define a procedure histogram() that takes a list of integers and 
prints a histogram to the screen. The second argument restricts 
the printing width. For example, histogram([4, 9, 7], 60) 
should print the following:
****
*********
*******
'''
def histogram(l, w):

    m = maxn(l)
    
    for n in l:
        n2 = int(float(n) / float(m) * float(w)) 
        print '%2i | %s' % (n, repeat_chars(n2, '*'))

'''
"99 Bottles of Beer" is a traditional song in the US and Canada. It 
is popular to sing on long trips, as it has a very repetitive format 
which is easy to memorize, and can take a long time to sing. The songs 
simple lyrics are as follows:
       99 bottles of beer on the wall, 99 bottles of beer.
       Take one down, pass it around, 98 bottles of beer on the wall.
The same verse is repeated, each time with one fewer bottle.The song 
is completed when the singer or singers reach zero.
'''
def bottles_song(n):
    
    for i in range(n, 0, -1):
        b1 = 'bottles'
        if i == 1:
            b1 = 'bottle'

        b2 = 'bottles'
        if i - 1 == 1:
            b2 = 'bottle'

        print str(i) + ' ' + b1 + ' of beer on the wall, ' + str(i) + ' ' + b1 + ' of beer.'
        print 'Take one down, pass it around, ' + str(i-1) + ' ' + b2 + ' of beer on the wall.'
        print
    
