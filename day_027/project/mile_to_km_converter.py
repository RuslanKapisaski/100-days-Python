from tkinter import *

# Window
window = Tk()
window.title("Mile to Km Converter")
window.geometry("300x150")
window.config(padx=10, pady=20)

# Entry
user_input = Entry(width=10)
user_input.grid(row=0, column=2)

# Labels
mile_label = Label(text="Miles")
mile_label.grid(row=0, column=3)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=3)

# Result label (empty initially)
result_label = Label(text="")
result_label.grid(row=1, column=2)

# Convert logic
def convert_to_km():
    miles = user_input.get()
    if not miles:  # handle empty input
        result_label.config(text="0")
        return
    try:
        miles = float(miles)
    except ValueError:
        result_label.config(text="Invalid input")
        return

    km = miles * 1.61
    result_label.config(text=f"{km:.2f}")

# Button
button = Button(text="Calculate", command=convert_to_km)
button.grid(row=2, column=2)

window.mainloop()