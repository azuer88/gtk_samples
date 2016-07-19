#!/usr/bin/env python

import gtk

from gtk.gdk import pointer_grab, pointer_ungrab, keyboard_grab, keyboard_ungrab


class Window:
    def __init__(self):
        self.locked = False
        self.window = gtk.Window()
        self.window.set_title("Window Example")

        self.window.connect("destroy", self.destroy)

        box = gtk.VBox()
        self.button = gtk.Button("Lock")

        self.button.connect("clicked", self.button_clicked)

        box.pack_start(self.button)

        box.pack_start(gtk.Entry())

        self.window.add(box)

    def destroy(self, widget):
        self.unlock()
        gtk.main_quit()

    def button_clicked(self, widget):
        if self.locked:
            self.button.set_label("unlock")
            self.lock()
        else:
            self.button.set_label("lock")
            self.unlock()
        self.locked = not self.locked
        print "button clicked"

    def show(self):
        self.window.show_all()

    def lock(self):
        pointer_grab(self.window.window, True)
        keyboard_grab(self.window.window, True)

    def unlock(self):
        pointer_ungrab()
        keyboard_ungrab()


Window().show()

gtk.main()
