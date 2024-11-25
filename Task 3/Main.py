class Stadium:
    def __init__(self, name='', opening_date='', country='', city='', capacity=0):
        self.__name = name
        self.__opening_date = opening_date
        self.__country = country
        self.__city = city
        self.__capacity = capacity

    def enter_details(self):
        self.__name = input("Zadejte název stadionu: ")
        self.__opening_date = input("Zadejte datum otevření: ")
        self.__country = input("Zadejte zemi: ")
        self.__city = input("Zadejte město: ")
        self.__capacity = int(input("Zadejte kapacitu: "))

    def display_details(self):
        print(f"Název stadionu: {self.__name}")
        print(f"Datum otevření: {self.__opening_date}")
        print(f"Země: {self.__country}")
        print(f"Město: {self.__city}")
        print(f"Kapacita: {self.__capacity} míst")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_opening_date(self):
        return self.__opening_date

    def set_opening_date(self, opening_date):
        self.__opening_date = opening_date

    def get_country(self):
        return self.__country

    def set_country(self, country):
        self.__country = country

    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, capacity):
        self.__capacity = capacity

# Example usage
if __name__ == "__main__":
    stadium = Stadium()
    stadium.enter_details()
    stadium.display_details()

    # Access individual fields
    print("\nAktualizace názvu stadionu...")
    stadium.set_name("Velky stadion " + stadium.get_name())
    print(f"Aktualizovaný název stadionu: {stadium.get_name()}")