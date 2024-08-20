import pickle

class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, address):
        self.contacts[name] = address

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def get_contact(self, name):
        return self.contacts.get(name)

    def display_contacts(self):
        for name, address in self.contacts.items():
            print(f"{name}: {address}")

# Функції для серіалізації/десеріалізації
def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повертаємо нову адресну книгу, якщо файл не знайдено

# Основний цикл програми
def main():
    # Завантаження адресної книги з файлу при запуску
    book = load_data()

    while True:
        command = input("Enter command (add, remove, display, exit): ").strip().lower()
        
        if command == "add":
            name = input("Enter name: ").strip()
            address = input("Enter address: ").strip()
            book.add_contact(name, address)
        
        elif command == "remove":
            name = input("Enter name to remove: ").strip()
            book.remove_contact(name)
        
        elif command == "display":
            book.display_contacts()
        
        elif command == "exit":
            # Збереження адресної книги перед виходом
            save_data(book)
            print("Address book saved. Exiting...")
            break
        
        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()
