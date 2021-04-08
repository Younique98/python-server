from animals import request

EMPLOYEES = [
    {
      "id": 1,
      "name": "Jeremy Bakker",
      "locationId": 2
    },
    {
      "id": 2,
      "name": "Eeremy Bakker",
      "locationId": 1
    },
    {
      "id": 3,
      "name": "Feremy Bakker",
      "locationId": 2
    },
    {
      "id": 4,
      "name": "Neremy Bakker",
      "locationId": 1
    }    
]
def get_all_employees():
    return EMPLOYEES

# Function with a single parameter
def get_single_employee(id):
    #Variable to hold the found employee, if it exists
    requested_employee = None
    # Iterate the EMPLOYEES list above
    for employee in EMPLOYEES:
        # Utilize Dictionaries in Python
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee