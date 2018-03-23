#!/usr/bin/env python
"Busca informações e atualizações no servidor SrMoura"
import requests, json, random, string
#import psutil

def forToken(token):
	"Busca informações do Servidor pelo token"
	url='https://srmoura.com.br/api/arch/t{}'
	data = requests.get(url.format(token)).json()
	return data

def forAll():
	"Busca informações genéricas do servidor"
	url='https://srmoura.com.br/api/arch/all'
	data=requests.get(url).json()
	return data

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def repo():
	return "[srmoura]\nServer = http://srmoura.com.br/repo/arch/\$arch\nSigLevel = PackageRequired\n"
def repoCK():
	return "[repo-ck]\nServer = http://repo-ck.com/\$arch"