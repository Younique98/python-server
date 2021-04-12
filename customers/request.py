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
    },
    {
      "id": 8,
      "name": "Fannah Hall",
      "address": "5002 Thestnut Ct",
      "email": "fanhall@gmail.com"
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

def create_customer(customer):
    # Get the id value of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the customer dictionary
    customer["id"] = new_id

    # Add the customer dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer

def delete_customer(id):
    # Initial -1 value for customer index, in case one isn't found
    customer_index = -1

    # Iterate the customerS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Store the current index.
            customer_index = index

    # If the customer was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    # Iterate the customerS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Update the value.
            CUSTOMERS[index] = new_customer
            break