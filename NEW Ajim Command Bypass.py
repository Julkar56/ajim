# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-05-09 21:58:33.548178


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)

logo2 = """
                 .88888888:.
                88888888.88888.
              .8888888888888888.
              888888888888888888
              88' _`88'_  `88888
              88 88 88 88  88888
              88_88_::_88_:88888
              88:::,::,:::::8888
              88`:::::::::'`8888
             .88  `::::'    8:88.
            8888            `8:888.
          .8888'             `888888.
         .8888:..  .::.  ...:'8888888:.
        .8888.'     :'     `'::`88:88888
       .8888        '         `.888:8888.
      888:8         .           888:88888
    .888:88        .:           888:88888:
    8888888.       ::           88:888888
    `.::.888.      ::          .88888888
   .::::::.888.    ::         :::`8888'.:.
  ::::::::::.888   '         .::::::::::::
  ::::::::::::.8    '      .:8::::::::::::.
 .::::::::::::::.        .:888:::::::::::::
 :::::::::::::::88:.__..:88888:::::::::::'
  `'.:::::::::::88888888888.88:::::::::'
        `':::_:' -- '' -'-' `':_::::'`

---------------------------------------------
\033[1;96m|-------+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-----|
\033[1;96m|               Pak Anonymous               |
\033[1;96m|This Tool is Only for Bangladesh FB Acounts|
\033[1;96m|------+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+------|

\033[1;91m [⚡\033[1;97mAuthor Name: Babar Ali     ⚡\033[1;91m]
\033[1;91m [⚡\033[1;97mYutube Chnl: Pak Anonymous ⚡\033[1;91m]
\033[1;91m [⚡       \033[1;97mFrom: Pakistan      ⚡\033[1;91m]
\033[1;95m«-_-_-_-_-_-_-_-_-\033[1;91mHuntter\033[1;95m-_-_-_-_-_-_-_-_-»
"""
os.system("clear")

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(0.1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")






import os
import sys
import time
import datetime
import re
import threading
import json
import random
import requests
import hashlib
import cookielib
import uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError

os.system('git pull')
os.system('clear')
class colores:
    red="\033[31;1m"
    verde="\033[92m"
    azul="\033[94m"

os.system("clear")
color_random=[colores.red,colores.verde,colores.azul]
random.shuffle(color_random)

logo2 = color_random[0] +"""
 \033[10;34m 
 █████╗      ██╗██╗███╗   ███╗    ██╗   ██╗ █████╗ ██╗   ██╗
██╔══██╗     ██║██║████╗ ████║    ██║   ██║██╔══██╗██║   ██║
███████║     ██║██║██╔████╔██║    ██║   ██║███████║██║   ██║
██╔══██║██   ██║██║██║╚██╔╝██║    ╚██╗ ██╔╝██╔══██║██║   ██║
██║  ██║╚█████╔╝██║██║ ╚═╝ ██║     ╚████╔╝ ██║  ██║╚██████╔╝
╚═╝  ╚═╝ ╚════╝ ╚═╝╚═╝     ╚═╝      ╚═══╝  ╚═╝  ╚═╝ ╚═════╝ 
                                                            
        
       \033[10;31m        ░▒▓██████████►╬◄██████████▓▒░
               ░▒▓██►╔╦╦╦═╦╗╔═╦═╦══╦═╗◄██▓▒░
               ░▒▓██►║║║║╩╣╚╣═╣║║║║║╩╣◄██▓▒░
               ░▒▓██►╚══╩═╩═╩═╩═╩╩╩╩═╝◄██▓▒░
               ░▒▓██████████►╬◄██████████▓▒░

                                       """
logo = """
\033[10;34m 
 █████╗      ██╗██╗███╗   ███╗    ██╗   ██╗ █████╗ ██╗   ██╗
██╔══██╗     ██║██║████╗ ████║    ██║   ██║██╔══██╗██║   ██║
███████║     ██║██║██╔████╔██║    ██║   ██║███████║██║   ██║
██╔══██║██   ██║██║██║╚██╔╝██║    ╚██╗ ██╔╝██╔══██║██║   ██║
██║  ██║╚█████╔╝██║██║ ╚═╝ ██║     ╚████╔╝ ██║  ██║╚██████╔╝
╚═╝  ╚═╝ ╚════╝ ╚═╝╚═╝     ╚═╝      ╚═══╝  ╚═╝  ╚═╝ ╚═════╝ 
                                                            
        
       """

def reg():
    os.system("clear")
    
    
    print ''
    print '\x1b[1;32;1m W E L C O M    ....!'
    print ''
    time.sleep(0)
    
    try:
        to = open('/sdcard/.RANAMZnamtusunahuga.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://github.com/ajim-vau/appruved/blob/main/id.txt').text
    if to in r:
        ip()
    else:
        os.system('clear')
        print logo
        print '\tN O T       A P P R O U V E D ....!'
        print '+=========================================+ '
        print """+=========================================+ 

your I'd sent from ajim vau



"""
        print ' \x1b[1;97m Y O U R    ID NAMBER : ' + to
        raw_input("""
        
\x1b[1;92m    PRESS  E N T E R    """)
        os.system('xdg-open https://www.facebook.com/profile.php?id=100007273636301')
    reg()


def reg2():
    os.system('clear')
    print logo2
    
    print ' \033[10;32m ╔══●➤\033[1;30m[\033[1;32m■-\033[10;31m1\033[1;30m]\033[1;37mTHIS IS TOOL IS PAID\033[10;30m[\033[20;31mNOT FREE\033[10;30m]    '
    
    print ' \033[10;32m ╠══●➤\033[1;30m[\033[1;32m■-\033[10;31m2\033[1;30m]\033[1;96m\x1b[5;37mTHIS TOOL FOR \033[10;30m[\033[20;32m!!!!\033[10;30m]  ' 
    print ' \033[10;32m ║ '
    
    id = uuid.uuid4().hex[:30]
    print ' \033[10;32m ╚══●➤\033[1;30m[\033[1;32m■\033[1;30m]\033[20;37mYOUR\033[1;37m TOOL ID::  \033[1;32m' + id

    raw_input("""   """)
         
    os.system('xdg-open https://www.facebook.com/RanaMZ.zeshi')
    sav = open('/sdcard/.RANAMZnamtusunahuga.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;97m   E N T E R ')
    reg()


def ip():
    os.system('clear')
    print logo
    
    
    try:
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        ips = z['query']
        country = z['country']
        regi = z['regionName']
        network = z['isp']
    except:
        pass

    
    print '\033[1;32m ╠══●➤\033[1;30m[\033[1;32m■-\033[10;31m2\033[1;30m]\033[1;96m\x1b[5;37myour ip\033[10;32m  : ' + ips
    time.sleep(1)
    print '\033[1;32m ╠══●➤\033[1;30m[\033[1;32m■-\033[10;31m3\033[1;30m]\033[1;96m\x1b[5;37m your country: ' + country
    time.sleep(1)
    print '\033[1;32m ╠══●➤\033[1;30m[\033[1;32m■-\033[10;31m3\033[1;30m]\033[1;96m\x1b[5;37mlocetion: ' + regi
    time.sleep(1)
    print """\033[1;32m ╚══●➤\033[1;30m[\033[1;32m■\033[1;30m]\033[20;37mDark\033[1;37m network: : """ + network
    print """ 
     (1) start cloning """
    menu_s()
 

def menu_s():
    ms = raw_input("""

\x1b[1;97m Cross 1 :  """)
    if ms == '1':
    	os.system('clear')
        
    elif ms == '':
        print '\x1b[1;32m  ONER IZ RANA-MZ'
        os.system('xdg-open https://wa.me/+923219033282')
    else:
        print ''
        print '\tNot Jaani'
        print ''
        menu_s()

if __name__ == '__main__':
    reg()

