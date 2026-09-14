# агрегація, тип зв'язку між класами, коли один клас "володіє" об'єктами іншого класу, але ці об'єкти можуть існувати незалежно.

class Vehicle:
    def __init__(self, vehicle_type, registration_number):
        self.vehicle_type = vehicle_type
        self.registration_number = registration_number

    def display_info(self):
        return f"Vehicle Type: {self.vehicle_type}, Registration Number: {self.registration_number}"


class Ride:
    def __init__(self, passenger_name, vehicle):
        self.passenger_name = passenger_name
        self.vehicle = vehicle

    def start_ride(self):
        print(f"Ride started for {self.passenger_name}.")
        print("Vehicle details:", self.vehicle.display_info())

    def end_ride(self):
        print(f"Ride ended for {self.passenger_name}.")


vehicle1 = Vehicle("Car", "AB1234XY")

ride1 = Ride("Alice", vehicle1)

ride1.start_ride()
ride1.end_ride()

vehicle2 = Vehicle("Bike", "CD5678YZ")
print("Independent Vehicle Info:", vehicle2.display_info())
