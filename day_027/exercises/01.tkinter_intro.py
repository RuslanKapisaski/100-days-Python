import tkinter

def show_label_text(input_text):
        my_label.config(text=f"You've typed: {input_text}")

# Window
window = tkinter.Tk()
window.title("My first GUI application")
window.minsize(500, 300)

# Label
my_label = tkinter.Label(window, text="My first GUI application", font=("Arial", 25,"bold"))
my_label.pack()

# Entry
entry = tkinter.Entry(width=40)
entry.pack()

# Button
my_button = tkinter.Button(text="Click Me!", command=lambda: show_label_text(entry.get()))
my_button.pack()
window.mainloop()
my_button.pack()



window.mainloop()
