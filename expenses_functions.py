import tkinter as tk
from tkinter import messagebox
import database

def add_expense(connection, description_entry, amount_entry, category_entry, expense_list, total_amount, expenses):
    description = description_entry.get()
    amount = amount_entry.get()
    category = category_entry.get()

    if description == "":
        messagebox.showerror(
            "Invalid description",
            "Please enter a valid description."
        )
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror(
            "Invalid amount",
            "Please enter valid number(s)."
        )
        return

    if amount <= 0:
        messagebox.showerror(
            "Invalid amount",
            "Amount must be greater than 0."
        )
        return

    if category == "":
        messagebox.showerror(
            "Invalid category",
            "Please select a category."
        )
        return

    expenses.append({
        "description": description,
        "amount": amount,
        "category": category
    })

    database.add_expense(connection, description, amount, category)

    expense_list.insert(tk.END, f"{description} - ${amount:.2f} - {category}")
    description_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_entry.set("Food")

    update_total(expenses, total_amount)


def delete_expense(connection, expense_list, total_amount, expenses, filtered_expenses):
    selected = expense_list.curselection()

    if selected:
        index = selected[0]

        if filtered_expenses:
            expense = filtered_expenses[index]
        else:
            expense = expenses[index]

        expense_id = expense["id"]

        database.delete_expense(connection, expense_id)
        expenses.remove(expense)

        if filtered_expenses:
            filtered_expenses.remove(expense)

        expense_list.delete(index)

        update_total(expenses, total_amount)

def update_total(expenses, total_amount):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    total_amount.config(text=f"Total: ${total:.2f}")

def load_expenses(connection, expense_list, total_amount, expenses):
    saved_expenses = database.get_expenses(connection)

    for expense in saved_expenses:
        expense_id, description, amount, category = expense

        expenses.append({
            "id": expense_id,
            "description": description,
            "amount": amount,
            "category": category
        })

        expense_list.insert(tk.END, f"{description} - ${amount:.2f} - {category}")

    update_total(expenses, total_amount)

def edit_expense(expense_list, description_entry, amount_entry, category_entry, expenses, filtered_expenses):
    selected = expense_list.curselection()

    if not selected:
        return

    index = selected[0]

    if filtered_expenses:
        expense = filtered_expenses[index]
    else:
        expense = expenses[index]

    description_entry.delete(0, tk.END)
    description_entry.insert(0, expense["description"])

    amount_entry.delete(0, tk.END)
    amount_entry.insert(0, expense["amount"])

    category_entry.set(expense["category"])

def save_edit(connection, expense_list, description_entry, amount_entry, category_entry, total_amount, expenses, filtered_expenses):
    selected = expense_list.curselection()

    if not selected:
        return

    index = selected[0]

    if filtered_expenses:
        expense = filtered_expenses[index]
    else:
        expense = expenses[index]

    expense_index = expenses.index(expense)

    description = description_entry.get()
    amount = amount_entry.get()
    category = category_entry.get()

    if description == "":
        messagebox.showerror(
            "Invalid description",
            "Please enter a valid description."
        )
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror(
            "Invalid amount",
            "Please enter valid number(s)."
        )   
        return

    if amount <= 0:
        messagebox.showerror(
            "Invalid amount",
            "Amount must be greater than 0."
        )
        return

    if category == "":
        messagebox.showerror(
            "Invalid category",
            "Please select a category."
        )
        return

    expense_id = expense["id"]

    database.update_expense(connection, expense_id, description, amount, category)

    expense["description"] = description
    expense["amount"] = amount
    expense["category"] = category

    expense_list.delete(index)

    expense_list.insert(index, f"{description} - ${amount:.2f} - {category}")

    update_total(expenses, total_amount)

def search_expenses(search_entry, expense_list, expenses, filtered_expenses):
    search = search_entry.get().lower()

    expense_list.delete(0, tk.END)

    filtered_expenses.clear()

    for expense in expenses:
        description = expense["description"].lower()
        category = expense["category"].lower()

        if search in description or search in category:
            filtered_expenses.append(expense)

            expense_list.insert(
                tk.END,
                f"{expense['description']} - "
                f"${expense['amount']:.2f} - "
                f"{expense['category']}"
            )