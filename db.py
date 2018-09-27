from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['category-product-api']


class Item(object):
    """docstring for Item"""
    def __init__(self, name='', description='', child_categories=[], **kwargs):
        self.name = name
        self.description = description
        self.child_categories = child_categories


    def get_all(self):
        return db[self.collection_name].find()


    def save(self, collection_name):
        if self.name:
            db[collection_name].insert_one(self.__dict__)
        else:
            raise Exception('name is compulsory field')


class Category(Item):
    """docstring for Category
    - Add a category
    - Category can have multiple child categories. 
    - Child category can have further child categories. 
    - Category can have multiple products and product can have a multiple categories. 
    - Get all categories with all its child categories mapped to it.
    Note : Each category object should look something like this:
    {Id : 1 , child_categories: [], ...}
    """

    collection_name = 'categories'

    def __init__(self, child_products=[]):
        super(Category, self).__init__()
        self.child_products = child_products

    def add_category(self, name, description=''):
        self.name = name
        self.save()

    def save(self):
        super(Category, self).save(collection_name=self.collection_name)


class Product(Item):
    """docstring for Product
    - Category can have multiple products and product can have a multiple categories. 
    - Add Product mapped to a category or categories.
    - Get all products by a category
    - Update product details (name,price,etc) 
    """

    collection_name = 'products'

    def __init__(self, price=None, **kwargs):
        super(Product, self).__init__()
        self.price = price

    def add_product(self, name, categories=[]):
        if categories:
            pass
        else:
            raise Exception('Insufficient details')


    def save(self):
        super(Product, self).save(collection_name=self.collection_name)
