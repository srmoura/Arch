#!/usr/bin/env python
"""Busca informações e atualizações no servidor SrMoura"""
import random
import string
# from sys import argv as arg
from configparser import ConfigParser
from urllib.parse import urlencode
from urllib.request import Request, urlopen

import requests

config = {'file': '/etc/srmoura.conf',  # Arquivo de configuração
          'api_url': 'https://',  # URL da API
          'repo': 'https://'  # Repositório
          }


# import psutil

def getToken():
    """Busca informações do Servidor pelo token"""
    url = 'https://srmoura.com.br/api/arch/t{}'
    data = requests.get(url.format(read_conf()['token'])).json()
    return data


def getAll():
    """Busca informações genéricas do servidor"""
    url = 'https://srmoura.com.br/api/arch/all'
    data = requests.get(url).json()
    return data


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def repo():
    return "[srmoura]\nServer = http://srmoura.com.br/repo/arch/\$arch\nSigLevel = PackageRequired\n"


def repoCK():
    return "[repo-ck]\nServer = http://repo-ck.com/\$arch"


def postSend(data=[], url='https://srmoura.com.br/api/arch/new_client'):
    """Envia post para o servidor"""
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()
    return json


def new_client(data):
    client = postSend(data)
    write_conf(client['token'])
    return True


def read_conf():
    conf = ConfigParser()
    conf.read(config['file'])
    return {
        'token': conf.get('srmoura', 'token')
    }


def write_conf(token):
    conf = ConfigParser()

    conf.read(config['file'])

    conf.add_section('srmoura')
    conf.set('srmoura', 'token', token)
    conf.set('srmoura', 'repo', config['repo'])

    with open(config['file'], 'w') as confFile:
        conf.write(confFile)
    return True

# def main():
#    if arg == None:
#        print("""Uso: SrMoura [OPÇÔES]
#            - u
#        """)
#    elif arg == '-u':
#        print()
#    else:
#        print()
