from Tkinter import *
from site_fetch import *
from vulnerability import *
from __future__ import *

class Main_Window:
    def __init__(self, master):
        print "Starting program..."
        master.title("NetSecure")

        frame = Frame(master)
        frame.pack()

        self.url_label = Label(frame, text="Enter the URL to scan: ")
        self.url_label.pack()

        self.url_entry= Entry(frame)
        self.url_entry.pack()