from datetime import datetime

class PureSaleDomain:
    def __init__(self, product_id, quantity, sale_price, sale_date=None):
        self.product_id = product_id
        self.quantity = quantity
        self.sale_price = sale_price
        self.sale_date = sale_date or datetime.utcnow()
    
    def to_dict(self):
        return {
            "product_id": self.product_id,
            "quantity": self.quantity,
            "sale_price": self.sale_price,
            "sale_date": self.sale_date.isoformat()
        }

    def validate_quantity(self, available_quantity):
        if self.quantity <= 0:
            raise ValueError("Quantidade deve ser maior que zero")
        if self.quantity > available_quantity:
            raise ValueError(f"Quantidade indisponível. Disponível: {available_quantity}")