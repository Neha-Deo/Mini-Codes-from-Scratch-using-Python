# 1) In Terminal Type : pip install pyshorteners
# 2) Write Code :

import pyshorteners
url=input("Enter url : ")
shortener=pyshorteners.Shortener()
a=shortener.tinyurl.short(url)
print(a)

# 3) Run Code : python urlshort.py
# 4) Output : 
#    Enter url : https://www.google.com/
#    https://tinyurl.com/cv8mol7
