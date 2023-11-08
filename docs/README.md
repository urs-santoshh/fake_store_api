# FakeStore API Documentation
Here is the Entity-Relationship diagram generated using https://dbdiagram.io/. This visual representation of the models can help users understand the structure of your database at a glance.
![Model](/docs/fake_store_db_eer.png)

## Product Model

The `Product` model is an integral part of the Fake Store API, responsible for managing product information. This documentation provides an overview of the model's attributes and their functions. 

### Model Fields

- `seller`: ForeignKey to the User model, representing the seller of the product.

- `category`: ForeignKey to the ProductCategory model, representing the category to which the product belongs. If the category is not specified, it defaults to "Others."

- `name`: A character field with a maximum length of 200 characters, representing the product's name.

- `desc`: A text field for providing a description of the product. It can be left blank.

- `image`: An ImageField for uploading product images. This field is optional.

- `price`: A Decimal field with two decimal places, specifying the product's price.

- `quantity`: An integer field indicating the quantity of the product. It defaults to 1.

- `created_at`: DateTime field that records the date and time when the product was created.

- `updated_at`: DateTime field that is automatically updated whenever the product is modified.

### Model Functions

- `__str__(self)`: Returns the name of the product as a string, making it more human-readable when working with instances of this model.

### Model Meta Options

- `ordering`: Products are ordered by their `created_at` field in descending order, meaning the most recently created products will appear first.

### Default Product Category

A default product category named "Others" is provided to handle cases where a product is not explicitly assigned to a category.

### Important Notes

- When a product's category is not specified during creation, it will be automatically set to "Others" as the default.

- Images for the product and category are optional and can be left blank.


## Order and OrderItem Models

The `Order` and `OrderItem` models are essential components of the Fake Store API, responsible for managing orders and order items. This documentation provides an overview of their attributes and functions.

### Order Model

The `Order` model represents an order placed by a buyer and includes the following fields and properties:

### Model Fields

- `buyer`: ForeignKey to the User model, representing the buyer who placed the order.

- `status`: A character field with choices for order status, which can be "P" (Pending) or "C" (Completed). Orders are set to "Pending" by default.

- `shipping_address`: ForeignKey to the Address model, representing the shipping address for the order. It can be left blank or set to null if not applicable.

- `billing_address`: ForeignKey to the Address model, representing the billing address for the order. It can be left blank or set to null if not applicable.

- `created_at`: DateTime field that records the date and time when the order was created.

- `updated_at`: DateTime field that is automatically updated whenever the order is modified.

### Model Functions

- `__str__(self)`: Returns the full name of the buyer as a string, making it more human-readable when working with instances of this model.

- `total_cost`: A property that calculates the total cost of all items in the order.

### OrderItem Model

The `OrderItem` model represents an item within an order and includes the following fields and properties:

### Model Fields

- `order`: ForeignKey to the Order model, linking the order item to its parent order.

- `product`: ForeignKey to the Product model, linking the order item to the product being ordered.

- `quantity`: An integer field representing the quantity of the product in the order.

- `created_at`: DateTime field that records the date and time when the order item was created.

- `updated_at`: DateTime field that is automatically updated whenever the order item is modified.

### Model Functions

- `__str__(self)`: Returns the full name of the buyer who placed the order as a string.

- `cost`: A property that calculates the total cost of the order item.

### Model Meta Options

Both models have the following meta option:

- `ordering`: Orders and order items are ordered by their `created_at` field in descending order, meaning the most recently created orders and items will appear first.

### Important Notes

- The `status` field in the `Order` model is set to "Pending" by default but can be updated to "Completed" when the order is processed.

- Addresses for shipping and billing are optional and can be left blank or set to null.

- The `total_cost` property in the `Order` model calculates the total cost of all order items within the order.

- The `cost` property in the `OrderItem` model calculates the total cost of a single order item based on the product's price and quantity.


## Cart and CartItem Models

The `Cart` and `CartItem` models are integral components of the Fake Store API, responsible for managing user shopping carts and cart items. This documentation provides an overview of their attributes and functions.

