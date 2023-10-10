class NationalPark:

    def __init__(self, name):
        self.name = name

        self._trips = []
        self._visitors = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if type(name) == str and len(name) >= 3 and not hasattr(self, "name"):
            self._name = name
        else:
            raise Exception("Name must be a string greater than or equal to 3 characters!")
            
        
    def trips(self):
        return self._trips
    
    def visitors(self):
        return list(set(self._visitors))
    
    def total_visits(self):
        return len(self._trips)
    
    # Have Eleanor explain this part to me step-by-step before the code challenge
    def best_visitor(self):
        return max(self._visitors, key = self._visitors.count, default = None)

class Visitor:

    def __init__(self, name):
        self.name = name

        self._trips = []
        self._national_parks = []

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, name):
        if type(name) == str and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception("Name must be a string between 1 and 15 characters!")
        
    def trips(self):
        return self._trips
    
    def national_parks(self):
        return list(set(self._national_parks))
    
    # monkey = ["Zion", "Yellowstone", "Zion"]
    
    def total_visits_at_park(self, park):
        total_visits = 0
        for item in self._national_parks:
            if item == park:
                total_visits += 1
        return total_visits


class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

        self.visitor._trips.append(self)
        self.visitor._national_parks.append(self.national_park)

        self.national_park._trips.append(self)
        self.national_park._visitors.append(self.visitor)

        Trip.all.append(self)

    #visitor property
    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            raise Exception("Visitor must be instance of class Visitor!")
    
    #national_park property
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise Exception("national_park must be instance of class NationalPark!")

    #start_date property
    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if type(start_date) == str and len(start_date) >= 7:
            self._start_date = start_date
        else:
            raise Exception("start_date must be a string longer than 7 characters!")

    #end_date property
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        if type(end_date) == str and len(end_date) >= 7:
            self._end_date = end_date
        else:
            raise Exception("end_date must be a string longer than 7 characters!")