# import all the required  modules
import json
import select
import threading

import tkinter as tk
from tkinter import font
from tkinter import ttk

import chat_utils as cu

class Main_GUI:
    def __init__(self, send, recv, sm, s):
        self.root = tk.Tk()
        self.root.withdraw()
        
        self.setup_chat_window()
        self.setup_chat_box()
        self.init_send_btn()

        self.send = send
        self.recv = recv
        self.sm = sm
        self.socket = s

        self.my_msg = ""
        self.system_msg = ""

    def setup_chat_window(self):
        self.chat_window = tk.Toplevel(self.root)
        w = self.chat_window  
        w.title("PyChat")
        w.geometry("800x600")
        w.resizable(width=True,
                    height=True)
        w.minsize(width=600, height=400)
    
    def setup_chat_box(self):
        self.chat_box = tk.Label(self.chat_window)
        self.chat_box.grid()
        
    def init_send_btn(self):
        self.send_btn = tk.Button(self.chat_window,
                                  text="Send", 
                                  anchor="se")
        self.send_btn.grid()
        
    def present_chat_window(self):
        self.chat_window.update()
        self.chat_window.deiconify()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = Main_GUI(None, None, None, None)
    gui.run()
        

