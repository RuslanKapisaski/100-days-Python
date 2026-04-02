import tkinter


def show_label_text(input_text):
        my_label.config(text=f"You've typed: {input_text}")

# Window
window = tkinter.Tk()
window.title("My first GUI application")
window.minsize(500, 300)
window.config(padx=100, pady=100)

# Label
my_label = tkinter.Label(window, text="My first GUI application", font=("Arial", 25,"bold"))
my_label.grid(row=0,column=0)

# Button
my_button1 = tkinter.Button(text="Click Me!", command=lambda: show_label_text(entry.get()))
my_button1.grid(row=1, column=1)

# Button
my_button2 = tkinter.Button(text="My Button", command=lambda: show_label_text(entry.get()))
my_button2.grid(row=0, column=2)

# Entry
entry = tkinter.Entry(width=40)
entry.grid(row=2, column=3)

window.mainloop()