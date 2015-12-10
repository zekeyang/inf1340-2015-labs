#!/usr/bin/env python3

""" GUI for Name that Shape """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from name_that_shape import *

import Tkinter
import tkMessageBox

"""
   Create a GUI for the Name That Shape program
   See name_shape_gui.png for specification
   Use the name_that_shape.py to perform computations
   For inputs that raise an error, pop up a modal dialog box
   For inputs that produce a shape name, display the string in the window
"""


class NameThatShapeGUI:

    def __init__(self):
        # Create the main window widget
        self.main_window = Tkinter.Tk()
        self.main_window.geometry('500x100')

        # Create two frames to group widgets
        self.top_frame = Tkinter.Frame(self.main_window)
        self.middle_frame = Tkinter.Frame(self.main_window)
        self.bottom_frame = Tkinter.Frame(self.main_window)

        # Create widgets for the top frame
        self.prompt_label = Tkinter.Label(self.top_frame,
                                          text="Enter the number of sides in the shape:")
        self.side_entry = Tkinter.Entry(self.top_frame, width=10)

        # Pack the top frame's widgets
        self.prompt_label.pack(side="left")
        self.side_entry.pack(side="left")

        # Create widgets for the middle frame
        self.descr_label = Tkinter.Label(self.middle_frame, text="Name of shape:")
        self.value = Tkinter.StringVar()
        self.value.set("")
        self.shape_name = Tkinter.Label(self.middle_frame, textvariable=self.value)

        # Pack the middle frame's widgets
        self.descr_label.pack(side="left")
        self.shape_name.pack(side="left")

        # Create widgets for bottom frame
        self.conv_button = Tkinter.Button(self.bottom_frame,
                                          text="Name",
                                          command=self.convert)

        self.quit_button = Tkinter.Button(self.bottom_frame,
                                          text="Quit",
                                          command=self.main_window.destroy)

        # Pack the bottom buttons
        self.conv_button.pack(side="left")
        self.quit_button.pack(side="left")

        # Pack the frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        # Enter the Tkinter main loop
        Tkinter.mainloop()

    def convert(self):
        # Display and info dialog box
        # self.value.set(self.side_entry.get())
        try:
            self.value.set(name_that_shape(self.side_entry.get()))
        except:
            #tkMessageBox.showinfo("Response", self.side_entry.get())
            self.value.set("")
            tkMessageBox.showinfo("Response", "error")


# Instantiating the object
ntsg = NameThatShapeGUI()
