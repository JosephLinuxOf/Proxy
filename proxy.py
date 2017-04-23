#!/bin/python
# -*- coding: utf-8 -*-

# Testador de proxys HTTP desenvolvido por Joe Linux, criador do RHC
# Dúvidas e sugestões entre em contato contato@tlbsecurity.com
# Cooperado por http://baseti.com.br

import sys, re, os, commands, urllib2, socket
import string
from termcolor import colored

# Limpar tela
os.system("clear")

# verificar componentes e instalar caso necessário
try:
    import requests
except:
    print colored("Os componentes necessários não foram encontrados.\n","cyan")
    print colored("Instalando componentes necessários...\n","red")
    os.system("apt-get update 1>/dev/null && apt-get -y install python-pip 1>/dev/null && pip install requests 1>/dev/null")

    # importar após instalação
    import requests
    os.system("clear")
    

# banner    
print colored\
("""
 ____            ____ _   _ _  __
|  _ \          / ___| | | | |/ /
| |_) |  ___   | |   | |_| | " / 
|  __/  |___|  | |___|  _  | . \ 
|_|             \____|_| |_|_|\_| V3
 

""", "green")                             
print colored("Desenvolvido por Joe Linux","red")
print colored("https://telegram.me/RedHatChannel","cyan")
print colored("Proxy Alive Checker - RHC","yellow")

#ajuda
print colored("------------------------------------------------","yellow")
print "Uso: python proxy.py"
print "Formado da lista - IP:PORTA"
print colored("------------------------------------------------", "yellow")

socket.setdefaulttimeout(5)
sys.tracebacklimit = 0

arquivo = raw_input("Nome da sua lista de proxys: ")
proxyList = open(arquivo,"r").readlines()


# ler lista de proxys

print len(proxyList) , "Proxys Carregados!"

if len > 20:
	print "O processo pode ser um pouco demorado..." 
	 
else:
	pass
	
print colored("------------------------------------------------","yellow")          
print "Não se preocupe, pois irei criar um arquivo"
print "com todos os proxys aprovados neste teste :)"
print colored("------------------------------------------------","yellow")  

def bad(pip):    
    try:        
        proxy_handler = urllib2.ProxyHandler({"http": pip})        
        opener = urllib2.build_opener(proxy_handler)
        opener.addheaders = [("User-agent", "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.6) Gecko/2009022111 Gentoo Firefox/3.0.6")]
        urllib2.install_opener(opener)        
        req=urllib2.Request("http://createssh.com/")
        sock=urllib2.urlopen(req)
    except urllib2.HTTPError, e:        
             return e.code
    except Exception:
             return 1

# gravar lista de proxys aprovados
output = open("Aprovados.txt", "w")        

for proxy in proxyList:
    if bad(proxy):
	pass
    else:
		output = open("Aprovados.txt", "a") 
		output.writelines(proxy)
		output.close()
		print colored("#Aprovado :D","green"), proxy
		
print colored("------------------------------------------------","yellow")  
print "Processo terminado!"
