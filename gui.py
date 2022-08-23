from tkinter import *
from tkinter import filedialog

from web3 import Web3


'''
    Gui class: [all the tkinter entry and buttons]
'''  
class Gui():
    def __init__(self):
        # window
        self.window = Tk()

        self.window.geometry("540x624")
        self.window.configure(bg = "#0c0c0c")
        self.window.iconbitmap("assets/Logo.ico")
        self.window.title("EtherChecker")

        # canvas and background
        self.background()

        # tkinter entry
        self.entry()

        # tkinter button
        self.button()

    # inserting background to the window
    def background(self):
        self.canvas = Canvas(
            self.window,
            bg = "#0c0c0c",
            height = 624,
            width = 540,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"assets/background.png")
        self.background = self.canvas.create_image(
            269.5, 312.0,
            image=self.background_img)

    # Entry method
    def entry(self):
        self.entry0_img = PhotoImage(file = f"assets/img_textBox0.png")
        self.entry0_bg = self.canvas.create_image(
            270.0, 168.0,
            image = self.entry0_img)

        self.entry0 = Entry(
            bd = 0,
            bg = "#252525",
            fg = "#FFFFFF",
            insertbackground = "#FFFFFF",
            highlightthickness = 0)

        self.entry0.place(
            x = 97.0, y = 145,
            width = 346.0,
            height = 44)

        self.entry1_img = PhotoImage(file = f"assets/img_textBox1.png")
        self.entry1_bg = self.canvas.create_image(
            319.0, 326.5,
            image = self.entry1_img)

        self.entry1 = Entry(
            bd = 0,
            bg = "#1f1f1f",
            fg = "#FFFFFF",
            insertbackground = "#FFFFFF",
            highlightthickness = 0)

        self.entry1.place(
            x = 197.0, y = 304,
            width = 244.0,
            height = 43)

        self.entry2_img = PhotoImage(file = f"assets/img_textBox2.png")
        self.entry2_bg = self.canvas.create_image(
            319.0, 496.5,
            image = self.entry2_img)

        self.entry2 = Entry(
            bd = 0,
            bg = "#1f1f1f",
            fg = "#FFFFFF",
            insertbackground = "#FFFFFF",
            highlightthickness = 0)

        self.entry2.place(
            x = 197.0, y = 474,
            width = 244.0,
            height = 43)


    # Button method
    def button(self):
        self.img0 = PhotoImage(file = f"assets/img0.png")
        self.b0 = Button(
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: current_block(self),
            relief = "flat")

        self.b0.place(
            x = 87, y = 218,
            width = 366,
            height = 47)

        self.img1 = PhotoImage(file = f"assets/img1.png")
        self.b1 = Button(
            image = self.img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: check_balance(self),
            relief = "flat")

        self.b1.place(
            x = 87, y = 388,
            width = 366,
            height = 47)


        def current_block(self):
            self.infura_url = "https://mainnet.infura.io/v3/418d0e67dd734fc486c3d99488c30fbf"
            self.w3 = Web3(Web3.HTTPProvider(self.infura_url))
            self.blocknumber = self.w3.eth.blockNumber
            self.entry1.insert(END, self.blocknumber)
            print(self.blocknumber)
            

        def check_balance(self):
            self.balance = self.w3.eth.get_balance(self.entry0.get())
            self.eth_balance = self.w3.fromWei(self.balance, 'ether')
            self.entry2.insert(END, self.eth_balance)
            print(self.balance)