import os

# --- Helper Functions ---
def display_menu():
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

def add_book(library):
    print("\n--- Add a Book ---")
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    try:
        year = int(input("Enter the publication year: "))
    except ValueError:
        print("Invalid year. Please enter a valid number.")
        return
    genre = input("Enter the genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower()
    read = True if read_status in ['yes', 'y'] else False

    # Add the book to the library
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    print(f"Book '{title}' added successfully!")

def remove_book(library):
    print("\n--- Remove a Book ---")
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print(f"Book '{title}' removed successfully!")
            return
    print(f"Book '{title}' not found in the library.")

def search_books(library):
    print("\n--- Search for a Book ---")
    print("Search by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        query = input("Enter the title: ").strip().lower()
        matches = [book for book in library if query in book["title"].lower()]
    elif choice == "2":
        query = input("Enter the author: ").strip().lower()
        matches = [book for book in library if query in book["author"].lower()]
    else:
        print("Invalid choice.")
        return

    if matches:
        print("\nMatching Books:")
        for idx, book in enumerate(matches, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No matching books found.")

def display_all_books(library):
    print("\n--- Your Library ---")
    if not library:
        print("Your library is empty.")
        return
    for idx, book in enumerate(library, 1):
        status = "Read" if book["read"] else "Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def display_statistics(library):
    print("\n--- Library Statistics ---")
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    unread_books = total_books - read_books

    if total_books > 0:
        percentage_read = (read_books / total_books) * 100
    else:
        percentage_read = 0.0

    print(f"Total books: {total_books}")
    print(f"Books read: {read_books}")
    print(f"Books unread: {unread_books}")
    print(f"Percentage read: {percentage_read:.1f}%")

def save_library(library, filename="library.txt"):
    with open(filename, "w") as file:
        for book in library:
            file.write(f"{book['title']}|{book['author']}|{book['year']}|{book['genre']}|{book['read']}\n")
    print("Library saved to file.")

def load_library(filename="library.txt"):
    library = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                title, author, year, genre, read = line.strip().split("|")
                book = {
                    "title": title,
                    "author": author,
                    "year": int(year),
                    "genre": genre,
                    "read": read == "True"
                }
                library.append(book)
    return library

# --- Main Program ---
def main():
    # Load library from file (if it exists)
    library = load_library()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()