# 
# These Python coding exercises wher taken from: http://www.ling.gu.se/~lager/python_exercises.html
#

s = 'happy day'
print s

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
Define a function max_of_three() that takes three numbers as 
arguments and returns the largest of them.
'''
def max_of_three(value1, value2, value3):
    return max(max(value1, value2), value3)

'''
Define a function that computes the length of a given string. 
(It is true that Python has the len() function built in, but 
writing it yourself is nevertheless a good exercise.)
'''
def length(value):
    count = 0
    array = list(value)
    for i in array:
        count += 1
    return count

'''
Write a function that takes a character (i.e. a string of 
length 1) and returns True if it is a vowel, False otherwise.
'''
def vowel(value):
    v = 'aeiou'

    for c in list(v):
        if value == c:
            return True

    return False

'''
Define a function reverse() that computes the reversal of 
a string. For example, reverse("I am testing") should return 
the string "gnitset ma I".
'''
def reverse(value):
    o = ""
    for c in list(value):
        o = c + o
        print "i=", value, "o=", o

    return o

'''
Define a function repeat_chars() that takes an integer n and 
a character c and returns a string, n characters long. For 
example, repeat_chars(5,"x") should return the string "xxxxx". 
(Python is unusual in that you can actually write an expression 
5 * "x" that will evaluate to "xxxxx". For the sake of the 
exercise you should ignore that the problem can be solved in 
this manner.)
'''
def repeat_chars(num, char):
    s = ""
    for i in range(1,num+1):
        s += char
        #print "i=", i, "s=", s

    return s

'''
Define a procedure histogram() that takes a list of integers and 
prints a histogram to the screen. For example, histogram([4, 9, 7]) 
should print the following:
****
*********
*******
'''
def histogram(l):
    for i in l:
        #print i, '|', repeat_chars(i, '*')
        print '%3d | %s' % (i, repeat_chars(i, '*'))
      
'''
Like histogram(), but create a normalized histogram
'''
def histogram2(l, w):
    m = sorted(l)[-1]
    ll = []
    for i in l:
        ll.append(int(float(i)/float(m)*w))
    histogram(ll)

'''
Like histogram(), but create a normalized histogram
'''
def histogram3(l, w):
    m = sorted(l)[-1]
    for i in l:
        #print i, '|', repeat_chars(i, '*')
        print '%5d | %s' % (i, repeat_chars(int(float(i)/float(m)*w), '*'))

