ANIMALS = [
    {
      "id": 2,
      "name": "AoodlesisAPoodle",
      "breed": "Poodle",
      "locationId": 2,
      "customerId": 2
    },
    {
      "id": 4,
      "name": "Toodles",
      "breed": "Poodle",
      "customerId": 4,
      "locationId": 2
    },
    {
      "id": 5,
      "name": "Roodles",
      "breed": "Poodle",
      "customerId": 5,
      "locationId": 2
    },
    {
      "id": 6,
      "name": "aoodles",
      "breed": "Poodle",
      "customerId": 5,
      "locationId": 2
    },
    {
      "name": "Fluffy",
      "breed": "Lion rabbit",
      "locationId": 2,
      "customerId": 1,
      "id": 7
    },
    {
      "name": "Elephant",
      "breed": "Larger Cute Elephant",
      "locationId": 1,
      "customerId": 3,
      "id": 8
    }
]
def get_all_animals():
    return ANIMALS

# Function with a single parameter
def get_single_animal(id):
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal
