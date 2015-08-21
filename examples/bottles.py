import func, cgi

print "Content-type: text/plain"
print

# give me the form data
form = cgi.FieldStorage()

bottles = 99

if 'bottles' in form and form['bottles'].value.isdigit():
    bottles = int(form['bottles'].value)

    if bottles < 0:
        bottles = abs(bottles)
    elif bottles == 0:
        bottles = 99

print str(bottles) + ' Bottles of Beer on the Wall Song'
print

func.bottles_song(bottles)
