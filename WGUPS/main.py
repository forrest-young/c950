# Author: Forrest Young
# WGU Student ID: 000833199
# Overall Time Complexity  : O(N) + O(N) + O(N) + O(N) + O(1) + O(N^2) + O(N^2) + O(N) + O(N)    = O(2N^2 + 6N + 1) --> O(N^2)
# Overall Space Complexity : O(1) + O(1) + O(1) + O(1) + O(1) + O(N) + O(1) + O(N) + O(1) + O(1) = O(2N + 8)        --> O(N)

import csv
import datetime

from hash import HashMap
from packages import Package
from trucks import Truck


# Set difference method, returns set containing elements only found in set 1
# Time Complexity  : O(2N + 3) --> O(N)
# Space Complexity : O(3)      --> O(1)
def set_difference(set_1, set_2):
    set_diff = set()
    for element in set_1:
        if element not in set_2:
            set_diff.add(element)
    return set_diff


# Set union method, returns set containing elements found in multiple sets
# Time Complexity  : O(3N + 5) --> O(N)
# Space Complexity : O(4)      --> O(1)
def set_union(set_1, set_2, set_3):
    set_u = set()
    for element in set_1:
        set_u.add(element)
    for element in set_2:
        set_u.add(element)
    for element in set_3:
        set_u.add(element)
    return set_u


# References the address table and returns address index from an address string
# Time Complexity  : O(N + 2) --> O(N)
# Space Complexity : O(1)     --> O(1)
def address_lookup(address):
    for row in addressFile:
        if address in row[1]:
            return int(row[0])


# References the address table and returns address quadrant from an address string
# Time Complexity  : O(N + 2) --> O(N)
# Space Complexity : O(1)     --> O(1)
def quadrant_lookup(address):
    for row in addressFile:
        if address in row[1]:
            return str(row[2])


# References the distance table and returns the distance between two addresses
# Assumes distance from point_a to point_b is the same as from point_b to point_a
# Time Complexity  : O(6) --> O(1)
# Space Complexity : O(3) --> O(1)
def distance_lookup(point_a, point_b):
    d = distanceFile[point_a][point_b]
    if d == '':
        d = distanceFile[point_b][point_a]

    return float(d)


# Imports package data from file and inserts each package object into a hash map
# Time Complexity  : O(11N + 4) --> O(N)
# Space Complexity : O(N + 13)  --> O(N)
def import_package_data(hash_map):
    with open('packageData.csv') as file:
        reader = csv.reader(file)
        _i = 0

        for row in reader:
            _pack_id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zipcode = row[4]
            deadline = row[5]
            weight = row[6]
            note = row[7]

            _package = Package(_pack_id, address, city, state, zipcode, deadline, weight, note)
            hash_map.insert(_pack_id, _package)
            _i += 1

        return _i


