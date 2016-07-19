#!/usr/bin/env python

import gtk


class HelloWorld:
    def __init__(self):
        window = gtk.Window()
        window.set_type_hint(gtk.gdk.WINDOW_TYPE_HINT_DESKTOP)
        button = gtk.Button("Click Here")

        window.connect("destroy", self.close)
        window.connect("key-press-event", self.key_press_event)
        # button.connect("clicked", self.print_hello_world)
        button.connect("clicked", self.close)

        window.add(button)
        window.set_modal(True)
        window.set_keep_above(True)

        window.fullscreen()
        window.show_all()

    def key_press_event(self, widget, event):
        if event.string == "q":
            gtk.main_quit()
        elif event.string == "f":
            widget.window.unfullscreen()

    def close(self, widget):
        gtk.main_quit()

    def print_hello_world(self, widget):
        print "Hello World"

HelloWorld()
gtk.main()
