# 💻 b2bit live coding challenge

Hello! Welcome to the b2bit coding challenge. This will test you in some simple Python concepts that we frequently use in our day-to-day work.


## Use case: building a market catalog page

Let's assume we have a list of products that we want to sell. Each product has a name, a price, and a category. Our task is to build the HTTP request so the frontend can display the following screen with the list of products with a single API call.


![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Store catalog page")


Your task is to use the data in the products.py file, handle the data in the most effiient way possible, and return the data in the JSON format using the following structure.


```json
{
    "categories": [category_1, category_2, ...],
    "products": {
        "category_1": [product_1, product_2, ...],
        "category_2": [product_1, product_2, ...],
        ...
    }
}
```

The categories array should contain the list of unique categories present in the products array found in the products.py file. The frontend will use this info in the section 1 above. The products array should contain the list all of the products, grouped by category. The frontend will use this info in the section 2 above.