# Package sorting method, takes a package hash map and returns an array of lists
# First sorts packages with delivery instructions and early deadlines, then uses
# quadrants to efficiently load packages which are relatively close together
# Time Complexity  : O(4N^2 + 49N + 26) --> O(N^2)
# Space Complexity : O(13)              --> O(1)
def sort_packages(_packages):
    # Create sets for packages which ensures only a single package ID can be in any one bag
    bag_1 = set()
    bag_2 = set()
    bag_3 = set()
    bag_o = set()
    swap_bag = set()

    quadrant_a = set()
    quadrant_b = set()
    quadrant_c = set()
    quadrant_d = set()
    quadrant_e = set()
    quadrant_f = set()

    # Search packages for delivery instructions
    for _i in range(1, no_of_packages + 1):
        _package = _packages.search(_i)
        if 'truck 2' in _package.pack_note:
            if len(bag_2) < truck_max_capacity:
                bag_2.add(_i)
            else:
                print('Truck is full.  Will deliver package ID %d on the next available route' % _i)
                bag_o.add(_i)
        elif 'Delayed' in _package.pack_note:
            if len(bag_2) < truck_max_capacity and _package.pack_deadline != 'EOD':
                bag_2.add(_i)
            elif len(bag_3) < truck_max_capacity and _package.pack_deadline == 'EOD':
                bag_3.add(_i)
            elif len(bag_2) < truck_max_capacity:
                bag_2.add(_i)
            elif len(bag_3) < truck_max_capacity:
                bag_3.add(_i)
            else:
                print('Trucks are full.  Will deliver package ID %d on the next available route' % _i)
                bag_o.add(_i)
        elif 'Wrong address' in _package.pack_note:
            if len(bag_3) < truck_max_capacity:
                bag_3.add(_i)
            else:
                print('Truck is full.  Will deliver package ID %d on the next available route' % _i)
                bag_o.add(_i)
        elif 'Must be delivered' in _package.pack_note:
            _s = _package.pack_note[23:].split(',')
            if len(bag_1) < truck_max_capacity - (len(_s) + 1):
                bag_1.add(_i)
                for s_id in _s:
                    bag_1.add(int(s_id))
            elif len(bag_2) < truck_max_capacity - (len(_s) + 1):
                bag_2.add(_i)
                for s_id in _s:
                    bag_2.add(int(s_id))
            elif len(bag_3) < truck_max_capacity - (len(_s) + 1):
                bag_3.add(_i)
                for s_id in _s:
                    bag_3.add(int(s_id))
            else:
                print('Unable to accommodate delivery of multiple packages.')
                bag_o.add(_i)
                for s_id in _s:
                    bag_o.add(int(s_id))
        elif _package.pack_note != '':
            print('Unexpected delivery instruction.  Will deliver package ID %d to the listed address ASAP' % _i)
            if len(bag_1) < truck_max_capacity and (len(bag_1) <= len(bag_2) or len(bag_1) <= len(bag_3)):
                bag_1.add(_i)
            elif len(bag_2) < truck_max_capacity and (len(bag_2) <= len(bag_1) or len(bag_2) <= len(bag_3)):
                bag_2.add(_i)
            elif len(bag_3) < truck_max_capacity and (len(bag_3) <= len(bag_1) or len(bag_3) <= len(bag_2)):
                bag_3.add(_i)
            else:
                print('Trucks are full.  Will deliver package ID %d on the next available route' % _i)
                bag_o.add(_i)

    # Search packages without a delivery note, place early deadlines on earliest truck and sort the rest into quadrants
    for _i in range(1, no_of_packages + 1):
        _package = packages.search(_i)
        if _package.pack_note == '':
            if _package.pack_deadline == '9:00' or _package.pack_deadline == '10:30':
                bag_1.add(_i)
            elif quadrant_lookup(_package.pack_address) == 'a':
                quadrant_a.add(_i)
            elif quadrant_lookup(_package.pack_address) == 'b':
                quadrant_b.add(_i)
            elif quadrant_lookup(_package.pack_address) == 'c':
                quadrant_c.add(_i)
            elif quadrant_lookup(_package.pack_address) == 'd':
                quadrant_d.add(_i)
            elif quadrant_lookup(_package.pack_address) == 'e':
                quadrant_e.add(_i)
            elif quadrant_lookup(_package.pack_address) == 'f':
                quadrant_f.add(_i)

    # Ensure packages aren't on multiple trucks
    quadrant_a = set_difference(quadrant_a, set_union(bag_1, bag_2, bag_3))
    quadrant_b = set_difference(quadrant_b, set_union(bag_1, bag_2, bag_3))
    quadrant_c = set_difference(quadrant_c, set_union(bag_1, bag_2, bag_3))
    quadrant_d = set_difference(quadrant_d, set_union(bag_1, bag_2, bag_3))
    quadrant_e = set_difference(quadrant_e, set_union(bag_1, bag_2, bag_3))
    quadrant_f = set_difference(quadrant_f, set_union(bag_1, bag_2, bag_3))

    # Sort quadrants into trucks : quadrants A/B are northernmost
    #                            : quadrants C/D are central
    #                            : quadrants E/F are southernmost
    for _pack_id in quadrant_a:
        if len(bag_3) < truck_max_capacity:
            bag_3.add(_pack_id)
        else:
            bag_o.add(_pack_id)

    for _pack_id in quadrant_b:
        if len(bag_3) < truck_max_capacity:
            bag_3.add(_pack_id)
        else:
            bag_o.add(_pack_id)

    for _pack_id in quadrant_c:
        if len(bag_2) < truck_max_capacity:
            bag_2.add(_pack_id)
        else:
            bag_o.add(_pack_id)

    for _pack_id in quadrant_d:
        if len(bag_1) < truck_max_capacity:
            bag_1.add(_pack_id)
        else:
            bag_o.add(_pack_id)

    for _pack_id in quadrant_e:
        if len(bag_2) < truck_max_capacity:
            bag_2.add(_pack_id)
        else:
            bag_o.add(_pack_id)

    for _pack_id in quadrant_f:
        if len(bag_2) < truck_max_capacity:
            bag_2.add(_pack_id)
        else:
            bag_o.add(_pack_id)

    # If any packages were placed into the overflow bag check if there is any remaining space on any of the trucks
    for _pack_id in bag_o:
        swap_bag.add(_pack_id)

    for _pack_id in swap_bag:
        if len(bag_1) < truck_max_capacity:
            bag_1.add(_pack_id)
            bag_o.remove(_pack_id)
        elif len(bag_2) < truck_max_capacity:
            bag_2.add(_pack_id)
            bag_o.remove(_pack_id)
        elif len(bag_3) < truck_max_capacity:
            bag_3.add(_pack_id)
            bag_o.remove(_pack_id)
        else:
            print('Trucks are full.  Will deliver package ID %d on the next available route' % _pack_id)

    # Return sorted packages
    _bags = [list(bag_1), list(bag_2), list(bag_3), list(bag_o)]
    return _bags


