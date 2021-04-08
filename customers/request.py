from animals import request


CUSTOMERS = [
    {
      "id": 1,
      "name": "Fannah Hall",
      "address": "5002 Thestnut Ct",
      "email": "fanhall@gmail.com"
    },
    {
      "id": 2,
      "name": "Hannah Hall",
      "address": "7002 Dhestnut Ct",
      "email": "hanhall@gmail.com"
    },
    {
      "id": 3,
      "name": "Dannah Hall",
      "address": "9002 Chestnut Ct",
      "email": "danhall@gmail.com"
    },
    {
      "id": 4,
      "name": "Pannah Hall",
      "address": "9002 Chestnut Ct",
      "email": "panhall@gmail.com"
    },
    {
      "id": 5,
      "name": "Eannah Hall",
      "address": "9002 Chestnut Ct",
      "email": "eanhall@gmail.com"
    },
    {
      "email": "openthedoor@gmail.com",
      "name": "Erica Thompson",
      "address": "1234 somewhere land",
      "id": 6
    },
    {
      "email": "younique9820@gmail.com",
      "name": "Erica Thompson",
      "address": "1245 over the moon st",
      "id": 7
    }
]
def get_all_customers():
    return CUSTOMERS

# Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found location, if it exists
    requested_customer = None
    # Iterate the LOCATIONS list above
    for customer in CUSTOMERS:
        # Utilize Dictionaries in Python
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer