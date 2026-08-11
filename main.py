import tkinter as tk

def add_expense():
    description = description_entry.get()
    amount = amount_entry.get()

    if description:
        expense_list.insert(tk.END, f"{description} - ${amount}")  
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