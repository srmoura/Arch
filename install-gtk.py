#!/usr/bin/env python
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import SrMoura, pacman, os


class Handler:
    def repo_install(self, *args):
        """Instalação do repositório SrMoura"""
        os.system('echo "MAKEFLAGS = \"-j{}\"">>/etc/makepkg.conf'.format(os.cpu_count() + 1))
        os.system('echo "{}" >>/etc/pacman.conf'.format(SrMoura.repo()))
        pacman.netInstallY('srmoura-keyring pkgdistcache')
        pacman.populate()
        pacman.updateDB()
        os.system('echo "\n[options]\n{}" >>/etc/pacman.conf'.format('XferCommand = /usr/bin/pkgdistcache-client %u %o'))

    def yaourt(self, *args):
        """Instalação do Yaourt"""
        pacman.netInstallY('yaourt')

    def onDestroy(self, *args):
        """Fecha as janelas"""
        Gtk.main_quit()

    def assistantEnd(self, *args):
        """Fim da execução"""
        self.onDestroy()


#    about_dialog.run()
#   about_dialog.hide()


#    def sys_info(self, *args):
#       show_output.get_buffer()
#        show_output.set_text(uname().node)


builder = Gtk.Builder()
builder.add_from_file("install.glade")
builder.connect_signals(Handler())

"""Janelas"""

window0 = builder.get_object("assistant")

"""Objetos"""

# about_dialog = builder.get_object("about_dialog")
# show_output = builder.get_object("show_output")

window0.show_all()

Gtk.main()
