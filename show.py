#!C:\Users\chinh\AppData\Local\Microsoft\WindowsApps\python.exe


import cgi
import cgitb
import os
cgitb.enable()

# HEADERS

print('content-type:text/html\r\n\r\n')
print()

form = cgi.FieldStorage()
pn = str(form.getvalue("pname"))
des = str(form.getvalue("des"))
fle=form['filename']

fn = os.path.basename(fle.filename)
open("E:/O(n) Project/tem/" + fn, "wb").write(fle.file.read())
print('<html>')
print('<body>')
print('<h1>Product Name\n(%s)</h1>'%pn)
print('<img src=temp/%s>'%fn)
print('<h2>%s</h2>'%des)
print('</center><body></html>')