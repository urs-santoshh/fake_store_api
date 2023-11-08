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
    ```json
          {
            "count": "integer",
            "next": "string($uri)",
            "previous": "string($uri)",
            "results":
                    [{
                      "id": "integer",
                      "seller": "string",
                      "category": "string",
                      "name": "string",
                      "desc": "string",
                      "image": "string($uri)",
                      "price": "string($decimal)",
                      "quantity": "integer",
                      "created_at": "string($date-time)",
                      "updated_at": "string($date-time)"
                    }]
          }
    ```
- **Query Parameters:**
  - `page`: Use the `page` parameter for pagination. Example: `GET /api/products/?page=1`.
  - `price`: Filter products with a given price. Example: `GET /api/products/?price=50`.
  - `min_price`: Filter products with a minimum price. Example: `GET /api/products/?min_price=50`.
  - `max_price`: Filter products with a maximum price. Example: `GET /api/products/?max_price=100`.

#### Get a List of Products Categories

- **URL:** `/api/products/categories/`
- **Method:** `GET`
- **Description:** Retrieve a list of all products categories.
- **Response:**
  - Status Code: 200 OK
  - Data Type: JSON Array
  - Example Response:
    ```json
          {
            "count": "integer",
            "next": "string($uri)",
            "previous": "string($uri)",
            "results":
                    [{
                      "id": "integer",
                      "name": "string",
                      "icon": "string($uri)",
                      "created_at": "string($date-time)",
                      "updated_at": "string($date-time)"
                    }]
          }
    ```

#### Get Product Categories Details

- **URL:** `/api/products/categories/{category_id}/`
- **Method:** `GET`
- **Description:** Retrieve details of a specific product category by providing its unique `category_id`.
- **Response:**
  - Status Code: 200 OK
  - Data Type: JSON Object
  - Example Response:
    ```json
          {
            "id": "integer",
            "name": "string",
            "icon": "string($uri)",
            "created_at": "string($date-time)",
            "updated_at": "string($date-time)"
          }
    ```

#### Get Product Details

- **URL:** `/api/products/{product_id}/`
- **Method:** `GET`
- **Description:** Retrieve details of a specific product by providing its unique `product_id`.
- **Response:**
  - Status Code: 200 OK
  - Data Type: JSON Object
  - Example Response:
    ```json
          {
            "id": "integer",
            "seller": "string",
            "category": "string",
            "name": "string",
            "desc": "string",
            "image": "string($uri)",
            "price": "string($decimal)",
            "quantity": "integer",
            "created_at": "string($date-time)",
            "updated_at": "string($date-time)"
          }
    ```
  Non-authenticated users and authenticated users (non-admin or non-seller) can only use GET requests to retrieve product details.


#### Update a Product (Admin or seller Only)

- **URL:** `/api/products/{product_id}/`
- **Method:** `PUT or PATCH`
- **Description:** Update the details of a specific product by providing its unique product_id and the new product details in the request body. This operation is restricted to admin users or to the seller if they are the owner of the product.
- **Request Headers:**
  - Authorization: Basic your_valid_authentication_token_here
  - Content-Type: application/json
  - X-CSRFToken: your_csrf_token
- **Request Body Example:**
  ```json
        {
          "category": {
              "name": "string",
              "icon": "null",
          },
            "name": "string",
            "desc": "string",
            "image": "null",
            "price": "string($decimal)",
            "quantity": "integer"
        }
  ```
- **Response:**
  - Status Code: 200 OK
  - Data Type: JSON Object
  - Example Response (Newly Created Product):
    ```JSON
        {
          "category": {
              "id": "integer",
              "name": "string",
              "icon": "string($uri)",
              "created_at": "string($date-time)",
              "updated_at": "string($date-time)"
          },
          "name": "string",
          "desc": "string",
          "image": "string($uri)",
          "price": "string($decimal)",
          "quantity": "integer"
        }
    ```

#### DELETE a Product (Admin or Seller Only)

- **URL:** `/api/products/{product_id}/`
- **Method:** `DELETE`
- **Description:** Delete the specific product by providing its unique product_id. This operation is restricted to admin users or the seller if they are the owner of the product.
- **Request Headers:**
  - Authorization: Token your_valid_admin_token_here
  - Content-Type: application/json
  - X-CSRFToken: your_csrf_token
- **Response:**
  - Status Code: 204 No Content
