import customtkinter

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")


class App:
    def __init__(self, master):
        self.master = master
        # self.master.attributes("-fullscreen", True) 
        # self.master.geometry("500x350")
        self.master.geometry("{0}x{1}+0+0".format(self.master.winfo_screenwidth(), self.master.winfo_screenheight()))
        self.start()

    def clear_frame(self):
        for widget in self.master.winfo_children():
            widget.destroy()
    def start(self):
        self.clear_frame()
        self.frame = customtkinter.CTkFrame(master=self.master)
        self.frame.pack(pady=0, padx=0, fill="both", expand=True)

        self.label = customtkinter.CTkLabel(master=self.frame, text="Tutorial", font=("Roboto", 20))
        self.label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)


        self.previous_button = customtkinter.CTkButton(master=self.frame, text="Previous", font=("Roboto", 20))
        self.previous_button.place(relx=0.4, rely=0.8, anchor=customtkinter.CENTER)

        self.previous_button = customtkinter.CTkButton(master=self.frame, text="Previous", font=("Roboto", 20))
        self.previous_button.place(relx=0.4, rely=0.8, anchor=customtkinter.CENTER)

        self.Next_button = customtkinter.CTkButton(master=self.frame, text="Next", font=("Roboto", 20))
        self.Next_button.place(relx=0.6, rely=0.8, anchor=customtkinter.CENTER)

   


if __name__ == "__main__":
    root = customtkinter.CTk()
    app = App(root)
    root.mainloop()





