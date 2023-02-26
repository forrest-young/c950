# Truck class, stores relevant delivery information
class Truck:
    # Constructor method
    def __init__(self, max_capacity, loaded_packages, current_address, mileage, avg_speed, departure):
        self.max_capacity = max_capacity
        self.loaded_packages = loaded_packages
        self.current_address = current_address
        self.mileage = mileage
        self.avg_speed = avg_speed
        self.departure = departure
        self.current_time = departure

    # Method used to load the truck with packages
    def load_packages(self, pack_ids):
        self.loaded_packages = pack_ids

    # Print method
    def __str__(self):
        return "Max Capacity    : %s\nLoaded Packages : %s\nMileage         : %s\nDeparture       : %s\nReturned " \
               "to Hub : %s" % (self.max_capacity, self.loaded_packages, self.mileage, self.departure, self.current_time)
