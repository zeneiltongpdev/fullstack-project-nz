from src.Application.Service.product_service import ProductService
from src.config.data_base import db 
from werkzeug.utils import secure_filename
from flask import request, jsonify, make_response
from src.Infrastructure.Model.product import Product
import os

UPLOAD_FOLDER = 'src/uploads/'

class ProductController:
    
    def register_product():
        try:
            file = request.files['image']
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)

            name = request.form.get('name')
            price = float(request.form.get('price', 0))
            quantity = int(request.form.get('quantity', 0))
            status = request.form.get('status', 'Ativo')

            if not name or not price or not quantity:
                return make_response(jsonify({"erro": "Preencha todos os campos obrigatórios!"}), 400)

            # Verifica se já existe produto com mesmo nome (independente do preço)
            existing_product = Product.query.filter_by(name=name).first()
            if existing_product:
                # Atualiza a quantidade e o preço do produto existente
                existing_product.quantity += quantity
                existing_product.price = price  # Atualiza para o novo preço
                existing_product.image = filepath  # Atualiza a imagem também
                existing_product.status = status  # Atualiza o status se necessário
                
                db.session.commit()
                
                return make_response(jsonify({
                    "mensagem": "Produto já existente. Quantidade e preço atualizados com sucesso!",
                    "produto": existing_product.to_dict()
                }), 200)

            # Cria novo produto se não existir
            product = Product(
                name=name,
                price=price,
                quantity=quantity,
                status=status,
                image=filepath
            )
            
            db.session.add(product)
            db.session.commit()

            return make_response(jsonify({
                "mensagem": "Produto cadastrado com sucesso!",
                "produto": product.to_dict()
            }), 201)

        except ValueError as e:
            db.session.rollback()
            return make_response(jsonify({"erro": str(e)}), 409)

        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({"erro": str(e)}), 500)
        
   
    def get_products():
        try:
            products = Product.query.all()
            return make_response(jsonify([product.to_dict() for product in products]), 200)

        except Exception as e:
            return make_response(jsonify({"erro": str(e)}), 500)

  
    def get_product(product_id):
        try:
            product = Product.query.get(product_id)
            if not product:
                return make_response(jsonify({"erro": "Produto não encontrado"}), 404)

            return make_response(jsonify(product.to_dict()), 200)

        except Exception as e:
            return make_response(jsonify({"erro": str(e)}), 500)

    
    def update_product(product_id):
        try:
            product = Product.query.get(product_id)
            if not product:
                return make_response(jsonify({"erro": "Produto não encontrado"}), 404)

            data = request.get_json()
            product.name = data.get("name", product.name)
            product.price = data.get("price", product.price)
            product.quantity = data.get("quantity", product.quantity)
            product.status = data.get("status", product.status)
            product.image = data.get("image", product.image)

            db.session.commit()

            return make_response(jsonify({"mensagem": "Produto atualizado com sucesso!"}), 200)

        except Exception as e:
            return make_response(jsonify({"erro": str(e)}), 500)

    
    def inactivate_product(product_id):
        try:
            product = Product.query.get(product_id)
            if not product:
                return make_response(jsonify({"erro": "Produto não encontrado"}), 404)

            product.status = "Inativo"
            db.session.commit()

            return make_response(jsonify({"mensagem": "Produto inativado com sucesso!"}), 200)

        except Exception as e:
            return make_response(jsonify({"erro": str(e)}), 500)