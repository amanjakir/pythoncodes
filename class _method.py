class Car:
    total_cars = 0  # Class attribute

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1  # Increment the total_cars count for each instance

    @classmethod
    def display_total_cars(cls):
        print(f"Total Cars: {cls.total_cars}")

