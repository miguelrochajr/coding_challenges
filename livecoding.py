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

# category_list is a list of all the unique categories that exist in the list stores

# You task is to implement the function build_response(stores) and return a
# python dictionary like the response_example defined above.

def build_response(stores)
    # step 1: which categories exist in the list stores?
    # step 2: build the response.
    # tip: python dictionary is you friend
    print(stores)

resposne = build_response(stores)
print(resposne)
