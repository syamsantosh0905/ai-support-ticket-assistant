import sqlite3

def get_connection():
    return sqlite3.connect("tickets.db")

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            category TEXT,
            priority TEXT,
            status TEXT DEFAULT 'Open'
        )
    """)

    conn.commit()
    conn.close()

def save_ticket(description, category=None, priority=None):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tickets (description, category, priority)
        VALUES (?, ?, ?)
    """, (description, category, priority))

    conn.commit()
    ticket_id = cursor.lastrowid
    conn.close()

    return ticket_id

def get_tickets():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tickets")
    tickets = cursor.fetchall()

    conn.close()
    return tickets