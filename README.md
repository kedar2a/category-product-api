# category-product-api
> Flask based API for nested Categories and Products hierarchy


- The Entities are a “Categories” and “Products”. 
- Category can have multiple child categories. 
- Child category can have further child categories. 
- Category can have multiple products and product can have a multiple categories.
- The Entities will get saved in `MongoDB` and be retrieved via `POST` and `GET` Methods respectively.

---

Designed a proper Mongodb data model and APIs to 
  1. Add a category 
  2. Add Product mapped to a category or categories. 
  3. Get all categories with all its child categories mapped to it. Note : Each category object should look something like this {Id : 1 , child_categories: [], ...} 
  4. Get all products by a category. 
  5. Update product details (`name`, `price`, etc) 
