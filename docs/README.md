# FakeStore API Documentation

### Models
![Model](/docs/fake_store_db_eer.png)

#### Product Model

The Product model represents a product available in the FakeStore. It includes the following fields:

- `product_id` (AutoField): The unique identifier for the product.
- `name` (CharField): The name of the product (max length: 255).
- `description` (TextField): A detailed description of the product.
- `price` (DecimalField): The price of the product with decimal places.
- `category` (ForeignKey): A foreign key to the Category model, indicating the product's category.

#### Category Model

The Category model represents product categories in the FakeStore. It includes the following fields:

- `category_id` (AutoField): The unique identifier for the category.
- `name` (CharField): The name of the category (max length: 100).

Feel free to customize the models' descriptions and diagrams based on your project's specific requirements. This visual representation of the models can help users understand the structure of your database at a glance.
