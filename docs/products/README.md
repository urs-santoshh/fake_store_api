# FakeStore API Documentation

## Products API

The Products API allows you to perform various product-related operations, including retrieving product details. Only admin users have permission to create, update, and delete products.

#### Get a List of Products

- **URL:** `/api/products/`
- **Method:** `GET`
- **Description:** Retrieve a list of all products.
- **Response:**
  - Status Code: 200 OK
  - Data Type: JSON Array
  - Example Response:
    `json
        {
          "count": 2,
          "next": null,
          "previous": null,
          "results":
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
        }
    `
    The API supports pagination for large product lists. You can specify the page and page size as query parameters, e.g., /api/products/?page=1&page_size=10.

#### Get Product Details

- **URL:** `/api/products/{product_id}/`
- **Method:** `GET`
- **Description:** Retrieve details of a specific product by providing its unique `product_id`.
- **Response:**
  - Status Code: 200 OK
  - Data Type: JSON Object
  - Example Response:
    `json
        {
            "product_id": 1,
            "name": "Product Name 1",
            "description": "Product Description 1",
            "price": 99.99,
            "category": 1
        }
    `
    Non-authenticated users and authenticated users (non-admin) can only use GET requests to retrieve product details.

#### Create a New Product (Admin Only)

- **URL:** `/api/products/`
- **Method:** `POST`
- **Description:** Create a new product by providing product details in the request body. This operation is restricted to admin users.
- **Request Headers:**
  - Authorization: Basic your_valid_admin_token_here
  - Content-Type: application/json
  - X-CSRFToken: your_csrf_token
- **Request Body Example:**
  ```json
  {
    "name": "Product Name 111",
    "description": "Product Description 111",
    "price": 99.99,
    "category": 111 // Replace with the category ID
  }
  ```
- **Response:** - Status Code: 201 Created - Data Type: JSON Object - Example Response (Newly Created Product):
  `JSON
          {
              "product_id": 111,
              "name": "Product Name 111",
              "description": "Product Description 111",
              "price": 5999.00,
              "category": 111
          }
      `
  Products are categorized. You can assign a product to a specific category by providing the category field in the request body when creating or updating a product.

#### Update a Product (Admin Only)

- **URL:** `/api/products/{product_id}/`
- **Method:** `PATCH`
- **Description:** Update the details of a specific product by providing its unique product_id and the new product details in the request body. This operation is restricted to admin users.
- **Request Headers:**
  - Authorization: Basic your_valid_admin_token_here
  - Content-Type: application/json
  - X-CSRFToken: your_csrf_token
- **Request Body Example:**
  ```json
  {
    "name": "Updated Product Name",
    "description": "Updated Product Description",
    "price": 119.99,
    "category": 2 // Replace with the new category ID
  }
  ```
- **Response:**
  - Status Code: 200 OK
  - Data Type: JSON Object
  - Example Response (Newly Created Product):
    ```JSON
        {
            "product_id": 1,
            "name": "Updated Product Name",
            "description": "Updated Product Description",
            "price": 119.99,
            "category": 2
        }
    ```

#### DELETE a Product (Admin Only)

- **URL:** `/api/products/{product_id}/`
- **Method:** `DELETE`
- **Description:** Update the details of a specific product by providing its unique product_id and the new product details in the request body. This operation is restricted to admin users.
- **Request Headers:**
  - Authorization: Token your_valid_admin_token_here
  - Content-Type: application/json
- **Response:**
  - Status Code: 204 No Content
