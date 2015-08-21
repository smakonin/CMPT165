# load up the CGI library
import cgi

# print HTTP/HTML headers
# MOD: needed to change the HTML title from Add to Divide
print """Content-type: text/html

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html><head>
<title>Integer Divide Script</title>
</head><body>
"""

# give me the form data
form = cgi.FieldStorage()

# default values
left = ''
right = ''
total = '?'
error = ''

# is there form data?
if 'left' in form and 'right' in form:
    left = form['left'].value
    right = form['right'].value
    # make sure these are numbers
    if left.isdigit() and right.isdigit():
        # MOD: added a check to prevent divide by zero
        if int(right) == 0:
            error = '<strong>ERROR:</strong> divide by zero!'
        else:
            # all is OK, divide the numbers!
            total = str(int(left) / int(right)) # MOD: needed to change the math operator to divide
    else:
        error = '<strong>ERROR:</strong> non-integer used as input!'

# printing the form
print '<form action="divide.py">' # MOD: changed, make sure to call the right script
print '<br/><br/>'
print '<input type="text" name="left" value="' + left + '"/>'
print '&nbsp;&nbsp;<strong>&divide;</strong>&nbsp;&nbsp;' # MOD: need to change the symbol from + to &divide;
print '<input type="text" name="right" value="' + right + '"/>'
print '&nbsp;&nbsp;<input type="submit" value="=" />'
print '&nbsp;&nbsp;<strong>' + total + '</strong>'
print '<br/><br/>' + error
print '</form></body></html>'
