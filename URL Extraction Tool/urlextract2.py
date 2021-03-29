# 1) Write Code : 

from urllib.request import urlopen

page=urlopen("https://www.google.com/")

sourcecode=page.read()
print(sourcecode)

# 2) Run Code : python urlextract2.py
