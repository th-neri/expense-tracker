import tkinter as tk
from tkinter import messagebox
import database

def add_expense(connection, description_entry, amount_entry, category_entry, expense_list, total_amount, expenses):
    description = description_entry.get()
    amount = amount_entry.get()
    category = category_entry.get()

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

    if category == "":
        messagebox.showerror(
            "Invalid category.",
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


def delete_expense(connection, expense_list, total_amount, expenses):
    selected = expense_list.curselection()

    if selected:
        index = selected[0]

        expense = expenses[index]
        expense_id = expense["id"]

        database.delete_expense(connection, expense_id)
        expense_list.delete(index)

        expenses.pop(index)

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