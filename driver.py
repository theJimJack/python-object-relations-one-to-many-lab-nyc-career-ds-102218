# remeber to import the trip class here
from trip import Trip

class Driver:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def my_trips(self): #return all instance objects
        trip_list = []
        for x in Trip._all:
            if x.driver == self.name:
                trip_dict = {}
                trip_dict['trip start'] = x.start
                trip_dict['trip destination'] = x.destination
                trip_dict['driver name'] = x.driver
                trip_list.append(trip_dict)
        return trip_list

    def my_trip_summaries(self):
        # trip_list = []
        # for x in
        #
        #
        # return
        pass
