from animals import request


LOCATIONS = [
    {
      "id": 1,
      "name": "Nashville North",
      "address": "8422 Johnson Pike"
    },
    {
      "id": 2,
      "name": "Nashville South",
      "address": "209 Emory Drive"
    }
]
def get_all_locations():
    return LOCATIONS

# Function with a single parameter
def get_single_location(id):
    # Variable to hold the found location, if it exists
    requested_location = None
    # Iterate the LOCATIONS list above
    for location in LOCATIONS:
        # Utilize Dictionaries in Python
        if location["id"] == id:
            requested_location = location

    return requested_location