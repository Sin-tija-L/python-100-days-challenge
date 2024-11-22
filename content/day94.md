# **Day 94: Getting Started with SQLite3 in Python**

---

🎯 **Objective**:
Learn the basics of working with SQLite3 in Python: creating a database, tables, and performing basic CRUD (Create, Read, Update, Delete) operations.

---

📚 **What is SQLite3?**
SQLite3 is a lightweight, self-contained database engine that is easy to use and requires no setup. It’s ideal for small to medium-sized applications and for learning SQL concepts. SQLite3 databases are stored in a single file on your computer.

---

## 🛠 Setting Up SQLite3 in Python

### Step 1: Importing SQLite3
SQLite3 is part of Python’s standard library. You don’t need to install it separately.

```python
import sqlite3
```

### Step 2: Connecting to a Database
To work with SQLite3, you need to connect to a database. If the file doesn’t exist, it will be created automatically.

```python
# Connect to or create a database
connection = sqlite3.connect("example.db")

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

print("Connected to the database!")
```

---

## 📝 Creating a Table

A table is a collection of rows and columns that store related data.

```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,  -- Auto-incremented primary key
    name TEXT NOT NULL,      -- Name of the student (Required)
    age INTEGER,             -- Age of the student
    grade TEXT               -- Grade of the student
)
""")
connection.commit()
print("Table created!")
```

### **Explanation**:
- `id INTEGER PRIMARY KEY`: Unique identifier for each row.
- `name TEXT NOT NULL`: Text column that cannot be empty.
- `age INTEGER`: Stores numerical data.
- `grade TEXT`: Stores text values.

---

## ✍️ Inserting Data into a Table

You can insert rows into a table using the `INSERT INTO` statement.

### Single Record
```python
cursor.execute("""
INSERT INTO students (name, age, grade)
VALUES ('Alice', 23, 'A')
""")
connection.commit()
print("Data inserted successfully!")
```

### Batch Insert
Insert multiple rows at once with `executemany`.

```python
students = [
    ('Bob', 22, 'B'),
    ('Clara', 24, 'A'),
    ('Dave', 21, 'C')
]
cursor.executemany("""
INSERT INTO students (name, age, grade)
VALUES (?, ?, ?)
""", students)
connection.commit()
print("Batch data inserted!")
```

---

## 🔍 Querying Data

### Fetch All Records
```python
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()  # Fetch all rows

for row in rows:
    print(row)
```

### Filtering with WHERE Clause
Fetch specific rows by adding conditions.

```python
cursor.execute("SELECT * FROM students WHERE grade = 'A'")
rows = cursor.fetchall()

for row in rows:
    print(row)
```

---

## 🔄 Updating and Deleting Data

### Updating Records
Modify existing data using the `UPDATE` statement.

```python
cursor.execute("""
UPDATE students
SET grade = 'B'
WHERE name = 'Alice'
""")
connection.commit()
print("Record updated!")
```

### Deleting Records
Remove specific rows with the `DELETE` statement.

```python
cursor.execute("""
DELETE FROM students
WHERE name = 'Dave'
""")
connection.commit()
print("Record deleted!")
```

---

# 🏁 Challenge for Day 94:

1. Create a table named `books` with columns:
   - `id`: Primary key
   - `title`: Text (not null)
   - `author`: Text
   - `year_published`: Integer
2. Insert at least three books into the table.
3. Write SQL queries to:
   - Fetch all books.
   - Fetch books published after 2000.
   - Update the author of one book.
   - Delete a book based on its title.

<img id="image" src="assets/day94_1.png" alt="day94 image" width="750">

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
