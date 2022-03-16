import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# root window
root = tk.Tk()
root.geometry("300x250")
# root.resizable(False, False)
root.title('Value Finder')
value = tk.StringVar()
# store email address and password



def clac_value(e):
     global value
    try:
        value = int(value_enrty.get())
    except Exception as e:
        print(e)

    x = value / 1.0825
    result = "%.2f" % x
    result_lable.config(text=result)




# Sign in frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)


# email
info_label = ttk.Label(signin, text="Enter Value")
info_label.pack(fill='x', expand=True)

value_enrty = ttk.Entry(signin, textvariable=value)
value_enrty.pack(fill='x', expand=True)
value_enrty.focus()

result_lable = ttk.Label(signin)
result_lable.pack(fill='x', expand=True)

value_enrty.bind('<Return>', clac_value)

# login button
submit_button = ttk.Button(signin, text="Find Value", command=clac_value)
submit_button.pack(fill='x', expand=True, pady=10)


root.mainloop()
