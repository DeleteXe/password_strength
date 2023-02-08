from tkinter import*
import math
from tkinter import messagebox
from password_strength import PasswordStats
import tkinter as tk

root = tk.Tk()
root.title("Password Strength")
root.geometry("500x500")
root.configure(bg="white")
# root.resizable(0,0)

menubar = Menu(root)
root.config(menu=menubar)

about_menu = Menu(menubar, tearoff=0)
about_menu.add_command(label="Exit", command=lambda: root.destroy())
about_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Created by: Rocel Cabaral"))
menubar.add_cascade(label="Help", menu=about_menu)


def checkup():
	if entry_box.get() == "":
		messagebox.showerror("Error", "Text field in empty")
	else:
		result = PasswordStats(entry_box.get())
		finalresult = result.strength()
		percent_label["text"]=str(math.ceil(finalresult *100)) + " %"

		if finalresult >= 0.66:
			text_label.config(text="Strong", bg="white", fg="#00ff40")
			print("Strong")
		elif finalresult > 0.10 and finalresult < 0.40:
			text_label.config(text="Average", bg="white", fg="#e6e600")
			print("Average")
		elif finalresult <= 0.10:
			text_label.config(text="Weak", bg="white", fg="red")
			print("Weak")


def delete():
	entry_box.delete(0, END)
	text_label.config(text="")
	percent_label.config(text="")

frame = tk.Frame(root, bg="white")
frame.pack(fill="both", expand=True)


title = Label(frame, text="Password Strength", font=("Courier", 30, "bold"), bg="white", fg="black", bd=0)
title.grid(row=1, column=0, ipadx=50, ipady=20)

enter_password = Label(frame, text="Enter your password: ", font=("Helvetica", 20, "normal",), bg="white", fg="black", bd=0)
enter_password.grid(row=2, column=0, pady=5)

entry_box = Entry(frame, width=40, bd=2, relief="sunken", font=("Normal", 10, "bold"), bg="white", fg="black")
entry_box.grid(row=3, column=0, pady=10, ipady=10)

percent_label = Label(frame, text="", font=("Normal", 20, "bold"), bg="white", fg="black", bd=0)
percent_label.grid(row=5, column=0, pady=3)

delete_button = Button(frame, text="Delete", relief="raised", font=("Normal", 10, "normal"), bg="white", fg="black", bd=1, command=delete)
delete_button.grid(row=6, column=0, ipadx=20, ipady=10)

check_button = Button(frame, text="Check", relief="raised", font=("Normal", 10, "normal"), bg="white", fg="black", bd=1, command=checkup	)
check_button.grid(row=7, column=0, ipadx=20, ipady=10, padx=100)

text_label = Label(frame, text="", font=("Normal", 20, "bold"), bg="white", fg="black", bd=0)
text_label.grid(row=8, column=0, pady=5)

root.bind("<Control-q>", lambda quit: root.destroy())

root.mainloop()