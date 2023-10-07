# FakeStore API Documentation

## Products API
The Products API allows you to perform various product-related operations, including retrieving product details. Only admin users have permission to create, update, and delete products.

#### Get a List of Products
- **URL:** `/api/products/`
- **Method:** `GET`
- **Description:** Retrieve a list of all products.
- **Response:**
  - Status Code: `200 OK`
  - Data Type: JSON Array
  - Example Response:
    ```json
    [
        {
            "product_id": 1,
            "name": "Product Name 1",
            "description": "Product Description 1",
            "price": 99.99,
            "category": 1
        },
        {
            "product_id": 2,
            "name": "Product Name 2",
            "description": "Product Description 2",
            "price": 49.99,
            "category": 2
        }
        // ... more products
    ]
    ```

#### Get Product Details

- **URL:** `/api/products/{product_id}/`
- **Method:** `GET`
- **Description:** Retrieve details of a specific product by providing its unique `product_id`.

  **Response:**
  - Status Code: `200 OK`
  - Data Type: JSON Object
  - Example Response:
    ```json
    {
        "product_id": 1,
        "name": "Product Name 1",
        "description": "Product Description 1",
        "price": 99.99,
        "category": 1
    }
    ```
