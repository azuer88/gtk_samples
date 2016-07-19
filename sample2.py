#!/usr/bin/env python

import gtk


class HelloWorld:
    def __init__(self):
        window = gtk.Window()

        button = gtk.Button("Click Me")

        window.connect("destroy", lambda q: gtk.main_quit())
        button.connect("clicked", self.print_hello_world)

        window.add(button)
        window.show_all()

    def print_hello_world(self, widget):
        print "Hello World - from {}".format(widget.name)


if __name__ == "__main__":
    HelloWorld()
    gtk.main()
