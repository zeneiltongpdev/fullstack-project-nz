from src.Application.Service.sale_service import SaleService
from src.config.data_base import db
from flask import request, jsonify, make_response
from src.Infrastructure.Model.sale import Sale


class SaleController:
    @staticmethod
    def create_sale():
        try:
            data = request.get_json()
            product_id = data.get('product_id')
            seller_id = data.get('seller_id')
            quantity = data.get('quantity')

            if not all([product_id, quantity, seller_id]):
                return make_response(jsonify({"erro": "product_id e quantity são obrigatórios!"}), 400)

            sale = SaleService.create_sale(
                product_id=product_id,
                seller_id=seller_id,
                quantity=quantity
            )

            return make_response(jsonify({
                "mensagem": "Venda realizada com sucesso!",
                "venda": sale.to_dict()  # Já incluirá o sale_price calculado
            }), 201)

        except ValueError as e:
            db.session.rollback()
            return make_response(jsonify({"erro": str(e)}), 400)

        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({"erro": str(e)}), 500)

    @staticmethod
    def get_sales():
        try:
            sales = Sale.query.all()
            return make_response(jsonify([sale.to_dict() for sale in sales]), 200)
        except Exception as e:
            return make_response(jsonify({"erro": str(e)}), 500)

    @staticmethod
    def get_sale(sale_id):
        try:
            sale = Sale.query.get(sale_id)
            if not sale:
                return make_response(jsonify({"erro": "Venda não encontrada"}), 404)

            return make_response(jsonify(sale.to_dict()), 200)
        except Exception as e:
            return make_response(jsonify({"erro": str(e)}), 500)