class Book:
    def __init__(self, title='', year=0, publisher='', genre='', author='', price=0.0):
        self.__title = title
        self.__year = year
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price

    def enter_details(self):
        self.__title = input("Zadejte název knihy: ")
        self.__year = int(input("Zadejte rok vydání: "))
        self.__publisher = input("Zadejte vydavatele: ")
        self.__genre = input("Zadejte žánr: ")
        self.__author = input("Zadejte autora: ")
        self.__price = float(input("Zadejte cenu: "))

    def display_details(self):
        print(f"Název: {self.__title}")
        print(f"Rok vydání: {self.__year}")
        print(f"Vydavatel: {self.__publisher}")
        print(f"Žánr: {self.__genre}")
        print(f"Autor: {self.__author}")
        print(f"Cena: {self.__price:.2f} Kč")

    # Getter and Setter for title
    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    # Getter and Setter for year
    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    # Getter and Setter for publisher
    def get_publisher(self):
        return self.__publisher

    def set_publisher(self, publisher):
        self.__publisher = publisher

    # Getter and Setter for genre
    def get_genre(self):
        return self.__genre

    def set_genre(self, genre):
        self.__genre = genre

    # Getter and Setter for author
    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    # Getter and Setter for price
    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

if __name__ == "__main__":
    book = Book()
    book.enter_details()
    book.display_details()

    print("\nAktualizace názvu knihy...")
    book.set_title("Stará " + book.get_title())
    print(f"Aktualizovaný název: {book.get_title()}")
