import cgi

print '''Content-type: text/html

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html><head>
<title>Company X - Login</title>
</head><body>
'''

success_msg = ', you have successfully logged in.'
error_msg = 'Username and/or password is incorrect.'
name = ''
valid = False # only make True, if login is corrent
first = True # only make False, form submitted

form = cgi.FieldStorage()

if 'username' in form and 'password' in form:
    username = form.getvalue('username')
    password = form.getvalue('password')
    
    # check to see if username and password are correct
    f = open('users.csv', 'r')
    for line in f:
        values = line.strip().split(', ')
        db_username = values[0]
        db_fname = values[1]
        db_lname = values[2]
        db_password = values[3]

        print values
        
        if username == db_username and password == db_password:
            # success
            name = db_fname + ' ' + db_lname
            valid = True
            break

    f.close()
    first = False

if valid:
    print name + success_msg
else:
    if not first:
        print error_msg

    print '<form action="login.py">'
    print '<h1>Company X - Login</h1>'
    print 'Username: <input type="text" name="username" value="" maxlength="24" /><br/>'
    print 'Password: <input type="password" name="password" value="" maxlength="10" /><br/>'
    print '<input type="submit" value="Login"/>'
    print '</form>'

print '</body></html>'





