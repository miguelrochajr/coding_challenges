from stores import stores

# You must build the following response, as a Python dictionary
response_example = {
    'category_list': [
        {
            'category_id': 1,
            'category_verbose': 'Conveniência',
        },
        {
            'category_id': 1,
            'category_verbose': 'Conveniência',
        },
    ],
    'stores': stores
}

# category_list is a list of all the unique store types that exist in stores

# You task is to implement the function build_response(stores) and return a
# python dictionary like the response_example defined above. The stores object
# CAN be mutated.

def build_response(stores):
    print(stores)

resposne = build_response(stores)
print(resposne)
