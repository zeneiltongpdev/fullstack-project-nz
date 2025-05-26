from src.Infrastructure.Model.product import Product
from src.config.data_base import db

class ProductService:
    @staticmethod
    def create_product(name, price, quantity, status='Ativo', image=None):
        # Verifica se já existe um produto com o mesmo nome
        existing_product = Product.query.filter_by(name=name).first()
        if existing_product:
            raise ValueError("Já existe um produto com este nome.")

        # Validações básicas
        if price <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        
        if quantity < 0:
            raise ValueError("A quantidade não pode ser negativa.")

        # Cria o novo produto
        product = Product(
            name=name,
            price=price,
            quantity=quantity,
            status=status,
            image=image
        )

        # Persiste no banco de dados
        db.session.add(product)
        db.session.commit()
        
        return product