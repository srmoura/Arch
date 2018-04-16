#!/usr/bin/env python
# Pacote auxiliar ao pacman
from os import system


def netInstall(pkg):
    system('pacman -S {}'.format(pkg))


def netInstallY(pkg):
    system('pacman -S {} --noconfirm'.format(pkg))


def locInstall(pkg):
    system('pacman -U {}'.format(pkg))


def updateDB():
    system('pacman -Sy')


def upgrade():
    system('pacman -Syu')


def populate():
    system('pacman-key --populate')


def rmD(pkg):
    """Remove os pacotes e suas dependencias"""
    system('pacman -Rs {} --noconfirm'.format(pkg))


def rm(pkg):
    """Remove os pacotes deixando as dependencias"""
    system('pacman -R {} --noconfirm'.format(pkg))


def autoremove():
    """Remove os pacotes não mais usados"""
    system('pacman -R $(pacman -Qdtq)')


def listautoremove():
    """Lista os pacotes não mais usados"""
    system('pacman -Qdt')


def rmDn(pkg):
    """Pula as dependencias e Remove só o pacote principal"""
    system('pacman -Rdd {} --noconfirm'.format(pkg))


def listRepo(repo):
    """Lista os pacotes do repositório"""
    system('pacman -Sl {}'.format(repo))


def info(pkg):
    """Imprime as informações do pacote"""
    system('pacman -Si {}'.format(pkg))


def rmU():
    """Remove os pacotes que não são mais necessários"""
    system('pacman -Rns $(pacman -Qtdq)')


def down(pkg):
    """Faz download dos pacotes sem instalar-los"""
    system('pacman -Sw {}',format(pkg))


def optimize():
    """Melhora a performace do pacman"""
    system('pacman-optimize')