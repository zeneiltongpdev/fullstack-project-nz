from src.config.data_base import db


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='Ativo')
    image = db.Column(db.String(255))

    def __init__(self, name, price, quantity, status='Ativo', image=None):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.status = status
        self.image = image
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "status": self.status,
            "image": self.image
        }