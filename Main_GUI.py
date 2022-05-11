# import all the required  modules
import json
import select
import socket
import threading

import chat_utils as cu
import tkinter as tk

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
        self.chat_window.minsize(
                                    width=600, 
                                    height=400)

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
    # TODO: play tic tac toe method

    def login(self, name):
        msg = json.dumps({"action": "login","name": name})
        self.my_msg = msg
        response = json.loads(self.recv())
        if response["status"] == "ok":
            self.state_machine.set_state(cu.S_LOGGEDIN)
            self.state_machine.set_myname(name)
            self.chat_box.config(state=NORMAL)
            self.chat_box.insert(END, menu + "\n\n")
            self.chat_box.config(state=DISABLED)
            self.chat_box.see(END)

        # the thread to receive messages
        process = threading.Thread(target=self.background_process)
        process.daemon = True
        process.start()
            

    # Utility Functions Taken from GUI.py for easier integration
    def send_msg(self):
        
        # store into my_msg property for data handling
        self.my_msg = self.input_field.get().strip()

        # clear the input field
        self.input_field.delete(0, tk.END)

        if self.my_msg:
            # Add the message to the chat box
            self.chat_box.config(state=tk.NORMAL)
            self.chat_box.insert(tk.END, self.my_msg + "\n")
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
                self.system_msg = self.state_machine.proc(self.my_msg, peer_msg)
                self.my_msg = ""
                self.chat_box.config(state=tk.NORMAL)
                self.chat_box.insert(tk.END, self.system_msg + "\n\n")
                self.chat_box.config(state=tk.DISABLED)
                self.chat_box.see(tk.END)
            
    # Call this to start GUI
    def run(self):
        name = "test1"
        msg = json.dumps({"action": "login","name": name})
        self.send(msg)
        print("waiting for server")
        response = json.loads(self.recv())
        print(response)
        if response["status"] == "ok":
            print("received ok")

            # activate state machine
            print("activating state machine")
            self.state_machine.set_state(cu.S_LOGGEDIN)
            self.state_machine.set_myname(name)

            # initialize chat window
            print("initializing chat window")
            self.setup_chat_window()
            

            # print menu
            print("displaying menu")
            self.chat_box.config(state=tk.NORMAL)
            self.chat_box.insert(tk.END, cu.menu + "\n\n")
            self.chat_box.config(state=tk.DISABLED)
            self.chat_box.see(tk.END)

        print("starting process")
        # the thread to receive messages
        process = threading.Thread(target=self.background_process)
        process.daemon = True
        process.start()

        self.root.mainloop()
        

# Testint case (no send or receive functionalities)
if __name__ == "__main__":
    gui = Main_GUI(None, None, None, None)
    gui.run()