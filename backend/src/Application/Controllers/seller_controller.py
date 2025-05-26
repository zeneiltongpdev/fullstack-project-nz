# Arquivo: src/Interface/Controller/seller_controller.py
from src.Infrastructure.Model.seller import Seller
from src.config.data_base import db
from flask import request, jsonify, make_response

class SellerController:
    @staticmethod
    def create_seller():
        try:
            data = request.get_json()
            name = data.get('name')
            email = data.get('email')
            status = data.get('status', 'Ativo')

            if not all([name, email]):
                return make_response(jsonify({"erro": "Nome e email são obrigatórios!"}), 400)

            seller = Seller(
                name=name,
                email=email,
                status=status
            )
            
            db.session.add(seller)
            db.session.commit()

            return make_response(jsonify({
                "mensagem": "Vendedor cadastrado com sucesso!",
                "vendedor": seller.to_dict()
            }), 201)

        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({"erro": str(e)}), 500)