### Cart Model

The `Cart` model represents a user's shopping cart and includes the following fields and properties:

### Model Fields

- `user`: OneToOneField to the User model, associating the cart with a specific user.

- `created_at`: DateTime field that records the date and time when the cart was created.

- `updated_at`: DateTime field that is automatically updated whenever the cart is modified.

### Model Functions

- `__str__(self)`: Returns the full name of the user associated with the cart as a string, making it more human-readable when working with cart instances.

- `total_cost`: A property that calculates the total cost of all items in the cart.

### CartItem Model

The `CartItem` model represents an item within a user's shopping cart and includes the following fields and properties:

### Model Fields

- `cart`: ForeignKey to the Cart model, linking the cart item to its parent cart.

- `product`: ForeignKey to the Product model, linking the cart item to the product being added to the cart.

- `quantity`: An integer field representing the quantity of the product in the cart.

- `created_at`: DateTime field that records the date and time when the cart item was created.

- `updated_at`: DateTime field that is automatically updated whenever the cart item is modified.

### Model Functions

- `__str__(self)`: Returns the full name of the user associated with the cart as a string.

- `cost`: A property that calculates the total cost of the cart item based on the product's price and quantity.

### Model Meta Options

Both models have the following meta option:

- `ordering`: Carts and cart items are ordered by their `created_at` field in descending order, meaning the most recently created carts and items will appear first.

### Important Notes

- Each user has one associated cart, as specified by the OneToOneField relationship.

- The `total_cost` property in the `Cart` model calculates the total cost of all cart items within the cart.

- The `cost` property in the `CartItem` model calculates the total cost of a single cart item based on the product's price and quantity.


## Profile and Address Models

The `Profile` and `Address` models are important components of the Fake Store API, responsible for managing user profiles and user addresses. This documentation provides an overview of their attributes and functions.

### Profile Model

The `Profile` model represents a user's profile and includes the following fields:

### Model Fields

- `user`: OneToOneField to the User model, linking the profile to a specific user.

- `avatar`: An ImageField for uploading user avatars. This field is optional.

- `bio`: A character field with a maximum length of 200 characters for a user's bio. It can be left blank.

- `created_at`: DateTime field that records the date and time when the profile was created.

- `updated_at`: DateTime field that is automatically updated whenever the profile is modified.

### Model Functions

- `__str__(self)`: Returns the full name of the user associated with the profile as a string, making it more human-readable when working with profile instances.

### Address Model

The `Address` model represents user addresses for billing and shipping purposes. It includes the following fields:

### Model Fields

- `user`: ForeignKey to the User model, linking the address to a specific user.

- `address_type`: A character field with choices for address type, which can be "B" (Billing) or "S" (Shipping).

- `default`: A boolean field indicating whether this is the user's default address.

- `country`: A CountryField to store the country of the address.

- `city`: A character field with a maximum length of 100 characters to store the city.

- `street_address`: A character field with a maximum length of 100 characters for the street address.

- `apartment_address`: A character field with a maximum length of 100 characters for apartment information. It can be left blank.

- `postal_code`: A character field with a maximum length of 20 characters to store the postal code. It can be left blank.

- `created_at`: DateTime field that records the date and time when the address was created.

- `updated_at`: DateTime field that is automatically updated whenever the address is modified.

### Model Functions

- `__str__(self)`: Returns the full name of the user associated with the address as a string.

### Model Meta Options

Both models have the following meta option:

- `ordering`: Profiles and addresses are ordered by their `created_at` field in descending order, meaning the most recently created profiles and addresses will appear first.

### Important Notes

- User profiles may include avatars and bios, but these fields are optional.

- The `Address` model allows users to have multiple addresses, specifying whether each address is for billing or shipping purposes.

- Users can set a default address, which may be used as the primary address for billing or shipping.

***Note: Feel free to extend this model or use these models as part of your Fake Store API project. For more details on how to integrate these models into your project, please refer to the source code and project documentation. For the source code, kindly check the respective `models.py` file in your project repository.***

