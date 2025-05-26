class PureProductDomain:
    def __init__(self, name, description, price, category, stock_quantity):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.stock_quantity = stock_quantity

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "category": self.category,
            "stock_quantity": self.stock_quantity
        }