# Route compilation method, takes a truck and uses a Nearest Neighbor algorithm to
# deliver each package.  Packages are moved into an array and reinserted in the order
# they are delivered.  Delivery times and mileage is updated with each package iteration
# Time Complexity  : O(3N^2 + 8N + 5) --> O(N^2)
# Space Complexity : O(N + 4)         --> O(N)
def compile_delivery_route(truck):
    undelivered_packages = []
    for _pack_id in truck.loaded_packages:
        _package = packages.search(_pack_id)
        _package.start_time = truck.departure
        undelivered_packages.append(packages.search(_pack_id))
    truck.loaded_packages.clear()

    while len(undelivered_packages) > 0:
        nearest_package = undelivered_packages[0]
        next_address_distance = distance_lookup(address_lookup(truck.current_address), address_lookup(nearest_package.pack_address))
        # Cycle through packages which haven't been delivered and compare the distance of each package.
        for _package in undelivered_packages:
            if distance_lookup(address_lookup(truck.current_address), address_lookup(_package.pack_address)) <= next_address_distance:
                nearest_package = _package
                next_address_distance = distance_lookup(address_lookup(truck.current_address), address_lookup(nearest_package.pack_address))
        # Once the nearest package is found, update package and truck information
        undelivered_packages.remove(nearest_package)
        truck.loaded_packages.append(nearest_package.pack_id)
        truck.mileage += float(next_address_distance)
        truck.current_address = nearest_package.pack_address
        truck.current_time += datetime.timedelta(hours=next_address_distance / 18)
        nearest_package.end_time = truck.current_time
    # Once all packages have been delivered, return to hub.  If return mileage is to be recorded then include the following:
    # truck.mileage += distance_lookup(address_lookup(truck.current_address), address_lookup('4001 South 700 East'))
    truck.current_time += datetime.timedelta(hours=distance_lookup(address_lookup(truck.current_address),
                                                                   address_lookup('4001 South 700 East')) / 18)
    truck.current_address = '4001 South 700 East'


# Open and read distance data from file
with open("distanceData.csv") as file1:
    distanceFile = csv.reader(file1)
    distanceFile = list(distanceFile)

# Open and read address data from file
with open("addressData.csv") as file2:
    addressFile = csv.reader(file2)
    addressFile = list(addressFile)


