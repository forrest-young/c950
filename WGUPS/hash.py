# Hash Map Creation Class, used to store, update, and retrieve package data
# Source: zyBook ISBN: 978-1-5418-4355-4 Chapter 7.8 -- Python: Hash Tables
# Time Complexity  : O(1) + O(N) + O(N) + O(N) = O(3N + 1) --> O(N)
# Space Complexity : O(1) + O(1) + O(1) + O(1) = O(4)      --> O(1)
class HashMap:
    # Constructor method, starts with 10 buckets
    # Time Complexity  : O(11) --> O(1)
    # Space Complexity : O(11) --> O(1)
    def __init__(self, init_capacity=10):
        self.map = []
        for i in range(init_capacity):
            self.map.append([])

    # Insertion method, modified to incorporate key/value pairs and updates
    # Time Complexity  : O(N + 9) --> O(N)
    # Space Complexity : O(5)     --> O(1)
    def insert(self, key, value):
        # Calculate bucket index, point bucket_list to corresponding map bucket
        bucket = hash(key) % len(self.map)
        bucket_list = self.map[bucket]

        # Search buckets for key, if found update value
        for item in bucket_list:
            if item[0] == key:
                item[1] = item
                return True

        # Otherwise insert key/value pair in corresponding bucket
        kv = [key, value]
        bucket_list.append(kv)
        return True

    # Search method, takes key and returns item
    # Time Complexity  : O(N + 5) --> O(N)
    # Space Complexity : O(3)     --> O(1)
    def search(self, key):
        bucket = hash(key) % len(self.map)
        bucket_list = self.map[bucket]
        for item in bucket_list:
            if key == item[0]:
                return item[1]
        return None

    # Deletion method, modified to remove entire key/value pairs
    # Time Complexity  : O(N + 7) --> O(N)
    # Space Complexity : O(5)     --> O(1)
    def delete(self, key):
        bucket = hash(key) % len(self.map)
        bucket_list = self.map[bucket]
        for item in bucket_list:
            if key in item:
                value = item[1]
                item.remove(key)
                item.remove(value)
        self.map[bucket] = list(filter(None, bucket_list))

    # Print method
    def __str__(self):
        s = ""
        for item in self.map:
            s += str(item) + "\n"
        return s
