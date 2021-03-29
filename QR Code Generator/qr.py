# 1) In Terminal Type : pip install pyqrcode
# 2) Then : pip install pypng 
# 3) Write Code :

import pyqrcode
def qrcode():
    q=pyqrcode.create(input())
    q.png('qrcode.png', scale=6)
    print('QR generated')

if __name__ =='__main__':
    qrcode()

# 4) Run Code : python qr.py
# 5) Give Some Input text
# 6) Msg will printed on screen QR generated and png file will be created in your folder
# 7) Output : 
#    C:\Users\admin\Desktop\Mini-Codes>python qr.py 
#    C:\Users\admin\Desktop\Mini-Codes>python qr.py
#    Python
#    QR generated
