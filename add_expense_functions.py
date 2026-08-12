import tkinter as tk
from tkinter import messagebox

def add_expense(description_entry, amount_entry, category_entry, expense_list, total_amount):
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

    expense_list.insert(tk.END, f"{description} - ${amount:.2f} - {category}")
    description_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_entry.set("Food")

    update_total(expense_list, total_amount)


def delete_expense(expense_list, total_amount):
    selected = expense_list.curselection()

    if selected:
        expense_list.delete(selected)
        update_total(expense_list, total_amount)

def update_total(expense_list, total_amount):
    total = 0

    for expense in expense_list.get(0, tk.END):
        amount = expense.split(" - ")[1]
        amount = amount.replace("$", "")
        total += float(amount)

    total_amount.config(text=f"Total: ${total:.2f}")