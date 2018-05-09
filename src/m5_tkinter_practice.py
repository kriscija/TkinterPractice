"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Joe Krisciunas.
"""  # Done

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # Done
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------
    root = tkinter.Tk()
    root.mainloop()
    # ------------------------------------------------------------------
    # Done
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------
    frame1 = ttk.Frame(root, padding=20)
    frame1.grid()
    # ------------------------------------------------------------------
    # Done
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------
    say_hello_button = ttk.Button(frame1, text = 'say hi')
    say_hello_button.grid()
    # ------------------------------------------------------------------
    # Done.
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------
    say_hello_button['command'] = lambda: print("Hello")
    # ------------------------------------------------------------------
    # Done
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------
    my_entry_box = ttk.Entry(frame1)
    my_entry_box.grid()

    say_hello_button = ttk.Button(frame1,text='Test for ok')
    say_hello_button['command'] = lambda: check_for_ok(my_entry_box)
    say_hello_button.grid()
    # ------------------------------------------------------------------
    # Done
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################
    my_entry_box2 = ttk.Entry(frame1)
    my_entry_box2.grid()

    say_hello_button = ttk.Button(frame1, text='string multiply')
    say_hello_button['command'] = lambda: stringmult(my_entry_box,my_entry_box2)
    say_hello_button.grid()
    # ------------------------------------------------------------------
    # TODO: 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------
    root.mainloop()

def print_hello():
    print("Hello")

def check_for_ok(entry_box):
    contents = entry_box.get()
    if contents == 'ok':
        print('Hello')
    else:
        print('goodbye')
def stringmult(entry_box,entry_box2):
    str1 = entry_box.get()
    str2 = entry_box2.get()
    n= int(str2)
    print(str1*n)



# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
