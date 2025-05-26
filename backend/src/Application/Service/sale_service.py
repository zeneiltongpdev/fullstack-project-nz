# sale_service.py
from src.Infrastructure.Model.product import Product
from src.Infrastructure.Model.seller import Seller
from src.Infrastructure.Model.sale import Sale
from src.config.data_base import db

class SaleService:
    @staticmethod
    def create_sale(product_id, quantity, seller_id):
        product = Product.query.get(product_id)
        seller = Seller.query.get(seller_id)
        
        # Validações
        if not product:
            raise ValueError("Produto não encontrado.")
        
        if not seller:
            raise ValueError("Vendedor não encontrado.")
        
        if seller.status != 'Ativo':
            raise ValueError("Vendedor inativo não pode realizar vendas.")    
        
        if product.status != 'ativo':
            raise ValueError("Produto inativo não pode ser vendido.")
        
        if product.quantity < quantity:
            raise ValueError(f"Quantidade indisponível. Disponível: {product.quantity}")
        
        if quantity <= 0:
            raise ValueError("Quantidade deve ser maior que zero.")
        
        # Calcula o preço total
        total_price = product.price * quantity
        
        # Cria a venda com o preço total
        sale = Sale(
            product_id=product_id,
            seller_id=seller_id,
            quantity=quantity,
            sale_price=total_price  # Aqui usamos o preço total
        )
        
        # Atualiza estoque
        product.quantity -= quantity
        
        db.session.add(sale)
        db.session.commit()
        
        return sale