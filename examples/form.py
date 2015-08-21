import cgi

form = cgi.FieldStorage()
text1 = form.getvalue("text1")
text2 = form.getvalue("text2")

# print HTTP/HTML headers
print """Content-type: text/html

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html><head>
<title>A CGI Script</title>
</head><body>
"""

# print HTML body using form data
print "<p>In the first text box, you entered " + text1 + ".</p>"
print "<p>In the second text box, you entered " + text2 + ".</p>"
print "</body></html>"