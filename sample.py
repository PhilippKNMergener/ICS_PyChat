# import all the required  modules
import json
import select
import threading

import tkinter as tk
import chat_utils as cu

class Main_GUI:

    ### Class Initialization ###

    # Adapted version from GUI.py
    def __init__(self, send, recv, sm, s):

        # GUI variables
        self.input_message: str = ""
        self.font_name = "Comic Sans MS"
        self.font_size = 1

        # initiate the root tcl object for GUI
        self.root = tk.Tk()
        self.root.withdraw()
        
        # setup chat window views
        self.setup_chat_window()
        
        # necessary messaging properties
        self.send = send
        self.recv = recv
        self.sm = sm
        self.socket = s
        self.my_msg = ""
        self.system_msg = ""

    ### UI Elements Setup Methods ###

    def setup_chat_window(self):
        # New window for the group chat
        self.chat_window = tk.Toplevel(self.root)
        self.chat_window.resizable(
                                    width=True,
                                    height=True)
        self.chat_window.configure(
                                    width=800, 
                                    height=800)
        self.chat_window.minsize(width=600, height=400)

        self.setup_chat_box()
        self.setup_input_field()
        self.setup_send_button()
    
    def setup_chat_box(self):
        self.chat_box = tk.Text(self.chat_window,
                                font=(self.font_name, 12 * self.font_size))
        self.chat_box.grid()
        
    
    def setup_input_field(self):
        self.input_field = tk.Entry(self.chat_window)
        self.input_field.insert(0, "Input Field Placeholder")
        self.input_field.grid()
    
    def setup_send_button(self):
        self.send_btn = tk.Button(self.chat_window,
                                  text="Send Button Placeholder", 
                                  command=lambda: self.send_msg(self.input_field.get()))
        self.send_btn.grid()
    
        
    ### Action Methods ###

    def present_chat_window(self):
        self.chat_window.update()
        self.chat_window.deiconify()
    
    # Utility Functions Taken from GUI.py for easier integration
    def send_msg(self, msg):
        self.my_msg = msg
        self.input_field.delete(0, tk.END)
        self.chat_box.config(state=tk.NORMAL)
        self.chat_box.insert(tk.END, msg + "\n")
        self.chat_box.config(state=tk.DISABLED)
        self.chat_box.see(tk.END)

    def background_process(self):
        while True:
            read, write, error = select.select([self.socket], [], [], 0)
            peer_msg = []
            if self.socket in read:
                peer_msg = self.recv()
            if len(self.my_msg) > 0 or len(peer_msg) > 0:
                self.system_msg = self.sm.proc(self.my_msg, peer_msg)
                self.my_msg = ""
                self.textCons.config(state=NORMAL)
                self.textCons.insert(END, self.system_msg + "\n\n")
                self.textCons.config(state=DISABLED)
                self.textCons.see(END)
            
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = Main_GUI(None, None, None, None)
    gui.run()
        

