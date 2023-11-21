import customtkinter

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")


class App:
    def __init__(self, master):
        self.master = master
        # self.master.attributes("-fullscreen", True) 
        # self.master.geometry("500x350")
        self.master.geometry("{0}x{1}+0+0".format(self.master.winfo_screenwidth(), self.master.winfo_screenheight()))
        self.master.configure(bg="blue")
        self.start()

    def clear_frame(self):
        for widget in self.master.winfo_children():
            widget.destroy()
    def start(self):
        self.clear_frame()
        self.frame = customtkinter.CTkFrame(master=self.master,fg_color=("#98DAFF", "white"))
        self.frame.pack(pady=0, padx=0, fill="both", expand=True)

        self.label = customtkinter.CTkLabel(master=self.frame, text="Insert Cart Image", font=("Roboto", 24))
        self.label.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)
        self.button = customtkinter.CTkButton(master=self.frame, height=50, width=350,text="START SHOPPING", corner_radius=100,text_color="black",font=("Roboto", 35),command=self.loginOp)
        self.button.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)
        self.button = customtkinter.CTkLabel(master=self.frame, text="IM.AI CART", font=("Roboto", 23,'bold'))
        self.button.place(relx=0.5, rely=0.87, anchor=customtkinter.CENTER)
        self.button = customtkinter.CTkLabel(master=self.frame, text="Powered By: Linoflap Tech", font=("Light", 20))
        self.button.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)
    # First step
    def loginOp(self):
        self.clear_frame()
        self.frame = customtkinter.CTkFrame(master=self.master,fg_color=("#98DAFF", "white"))
        self.frame.pack(pady=0, padx=0, fill="both", expand=True)
        self.back_button = customtkinter.CTkButton(master=self.frame, text="Back", font=("Roboto", 20),command=self.start)
        self.back_button.place(relx=0.1, rely=0.1, anchor=customtkinter.CENTER)
        self.label = customtkinter.CTkLabel(master=self.frame, text="WHAT KIND OF SHOPPER ARE YOU?", font=("Roboto", 24))
        self.label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=4)
        self.frame.rowconfigure(2, weight=1)
        self.member_button = customtkinter.CTkButton(master=self.frame, text="Supermarket \nMember", font=("Roboto", 40), command=self.member)
        self.member_button.grid(row=1, column=1, padx=100, pady=0, sticky="nsew")
        self.non_member_button = customtkinter.CTkButton(master=self.frame, text="Non-Member", font=("Roboto", 40), command=self.nonmember)
        self.non_member_button.grid(row=1, column=2, padx=100, pady=0, sticky="nsew")
        # Second Step
    def member(self):
        self.clear_frame()
        self.frame = customtkinter.CTkFrame(master=self.master,corner_radius=0,fg_color=("#98DAFF", "white"))
        self.frame.pack(pady=0, padx=0, fill="both", expand=True, side="left")
        
        # Second Custom Frame
        self.frame2 = customtkinter.CTkFrame(master=self.master,corner_radius=0,fg_color=("#98DAFF", "white"))
        self.frame2.pack(pady=0, padx=0, fill="both", expand=True, side="right")
        self.frame2.columnconfigure(0, weight=0)
        self.frame2.columnconfigure(1, weight=2)
        self.frame2.columnconfigure(2, weight=0)
        self.frame2.rowconfigure(0, weight=3)
        self.frame2.rowconfigure(1, weight=6)
        self.frame2.rowconfigure(3, weight=0)
        self.frame2.rowconfigure(4, weight=4)
        self.frame2.columnconfigure(0, weight=0)
        self.frame.columnconfigure(1, weight=2)
        self.frame.columnconfigure(2, weight=0)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=0)
        self.frame.rowconfigure(2, weight=0)
        self.frame.rowconfigure(3, weight=0)
        self.frame.rowconfigure(4, weight=0)
        self.frame.rowconfigure(5, weight=0)
        self.frame.rowconfigure(6, weight=0)
        self.frame.rowconfigure(7, weight=0)
        self.frame.rowconfigure(8, weight=4)
        
        self.back_button = customtkinter.CTkButton(master=self.frame, text="Back", font=("Roboto", 20),command=self.loginOp)
        self.back_button.place(relx=0.199, rely=0.1, anchor=customtkinter.CENTER)

        self.label1 = customtkinter.CTkLabel(master=self.frame, text="Welcome Shopper!", font=("Roboto", 35))
        self.label1.grid(row=1, column=1, padx=0, pady=(50,0), sticky="ns")

        self.label2 = customtkinter.CTkLabel(master=self.frame, text="Good to see you!", font=("Roboto", 20))
        self.label2.grid(row=2, column=1, padx=0, pady=(0,100), sticky="ns")

        self.label3 = customtkinter.CTkLabel(master=self.frame, text="E-mail:", font=("Roboto", 25))
        self.label3.grid(row=3, column=1, padx=100, pady=0, sticky="w")

        self.entry1 = customtkinter.CTkEntry(master=self.frame, width=350, font=("Roboto", 25))
        self.entry1.grid(row=4, column=1, padx=100, pady=(0, 50), sticky="nsew")

        self.label4 = customtkinter.CTkLabel(master=self.frame, text="Password:", font=("Roboto", 25))
        self.label4.grid(row=5, column=1, padx=100, pady=0, sticky="w")

        self.entry2 = customtkinter.CTkEntry(master=self.frame,width=350 , font=("Roboto", 25), show='*')
        self.entry2.grid(row=6, column=1, padx=100, pady=(0,70), sticky="nsew")

        self.login_button = customtkinter.CTkButton(master=self.frame, text="LOGIN", font=("Roboto", 25))
        self.login_button.grid(row=7, column=1, padx=100, pady=0, sticky="nsew")

        # ======== FRAME 2 ============
        self.QR = customtkinter.CTkLabel(master=self.frame2, text="QR CODE", font=("Roboto", 50))
        self.QR.grid( row=1,column=1, padx=100, pady=(0,0), sticky="nsew")

        self.QR1 = customtkinter.CTkLabel(master=self.frame2, text="Log in with QR Code", font=("Roboto", 35))
        self.QR1.grid( row=2,column=1, padx=100, pady=0, sticky="nsew")

        self.QR2 = customtkinter.CTkLabel(master=self.frame2, text="Scan this with the supermarket\n mobile app to log in instantly.", font=("Roboto", 18))
        self.QR2.grid( row=3,column=1, padx=100, pady=0, sticky="nsew")

    def nonmember(self):
        self.clear_frame()
        self.frame = customtkinter.CTkFrame(master=self.master,corner_radius=0,fg_color=("#98DAFF", "white"))
        self.frame.pack(pady=0, padx=0, fill="both", expand=True)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=2)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure(0, weight=0)
        self.frame.rowconfigure(1, weight=3)
        self.frame.rowconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=0)
        self.back_button = customtkinter.CTkButton(master=self.frame, text="Back", font=("Roboto", 20),command=self.loginOp)
        self.back_button.place(relx=0.1, rely=0.1, anchor=customtkinter.CENTER)
        self.box= customtkinter.CTkButton(master=self.frame, text="ㅤ", font=("Roboto", 25))
        self.box.grid(row=1, column=1, padx=0, pady=(100,5), sticky="nsew")

        self.proceed_button = customtkinter.CTkButton(master=self.frame, text="PROCEED", font=("Roboto", 25))
        self.proceed_button.grid(row=2, column=1, padx=100, pady=0, sticky="wen")



if __name__ == "__main__":
    root = customtkinter.CTk()
    app = App(root)
    root.mainloop()





