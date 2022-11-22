import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

rt = customtkinter.CTk()

rt.geometry("800x550")

def reg():
    print("Registered")

fr = customtkinter.CTkFrame(master=rt)
fr.pack(pady=30, padx=120, fill="both", expand=True)

label = customtkinter.CTkLabel(master=fr, width=120, height=32, text="Register System", text_font=("Roboto", 24))
label.pack(pady=12, padx=10)

firstname = customtkinter.CTkEntry(master=fr, width=240, height=32, placeholder_text="Full name")
firstname.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=fr, width=240, height=32, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=fr, width=240, height=32, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)



button = customtkinter.CTkButton(master=fr, width=240, height=32, text="Register", command=reg)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=fr, text="Remember me")
checkbox.pack(pady=12, padx=10)

rt.mainloop()