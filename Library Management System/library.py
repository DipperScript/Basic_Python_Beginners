import tkinter as tk
from tkinter import messagebox

class Library:
    def __init__(self):
        self.books = {}
        self.recently_added = []

    def add_book(self, book_id, title, author):
        if book_id not in self.books:
            self.books[book_id] = {'title': title, 'author': author, 'available': True}
            self.recently_added.insert(0, book_id)
            if len(self.recently_added) > 5:
                self.recently_added.pop()

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            if book_id in self.recently_added:
                self.recently_added.remove(book_id)

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")

        self.library = Library()

        self.label = tk.Label(root, text="Library Management System", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.book_id_label = tk.Label(root, text="Book ID:")
        self.book_id_label.pack()

        self.book_id_entry = tk.Entry(root)
        self.book_id_entry.pack()

        self.title_label = tk.Label(root, text="Title:")
        self.title_label.pack()

        self.title_entry = tk.Entry(root)
        self.title_entry.pack()

        self.author_label = tk.Label(root, text="Author:")
        self.author_label.pack()

        self.author_entry = tk.Entry(root)
        self.author_entry.pack()

        self.add_button = tk.Button(root, text="Add Book", command=self.add_book)
        self.add_button.pack()

        self.remove_button = tk.Button(root, text="Remove Book", command=self.remove_book)
        self.remove_button.pack()

        self.recent_label = tk.Label(root, text="Recently Added Books:")
        self.recent_label.pack()

        self.recent_books_text = tk.Text(root, height=5, width=40)
        self.recent_books_text.pack()

        # Configure the recently added books text widget as read-only
        self.recent_books_text.config(state=tk.DISABLED)

    def add_book(self):
        book_id = self.book_id_entry.get()
        title = self.title_entry.get()
        author = self.author_entry.get()

        if book_id and title and author:
            self.library.add_book(book_id, title, author)
            self.update_recent_books()
            self.clear_input_fields()  # Clear input fields after adding book
            self.show_message("Book added successfully.")
        else:
            self.show_message("Please fill in all fields.")

    def remove_book(self):
        book_id = self.book_id_entry.get()
        if book_id:
            self.library.remove_book(book_id)
            self.update_recent_books()
            self.clear_input_fields()  # Clear input fields after removing book
            self.update_books_display()  # Update the displayed book list
            self.show_message("Book removed successfully.")
        else:
            self.show_message("Please enter a book ID.")

    def update_books_display(self):
        book_list = "\n".join([f"{self.library.books[book_id]['title']} by {self.library.books[book_id]['author']}" for book_id in self.library.books])
        self.books_text.delete(1.0, tk.END)
        self.books_text.insert(tk.END, book_list)

    def update_recent_books(self):
        recent_books = "\n".join([f"{self.library.books[book_id]['title']} by {self.library.books[book_id]['author']}" for book_id in self.library.recently_added])
        self.recent_books_text.config(state=tk.NORMAL)  # Enable text widget to modify content
        self.recent_books_text.delete(1.0, tk.END)
        self.recent_books_text.insert(tk.END, recent_books)
        self.recent_books_text.config(state=tk.DISABLED)  # Disable text widget to prevent modifications

    def clear_input_fields(self):
        self.book_id_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)

    def show_message(self, message):
        messagebox.showinfo("Message", message)

def main():
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
