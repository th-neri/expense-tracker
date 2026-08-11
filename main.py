import tkinter as tk
from tkinter import messagebox


def add_expense():
    description = description_entry.get()
    amount = amount_entry.get()

    if description == "":
        messagebox.showerror(
            "Invalid description.",
            "Please enter a valid description."
        )
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror(
            "Invalid amount.",
            "Please enter valid number(s)."
        )
        return

    if amount <= 0:
        messagebox.showerror(
            "Invalid amount.",
            "Amount must be greater than 0."
        )
        return

    expense_list.insert(tk.END, f"{description} - ${amount:.2f}")
    description_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)


window = tk.Tk()

window.title("Expense Tracker")
window.geometry("700x600")

title = tk.Label(
    window,
    text="Expense Tracker",
    font=("Arial", 20)
)

title.pack()

description = tk.Label(
    window,
    text="Description"
)

description.pack()

description_entry = tk.Entry(window)

description_entry.pack()

amount = tk.Label(
    window,
    text="Amount"
)

amount.pack()

amount_entry = tk.Entry(window)

amount_entry.pack()

button = tk.Button(
    window,
    text="Add Expense",
    command=add_expense
)

button.pack()

expense_list = tk.Listbox(window)

expense_list.pack()

window.mainloop()
