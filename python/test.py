import tkinter as tk

window = tk.Tk()
ratioList = ('1 : 1', '16 : 9')
variable = tk.StringVar()
variable.set(ratioList[0])

ratioDropdown = tk.OptionMenu(window, variable, *ratioList)
ratioDropdown.place(x=170, y=155)
ratioDropdown.config(relief="flat", highlightthickness=0, font=("Montserrat", (12)), bg="#035be3", activebackground="#023c96",activeforeground="white", fg="white", borderwidth="0", indicatoron=0)

ratioDropdown["menu"].config(font=("Montserrat", (12)), bg="#035be3", relief="flat", fg="white", activebackground="#023c96", borderwidth=0)

ratioDropdown.pack()

tk.mainloop()