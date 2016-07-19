#!/usr/bin/env python

from gi.repository import Gtk


class Handler:
    def btnHello_clicked_cb(self, button):
        print "Hello, world!"

    def btnQuit_clicked_cb(self, button):
        print "quit button pressed"
        Gtk.main_quit()

    def onDeleteWindow(self, *args):
        Gtk.main_quit(args)

    def MainWindow_destroy_cb(self, *args):
        Gtk.main_quit()

builder = Gtk.Builder()
builder.add_from_file("sample.glade")
builder.connect_signals(Handler())

window = builder.get_object("MainWindow")
window.show_all()

Gtk.main()
