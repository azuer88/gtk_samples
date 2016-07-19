#!/usr/bin/env python

import gtk


class HelloWorld:
    def __init__(self):
        window = gtk.Window()
        button = gtk.Button("Click Here")

        window.connect("destroy", self.close)
        button.connect("clicked", self.print_hello_world)

        window.add(button)
        window.show_all()

    def close(self, widget):
        gtk.main_quit()

    def print_hello_world(self, widget):
        print "Hello World"

HelloWorld()
gtk.main()
