# FakeStore API Documentation

## Products API
The Products API allows you to perform various operations related to products, including retrieving product details. Only admin users have permission to create, update, and delete products.

#### Get List of Products
    - **URL:** `/api/products/`
    - **Method:** `GET`
    - **Description:** Retrieve a list of all products.

#### Get Product Details
    - **URL:** `/api/products/{product_id}/`
    - **Method:** `GET`
    - **Description:** Retrieve details of a specific product by providing its unique `product_id`.

### Create a New Product (Admin Only)
    - **URL:** `/api/products/`
    - **Method:** `POST`
    - **Description:** Create a new product by providing product details in the request body. This operation is restricted to admin users.
    **Request Body Example:**
    ```json
    {
        "name": "Product Name",
        "description": "Product Description",
        "price": 99.99,
        "category": 1  // Replace with the category ID
    }