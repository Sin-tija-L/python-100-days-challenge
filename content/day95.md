# **Day 95: Advanced SQLite3 and Python**

---

🎯 **Objective**:
Dive deeper into SQL concepts: sorting, aggregating data, and handling SQL errors. Also, learn how to organize SQLite3 workflows in Python scripts.

---

## 📚 Key Concepts

### **1. Sorting Results**
Use `ORDER BY` to sort data.

```python
cursor.execute("SELECT * FROM students ORDER BY age DESC")
rows = cursor.fetchall()

for row in rows:
    print(row)
```

### **2. Aggregating Data**
Use functions like `COUNT`, `AVG`, and `SUM` to perform calculations.

```python
cursor.execute("SELECT AVG(age) AS average_age FROM students")
average_age = cursor.fetchone()[0]
print(f"Average age: {average_age}")
```

### **3. Transactions**
Ensure data consistency by grouping multiple operations.

```python
try:
    connection.execute("BEGIN")
    cursor.execute("UPDATE students SET grade = 'A' WHERE name = 'Bob'")
    cursor.execute("DELETE FROM students WHERE name = 'Clara'")
    connection.commit()
    print("Transaction successful!")
except sqlite3.Error as e:
    connection.rollback()
    print("Transaction failed:", e)
```

### **4. Handling Errors**
Gracefully handle errors with `try-except`.

```python
try:
    cursor.execute("SELECT * FROM non_existing_table")
except sqlite3.Error as e:
    print("Error occurred:", e)
```

---

# 🏁 Challenge for Day 95:

1. Expand the `books` table to include a new column `genre`.
2. Write a Python script to:
   - Add genres to all existing books.
   - Fetch and display books grouped by genre.
   - Calculate the total number of books and the average publication year.
3. Introduce error handling to ensure your script doesn’t crash if invalid SQL commands are executed.

<img id="image" src="assets/day95_1.png" alt="day95 image" width="890">

---

## Solution (No Peeking!)

<details>
<summary>👀 Answer</summary>

```python
import sqlite3

# Connect to or create the database
connection = sqlite3.connect("books.db")
cursor = connection.cursor()

# Step 1: Create the books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT,
    year_published INTEGER
)
""")
connection.commit()
print("Books table created.")

# Step 2: Insert at least three books into the table
books = [
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925),
    ("1984", "George Orwell", 1949),
    ("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997)
]
cursor.executemany("""
INSERT INTO books (title, author, year_published)
VALUES (?, ?, ?)
""", books)
connection.commit()
print("Books inserted into the table.")

# Step 3: Fetch all books
print("\nAll books:")
cursor.execute("SELECT * FROM books")
all_books = cursor.fetchall()
for book in all_books:
    print(book)

# Step 4: Fetch books published after 2000
print("\nBooks published after 2000:")
cursor.execute("SELECT * FROM books WHERE year_published > 2000")
recent_books = cursor.fetchall()
for book in recent_books:
    print(book)

# Step 5: Update the author of one book
cursor.execute("""
UPDATE books
SET author = 'Anonymous'
WHERE title = '1984'
""")
connection.commit()
print("\nAuthor updated for the book '1984'.")

# Step 6: Delete a book based on its title
cursor.execute("""
DELETE FROM books
WHERE title = 'The Great Gatsby'
""")
connection.commit()
print("\nDeleted 'The Great Gatsby' from the table.")

# Verify changes
print("\nBooks after updates:")
cursor.execute("SELECT * FROM books")
updated_books = cursor.fetchall()
for book in updated_books:
    print(book)

# Close the connection
connection.close()
print("\nDatabase connection closed.")
```

</details>