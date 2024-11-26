from products import products

# You must build the following response, as a Python dictionary
response_example = {
    "categories": [
        {
            "id": 1,
            "title": "Books",
        },
        {
            "id": 2,
            "verbose": "Electronics",
        },
    ],
    "products": {
        "Electronics": [{"id": 3, "name": "Bluetooth Speaker"}],
    },
}

# categories is a list of all the unique categories that exist in the list products

# You task is to implement the function build_response(stores) and return a
# python dictionary like the response_example defined above.


def build_response(prods: dict):
    # step 1: which categories exist in the list stores?
    # step 2: build the response.
    # tip: python dictionary is you friend


response = build_response(products)
print(response)
