"""
Author: Philipp Mergener
file: Main_GUI.py
"""
# import all the required  modules
import json
import select
import socket
import threading
import random

import chat_utils as cu
import tkinter as tk

from encrypt import Encrypt
from emojis import Emoji
class Spacer(tk.Label):
    def __init__(self, master):
        tk.Label.__init__(self, master, text="")

class Main_GUI:

    ### Class Initialization ###

    # Adapted version from GUI.py
    def __init__(self, send, recv, sm, s):
        # necessary messaging properties
        self.send = send
        self.recv = recv
        self.state_machine = sm
        self.socket = s
        self.my_msg = ""
        self.system_msg = ""

        # GUI variables
        self.e_build = Emoji()
        self.input_message: str = ""
        self.font_name = "Comic Sans MS"
        self.font_size = 1

        # initiate the root tcl object for GUI
        self.root = tk.Tk()
        self.root.withdraw()
        
        

    ### UI Elements Setup Methods ###
    # TODO: Design cleaner layout 
    # TODO: Scrolling implementation
    # TODO: Sidebar of group

    def launch_login_window():
        self.login_window = tk.Toplevel()
        self.login_window.title("PyChat - Login")
        self.login_window.resizable(width=False,
                               height=False)
        self.login_window.configure(width=800, 
                                    height=500)
        self.login_title = tk.Label(text="Welcome to PyChat \n \
                                        please enter your username")
        self.user_name_input = tk.Entry()
        self.login_btn = tk.Button(text="Login", 
                                   command = self.login(self.user_name_input.get()))
        
         
    # New window for the group chat
    def setup_chat_window(self):
        self.chat_window = tk.Toplevel(self.root)
        self.chat_window.title("PyChat")
        self.chat_window.resizable(
                                    width=False,
                                    height=False)
        self.chat_window.configure(
                                    width=800, 
                                    height=800)

        self.setup_chat_box()
        self.setup_input_bar()
        
    
    # Widget for displaying chat text
    def setup_chat_box(self):
        self.chat_box = tk.Text(self.chat_window,
                                font=(self.font_name, 12 * self.font_size), 
                                state=tk.DISABLED)
        self.chat_box.grid(row=0, columnspan=3, sticky=tk.NSEW)
        
    # Widget for user chat input
    def setup_input_bar(self):
        self.setup_input_field()
        self.setup_input_spacer()
        self.setup_send_button()

    # Widget for user input field
    def setup_input_field(self):
        self.input_field = tk.Entry(self.chat_window)
        self.input_field.grid(row=1, column=0, sticky=tk.NSEW)
        self.input_field.bind("<Return>", lambda *args: self.send_msg())
    
    # Widget to space input field and send button
    # Not for use
    def setup_input_spacer(self):
        self.input_spacer = Spacer(self.chat_window) 
        self.input_spacer.grid(row=1, column=1, sticky=tk.NSEW)

    # Widget for send button
    def setup_send_button(self):
        # Calls send function when enter is pressed
        self.send_btn = tk.Button(self.chat_window,
                                  text="Send", 
                                  command=lambda: self.send_msg())
        self.send_btn.grid(row=1, column=3, sticky=tk.NSEW)
        self.send_btn.bind("<Return>", lambda *args: self.send_msg())
    
    ### Action Methods ###
    # TODO: integrate send and receive methods for client class

    # Utility Functions Taken from GUI.py for easier integration
    def send_msg(self):
        commands = ["!time", "!who", "!c", "!?", "!p", "!q", "!emoji", "!help"]
        # store into my_msg property for data handling
        plain_text = self.input_field.get().strip()
        self.input_field.delete(0, tk.END)
        if plain_text: 
            if plain_text[0] == '!':
                self.post_to_chat_box(plain_text)
                words = plain_text.split()
                if words[0] in commands:
                    if words[0] == "!help":
                        self.post_to_chat_box(cu.menu)
                    elif words[0] == "!emoji":
                        emoji_menu = "\nEmoji Shortcuts: \n" + "\n ".join([f" {k}  -->  {v}" for k,v in self.e_build.shortcuts.items()]) + "\n"
                        self.post_to_chat_box(emoji_menu)
                    else:
                        self.my_msg = plain_text[1:]
                else:
                    invalid_command = "Command not recognized \n \
                                type !help for command menu"
                    self.post_to_chat_box(invalid_command)
            else:
                if self.state_machine.state != cu.S_CHATTING:
                    self.post_to_chat_box(plain_text)
                    self.post_to_chat_box("Please enter a valid command to start chatting")
                else:
                    encrypted, key = Encrypt.encrypt_message(plain_text)        
                    message = "$" + encrypted + key
                    self.my_msg = message
                    emoji_message = self.e_build.emojify_msg(plain_text)
                    # Add the message to the chat box
                    self.post_to_chat_box(emoji_message)

    def post_to_chat_box(self, msg):
        self.chat_box.config(state=tk.NORMAL)
        self.chat_box.insert(tk.END, msg)
        self.chat_box.config(state=tk.DISABLED)
        self.chat_box.see(tk.END)

    # Daemon task for receiving messages and adding them to the screen
    def background_process(self):
        while True:
            read, write, error = select.select([self.socket], [], [], 0)
            peer_msg = []
            if self.socket in read:
                peer_msg = self.recv()
            if len(self.my_msg) > 0 or len(peer_msg) > 0:
                if peer_msg:
                    decoded = json.loads(peer_msg)
                    try:
                        message = decoded['message']
                        message = Encrypt.decrypt_message(message[1:-3], message[-3:])
                        decoded['message'] = self.e_build.emojify_msg(message)
                        peer_msg = json.dumps(decoded)
                    except KeyError:
                        pass
                self.system_msg = self.state_machine.proc(self.my_msg, peer_msg)
                self.my_msg = ""
                self.post_to_chat_box(self.system_msg)
            

    def login(self, name):
        msg = json.dumps({"action": "login","name": name})
        self.send(msg)
        response = json.loads(self.recv())
        if response["status"] == "ok":
            # activate state machine
            self.state_machine.set_state(cu.S_LOGGEDIN)
            self.state_machine.set_myname(name)

            # initialize chat window
            self.setup_chat_window()
            
            # print menu
            self.post_to_chat_box(cu.menu)
            
        # the thread to receive messages
        process = threading.Thread(target=self.background_process)
        process.daemon = True
        process.start()

        self.root.mainloop()
    
    # Call this to start GUI
    def run(self):
        name = f"test{random.randint(0, 10)}"
        self.login(name)
                

# Testint case (no send or receive functionalities)
if __name__ == "__main__":
    gui = Main_GUI(None, None, None, None)
    gui.run()