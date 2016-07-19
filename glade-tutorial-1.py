#!/usr/bin/env python

import gtk


class MyApp:
    def __init__(self):
        self.gladefile = "tutorial-1.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(self.gladefile)

        self.builder.connect_signals(self)

        self.window = self.builder.get_object("window1")
        self.window.show()

    def on_gtk_quit_activate(self, menuitem, data=None):
        print "quit from menu"
        gtk.main_quit()

    def on_window1_destroy(self, object, data=None):
        print "quit with cancel"
        gtk.main_quit()

if __name__=="__main__":
    main = MyApp()
    gtk.main()
