import sys
import webbrowser
import requests
from PyQt5 import QtGui ,QtWidgets
app= QtWidgets.QApplication(sys.argv)
wd=QtWidgets.QWidget()
#for window
class window:
    wd.setWindowTitle('PROXY_NKCP : v 1.0')
    wd.setWindowIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\start\\PyQt5\\img\\icon.png'))
#for buttons
class buttons:
    but1 = QtWidgets.QPushButton('HTTPS', wd)
    but2 = QtWidgets.QPushButton('SOCKS4', wd)
    but3 = QtWidgets.QPushButton('SOCKS5', wd)
    but4 = QtWidgets.QPushButton('GITHUB', wd)
    but5 = QtWidgets.QPushButton('TELEGRAM', wd)
    but6 = QtWidgets.QPushButton('INSTAGRAM', wd)
    but7= QtWidgets.QPushButton('EXIT',wd)
#proxy  def
#http
def proxyhttp():
    url = 'https://www.proxy-list.download/api/v1/get?type=https'
    r = requests.get(url).text
    with  open('https[NOUREDINE_KN].txt', 'w') as rusalt:
        rusalt.write(r)
        ms1 = QtWidgets.QMessageBox.about(wd, 'SAVE', ' YOUR PROXY SAVE AS HTTPS[NOUREDINE_KN].txt')
#socks5
def proxysocks5():
    url = 'https://www.proxy-list.download/api/v1/get?type=socks5'
    r = requests.get(url).text
    with  open('SOCKS5[NOUREDINE_KN].txt', 'w') as rusalt:
        rusalt.write(r)
        ms1 = QtWidgets.QMessageBox.about(wd, 'SAVE', ' YOUR PROXY SAVE AS SOCKS5[NOUREDINE_KN].txt')
#sock4
def proxysocks4():
    url = 'https://www.proxy-list.download/api/v1/get?type=socks4'
    r = requests.get(url).text
    with  open('SOCKS4[NOUREDINE_KN].txt', 'w') as rusalt:
        rusalt.write(r)
        ms1 = QtWidgets.QMessageBox.about(wd, 'SAVE', 'YOUR PROXY SAVE AS SOCKS4[NOUREDINE_KN].txt')
#about
def tg():
    webbrowser.open_new_tab('https://t.me/nkcp_tm')
def ig():
    webbrowser.open_new_tab('https://www.instagram.com/nouredine_kn/')
def git():
    webbrowser.open_new_tab('https://github.com/nouredinekn')


#label
class lbl:
    l1=QtWidgets.QLabel('➠CLICK OF YOUR PROXY⤵',wd)
    l2=QtWidgets.QLabel('©THIS TOOL DEV BY NOUREDINE KAOINE',wd)
#style
class style:
    bs='''background-color:#fecf6a; 
      border:4px solid #ca8b01; 
      border-radius:20px;
      font-size:20px;
      color:#654500;
      font-family:Franklin Gothic Medium;
      '''
    ws='background-color:#FDB71F;'
    bs2='''background-color:#75c0e0; 
      border:1px solid #1c5f7c; 
      border-radius:10px;
      font-size:11px;
      color:#091f29;
    '''
    bs3='''background-color:#ffffff; 
      border:1px solid #ffffff; 
      border-radius:10px;
      font-size:11px;
      color:black;
    '''
    bs4='''background-color:#e2569f; 
      border:1px solid #e2569f; 
      border-radius:10px;
      font-size:11px;
      color:#ffffff;
    '''
    bs5='''background-color:#ff4336; 
      border:3px solid #e47d75 ; 
      border-radius:20px;
      font-size:17px;
      color:black;
      font-family:Comic Sans MS;
      '''
    lbl.l2.setStyleSheet('color:#654500;font-size:12px;font-family:Comic Sans MS')
    buttons.but4.setStyleSheet(bs3) ;buttons.but5.setStyleSheet(bs2);buttons.but6.setStyleSheet(bs4)
    l1='color:#654500;font-size:27px;font-family:Comic Sans MS'
    lbl.l1.setStyleSheet(l1)
    wd.setStyleSheet(ws)
    buttons.but1.setStyleSheet(bs),buttons.but2.setStyleSheet(bs),buttons.but3.setStyleSheet(bs),buttons.but7.setStyleSheet(bs5)

#UI
class resize:
    wd.resize(700, 400)
    buttons.but1.resize(100,50),buttons.but2.resize(100,50),buttons.but3.resize(100,50)
    buttons.but4.move(70, 20), buttons.but4.move(70,20), buttons.but4.move(70,20)
class move:
    lbl.l1.move(180, 30),lbl.l2.move(220,345)
    buttons.but4.move(10,300) , buttons.but5.move(10,330) ,buttons.but6.move(10,360)
    buttons.but1.move(300,110), buttons.but2.move(300,170), buttons.but3.move(300,230)
    buttons.but7.move(620,360)
class icons:
    xx='C:\\Users\\hp\\Desktop\\start\\PyQt5\\img\\binary-code.png'
    tyg='C:\\Users\\hp\\Desktop\\start\\PyQt5\\img\\telegram.png'
    git = 'C:\\Users\\hp\\Desktop\\start\\PyQt5\\img\\github.png'
    ing = 'C:\\Users\\hp\\Desktop\\start\\PyQt5\\img\\instagram.png'
    ex='C:\\Users\\hp\\Desktop\\start\\PyQt5\\img\\exit.png'
    buttons.but1.setIcon(QtGui.QIcon(xx));buttons.but2.setIcon(QtGui.QIcon(xx)); buttons.but3.setIcon(QtGui.QIcon(xx))
    buttons.but5.setIcon(QtGui.QIcon(tyg)),buttons.but4.setIcon(QtGui.QIcon(git)),buttons.but6.setIcon(QtGui.QIcon(ing))
    buttons.but7.setIcon(QtGui.QIcon(ex))

#run   and click connect buttons
class runed:
    buttons.but1.clicked.connect(proxyhttp)
    buttons.but2.clicked.connect(proxysocks4)
    buttons.but3.clicked.connect(proxysocks5)
    buttons.but5.clicked.connect(tg) ,buttons.but6.clicked.connect(ig),buttons.but4.clicked.connect(git)
    buttons.but7.clicked.connect(exit)
#show app
wd.show()
app.exec_()