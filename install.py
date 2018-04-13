#!/usr/bin/env python
# Intalação de otimizações SrMoura para Arch-Linux Based

import SrMoura, pacman, os

token = SrMoura.id_generator(64)
print('O token da atualização é: \n {}\n\n'.format(token))

pkgdistcache = 'XferCommand = /usr/bin/pkgdistcache-client %u %o'  # SrMoura.forAll()['pkgdistcache']

print('Setando configurações\n\n')

os.system('echo "MAKEFLAGS = "-j{}"">>/etc/makepkg.conf'.format(os.cpu_count() + 1))
os.system('echo "{}" >>/etc/pacman.conf'.format(SrMoura.repo()))

print('Instalando dependencias\n\n')
pacman.netInstallY('srmoura-keyring pkgdistcache')
pacman.populate()
pacman.updateDB()
os.system('echo "\n[options]\n{}" >>/etc/pacman.conf'.format(pkgdistcache))

Q0 = input('Deseja otimizar para desktop[s,n]?: ')
if Q0 == 's':
    dk='vm.swappiness=1\nvm.vfs_cache_pressure = 50\nvm.dirty_background_bytes = 16777216\nvm.dirty_bytes = 50331648'
    os.system('echo "{}" >>/etc/sysctl.conf'.format(dk))
    os.system('echo "{}" >/etc/sysctl.d/99-sysctl.conf'.format(dk))
    
Q1 = input('Deseja instalar o yaourt[s,n]?: ')
if Q1 == 's':
    pacman.netInstallY('yaourt')

Q2 = input('Deseja instalar o pamac-manager[s,n]?: ')
if Q2 == 's':
    pacman.netInstallY('pamac-manager')

Q3 = input('Deseja instalar o qtpacman[s,n]?: ')
if Q3 == 's':
    pacman.netInstallY('qtpacman')

Qck = input('Deseja instalar o kernel-ck[s,n]?: ')
if Qck == 's':
    print('Configurando repositório, chaves e instalando o linux-ck')
    os.system('gcc -c -Q -march=native --help=target | grep march')
    os.system('echo "{}" >>/etc/pacman.conf'.format(SrMoura.repoCK()))
    os.system('pacman-key -r 5EE46C4C && pacman-key --sign-key 5EE46C4C')
    pacman.populate()
    pacman.updateDB()
    ckv = input('Digite o nome printado: ')
    pacman.netInstallY('linux-ck-{} linux-ck-{}-headers'.format(ckv))

print ('Fim das configurações')
