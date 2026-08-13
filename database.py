import sqlite3


def connect():
    connection = sqlite3.connect("expense_tracker.db")
    return connection

def create_tables(connection):
    with connection:
        connection.execute("""
        CREATE TABLE IF NOT EXISTS expenses(
                expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL
            )
        """)

def add_expense(connection, description, amount, category):
    with connection:
        connection.execute("INSERT INTO expenses(description, amount, category) VALUES(?, ?, ?)", (description, amount, category))

def get_expenses(connection):
    with connection:
        return connection.execute("SELECT expense_id, description, amount, category FROM expenses").fetchall()

def delete_expense(connection, expense_id):
    with connection:
        connection.execute("DELETE FROM expenses WHERE expense_id=?", (expense_id,))