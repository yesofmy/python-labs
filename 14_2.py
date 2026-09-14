#Продемонструйте використання поліморфізму у Python без наслідування та детальну роботу з класами та об'єктами.


class TaxiService:
    def calculate_fare(self, distance, time):
        return distance * 2 + time * 0.5

    def calculate_wait_time(self, traffic_level):
        return 10 + traffic_level * 2


class RideSharing:
    def calculate_fare(self, distance, time):
        return distance * 1.5 + time * 0.3

    def calculate_wait_time(self, traffic_level):
        return 5 + traffic_level * 1.5


class BusService:
    def calculate_fare(self, distance):
        return distance * 0.8

    def calculate_wait_time(self, schedule):
        return max(0, schedule - 5)


'''def process_service(service, *args):
    if hasattr(service, "calculate_fare") and hasattr(service, "calculate_wait_time"):
        if len(args) == 2:
            distance, time_or_traffic = args
            print("Fare:", service.calculate_fare(distance, time_or_traffic))
            print("Wait time:", service.calculate_wait_time(time_or_traffic))
        elif len(args) == 1:
            distance_or_schedule = args[0]
            if "distance" in service.calculate_fare.__code__.co_varnames:
                print("Fare:", service.calculate_fare(distance_or_schedule))
            print("Wait time:", service.calculate_wait_time(distance_or_schedule))
    else:
        print("Service does not support required operations.")'''


taxi = TaxiService()
rideshare = RideSharing()
bus = BusService()

print("Taxi Service:")
print(taxi.calculate_fare(10, 25))

print("\nRide Sharing:")
print(rideshare.calculate_fare(8, 10))

print("\nBus Service:")
print(bus.calculate_fare(20))