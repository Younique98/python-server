class Employee():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, locationId):
        self.id = id
        self.name = name
        self.locationId = locationId

new_employee = Employee(6, "Rider", 2)