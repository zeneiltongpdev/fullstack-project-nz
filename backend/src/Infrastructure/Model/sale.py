from src.config.data_base import db
from datetime import datetime

class Sale(db.Model):
    __tablename__ = 'sales'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('sellers.id'), nullable=False)  # Novo campo
    quantity = db.Column(db.Integer, nullable=False)
    sale_price = db.Column(db.Float, nullable=False)
    sale_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
   

    product = db.relationship('Product', backref='sales')
    seller = db.relationship('Seller', backref='sales')

    def __init__(self, product_id, quantity, sale_price, seller_id):
        self.product_id = product_id
        self.seller_id = seller_id
        self.quantity = quantity
        self.sale_price = sale_price
     
    
    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "seller_id": self.seller_id,
            "quantity": self.quantity,
            "sale_price": self.sale_price,
            "sale_date": self.sale_date.isoformat()
        
        }