# Main method : initializes trucks, loads package and address data, then calculates delivery route.
# The user interface consists of a main menu allowing the user to access package and truck information
# Time Complexity  : O(9N + 39)  --> O(N)
# Space Complexity : O(15)       --> O(1)
if __name__ == '__main__':
    # Create truck objects
    truck_max_capacity = 16
    truck_avg_speed = 18
    truck_1 = Truck(truck_max_capacity, None, '4001 South 700 East', 0, truck_avg_speed, datetime.timedelta(hours=8, minutes=0))
    truck_2 = Truck(truck_max_capacity, None, '4001 South 700 East', 0, truck_avg_speed, datetime.timedelta(hours=9, minutes=5))
    truck_3 = Truck(truck_max_capacity, None, '4001 South 700 East', 0, truck_avg_speed, datetime.timedelta(hours=10, minutes=20))
    trucks = [truck_1, truck_2, truck_3]

    # Create package hash map
    packages = HashMap()
    # Import package data, save number of packages imported for further iterations
    no_of_packages = import_package_data(packages)
    # Sort packages into bags
    sorted_packages = sort_packages(packages)

    # Load each truck with the sorted packages
    for i in range(len(sorted_packages) - 1):
        trucks[i].load_packages(sorted_packages[i])

    # Compile delivery route for each truck
    for i in range(len(trucks)):
        # Ensures third truck leaves no earlier than the earliest returned truck
        if i == 2:
            if truck_1.current_time > truck_3.departure and truck_2.current_time > truck_3.departure:
                truck_3.departure = min(truck_1.current_time, truck_2.current_time)
        compile_delivery_route(trucks[i])

    # Additional logic required in the event of a non-empty overflow bag
    #
    # while sorted_packages[3] is not empty:
    #   for truck in trucks:
    #       truck.loaded_packages.clear()
    #   overflow_packages = sorted_packages[3]
    #   sorted_packages = sort_packages(overflow_packages)
    #   for i in range(len(sorted_packages) - 1):
    #       trucks[i].departure = trucks[i].current_time
    #       trucks[i].load_packages(sorted_packages[i])
    #   for i in range(len(trucks)):
    #       if i == 2:
    #           if truck_1.current_time > truck_3.departure and truck_2.current_time > truck_3.departure:
    #                   truck_3.departure = min(truck_1.current_time, truck_2.current_time)
    #               compile_delivery_route(trucks[i])

    print('Welcome to my WGUPS Program')
    print('Delivery route total mileage: %.2f' % (truck_1.mileage + truck_2.mileage + truck_3.mileage))
    print('Please enter from the following options:')

    # Main loop user interface
    done = False
    while not done:
        try:
            user_input = input('1 : Check status of ALL packages\n2 : Check status of an INDIVIDUAL package\n'
                               '3 : Check status of delivery trucks\n4 : Exit program\n')
            if user_input == '1':
                # Ask user for a time to check
                time_input = input('Enter the time you would like to check.  Use the following format -> HH:mm\n')
                (hour, minute) = time_input.split(':')
                time_input = datetime.timedelta(hours=int(hour), minutes=int(minute))

                # Iterate through each package and update package status with the provided time
                for i in range(1, no_of_packages + 1):
                    package = packages.search(i)
                    package.status_update(time_input)
                    print(package)
            elif user_input == '2':
                # Ask user for a time to check
                time_input = input('Enter the time you would like to check.  Use the following format -> HH:mm\n')
                (hour, minute) = time_input.split(':')
                time_input = datetime.timedelta(hours=int(hour), minutes=int(minute))

                # Second loop allows for individual package status
                _done = False
                while not _done:
                    # Ask user for a package ID
                    pack_id = input('Enter the package ID (1 - ' + str(no_of_packages) + '). Enter 0 to return to the main menu : ')
                    if 1 <= int(pack_id) <= no_of_packages:
                        package = packages.search(int(pack_id))
                        package.status_update(time_input)
                        print(package)
                    # Return to the main menu
                    elif int(pack_id) == 0:
                        _done = True
                    else:
                        print('Invalid package ID.  Please try again')
            elif user_input == '3':
                # Print truck information
                for i in range(len(trucks)):
                    print(trucks[i], '\n')
                print('Delivery route total mileage: %.2f' % (truck_1.mileage + truck_2.mileage + truck_3.mileage), '\n')
            elif user_input == '4':
                # Exit program
                done = True
            else:
                print('Unexpected input.  Please enter a valid number')
        except ValueError:
            print('Unexpected input.  Please try again')
