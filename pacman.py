#!/usr/bin/env python
#Pacote auxiliar ao pacman
import os
def netInstall(pkg):
    os.system('pacman -S {}'.format(pkg))
def netInstallY(pkg):
    os.system('pacman -S {} --noconfirm'.format(pkg))
def locInstall(pkg):
    os.system('pacman -U {}'.format(pkg))
def updateDB():
    os.system('pacman -Sy')
def upgrade():
    os.system('pacman -Syu')
def populate():
    os.system('pacman-key --populate')
def rmD(pkg):
    "Remove os pacotes e suas dependencias"
    os.system('pacman -Rs {} --noconfirm'.format(pkg))
def rm(pkg):
    "Remove os pacotes deixando as dependencias"
    os.system('pacman -R {} --noconfirm'.format(pkg))
def autoremove():
    "Remove os pacotes não mais usados"
    os.system('pacman -R $(pacman -Qdtq)')
def listautoremove():
    "Lista os pacotes não mais usados"
    os.system('pacman -Qdt')
def rmDn(pkg):
    "Pula as dependencias e Remove só o pacote principal"
    os.system('pacman -Rdd {} --noconfirm'.format(pkg))