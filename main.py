import tkinter as tk
from tkinter import ttk
from add_expense_functions import add_expense, delete_expense
import database

expenses = []

connection = database.connect()
database.create_tables(connection)

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

category = tk.Label(
    window,
    text="Category"
)

category.pack()

category_entry = ttk.Combobox(
    window,
    values=[
        "Food",
        "Transport",
        "Entertainment",
        "Health",
        "Other"
    ]
)

category_entry.pack()

category_entry.set("Food")

total_amount = tk.Label(
    window,
    text="Total: $0.00",
    font=("Arial", 15)
)

total_amount.pack()

button = tk.Button(
    window,
    text="Add Expense",
    command=lambda: add_expense(
        description_entry,
        amount_entry,
        category_entry,
        expense_list,
        total_amount,
        expenses
    )
)

button.pack()

expense_list = tk.Listbox(window)

expense_list.pack()

delete_button = tk.Button(
    window,
    text="Delete expense",
    command=lambda: delete_expense(expense_list, total_amount, expenses)
)

delete_button.pack()


window.mainloop()
