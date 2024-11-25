class Car:
    def __init__(self, model=None, year=None, manufacturer=None, engine_capacity=None, color=None, price=None):
        self._model = model
        self._year = year
        self._manufacturer = manufacturer
        self._engine_capacity = engine_capacity
        self._color = color
        self._price = price

    # Metoda pro zadání dat
    def input_data(self):
        self._model = input("Zadejte model auta: ")
        self._year = int(input("Zadejte rok výroby: "))
        self._manufacturer = input("Zadejte výrobce: ")
        self._engine_capacity = float(input("Zadejte objem motoru (v litrech): "))
        self._color = input("Zadejte barvu auta: ")
        self._price = float(input("Zadejte cenu: "))

    # Metoda pro výpis dat
    def output_data(self):
        print(f"Model: {self._model}")
        print(f"Rok výroby: {self._year}")
        print(f"Výrobce: {self._manufacturer}")
        print(f"Objem motoru: {self._engine_capacity} L")
        print(f"Barva: {self._color}")
        print(f"Cena: {self._price} Kč")

    # Gettery a settery pro jednotlivá pole
    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    def get_year(self):
        return self._year

    def set_year(self, year):
        self._year = year

    def get_manufacturer(self):
        return self._manufacturer

    def set_manufacturer(self, manufacturer):
        self._manufacturer = manufacturer

    def get_engine_capacity(self):
        return self._engine_capacity

    def set_engine_capacity(self, engine_capacity):
        self._engine_capacity = engine_capacity

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

# Příklad použití
if __name__ == "__main__":
    car = Car()
    car.input_data()  # Zadání údajů o autě
    print("\nDetaily auta:")
    car.output_data()  # Výpis údajů o autě

    # Přístup k jednotlivým polím pomocí getterů a setterů
    print("\nAktualizace ceny auta...")
    car.set_price(35000)
    print(f"Aktualizovaná cena: {car.get_price()} Kč")
