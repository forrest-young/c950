# Package class, stores relevant delivery information
class Package:
    # Constructor method
    def __init__(self, pack_id, pack_address, pack_city, pack_state, pack_zip, pack_deadline, pack_weight, pack_note):
        self.pack_id = pack_id
        self.pack_address = pack_address
        self.pack_city = pack_city
        self.pack_state = pack_state
        self.pack_zip = pack_zip
        self.pack_deadline = pack_deadline
        self.pack_weight = pack_weight
        self.pack_note = pack_note
        self.pack_status = 'Hub'
        self.start_time = None
        self.end_time = None

    # Method used to check package status
    def status_update(self, time):
        if self.end_time <= time:
            self.pack_status = 'Delivered'
        elif self.start_time <= time:
            self.pack_status = 'En route'
        else:
            self.pack_status = 'Hub'

    # Print method
    def __str__(self):
        s = "Package ID : %s\nAddress    : %s\n             %s, %s %s\nDeadline   : %s\nWeight     : %s\nStatus     : %s" \
            % (self.pack_id, self.pack_address, self.pack_city, self.pack_state, self.pack_zip, self.pack_deadline,
               self.pack_weight, self.pack_status)

        if self.pack_status == 'Delivered':
            s += " --> Departed at %s | Arrived at %s\n" % (self.start_time, self.end_time)
        elif self.pack_status == 'En route':
            s += " --> Departed at %s\n" % self.start_time
        else:
            s += "\n"

        return s
