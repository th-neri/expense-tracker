import tkinter as tk
from tkinter import ttk
from expenses_functions import add_expense, delete_expense, load_expenses, edit_expense, save_edit, search_expenses
import database

expenses = []
filtered_expenses = []

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
    text="Add expense",
    command=lambda: add_expense(
        connection,
        description_entry,
        amount_entry,
        category_entry,
        expense_list,
        total_amount,
        expenses
    )
)

button.pack()

search = tk.Label(
    window,
    text="Search"
)

search.pack()

search_entry = tk.Entry(window)

search_entry.pack()

search_entry.bind(
    "<KeyRelease>",
    lambda event: search_expenses(search_entry, expense_list, expenses, filtered_expenses)
)

expense_list = tk.Listbox(window)

expense_list.pack()

load_expenses(connection, expense_list, total_amount, expenses)

delete_button = tk.Button(
    window,
    text="Delete expense",
    command=lambda: delete_expense(connection, expense_list, total_amount, expenses, filtered_expenses)
)

delete_button.pack()

edit_button = tk.Button(
    window,
    text="Edit expense",
    command=lambda: edit_expense(expense_list, description_entry, amount_entry, category_entry, expenses, filtered_expenses)
)

edit_button.pack()

save_edit_button = tk.Button(
    window,
    text="Save edit",
    command=lambda: save_edit(connection, expense_list, description_entry, amount_entry, category_entry, total_amount, expenses, filtered_expenses)
)

save_edit_button.pack()

window.mainloop()
