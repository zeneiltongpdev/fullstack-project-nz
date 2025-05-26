from src.Application.Controllers.user_controller import UserController
from src.Application.Controllers.product_controller import ProductController
from src.Application.Controllers.sale_controller import SaleController
from src.Application.Controllers.seller_controller import SellerController
from flask import jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity

def init_routes(app):    
    @app.route('/api', methods=['GET'])
    def health():
        return make_response(jsonify({ 
            "mensagem": "API - OK",
        }), 200)
    
    @app.route('/user', methods=['POST'])
    def register_user():
        return UserController.register_user()
    
    @app.route('/users',methods=['GET'])
    @jwt_required()
    def get_users():
        return UserController.get_users()
    
    @app.route("/users/<int:user_id>", methods=["DELETE"])
    @jwt_required()
    def delete_user(user_id):
        return UserController.delete_user(user_id)
    
    @app.route("/users/<int:user_id>", methods=["PUT"])
    @jwt_required()
    def update_user(user_id):
        return UserController.update_user(user_id)

    @app.route('/login', methods=['POST'])
    def login_user():
        return UserController.login_user()

    @app.route('/ativar',methods=['POST'])
    def active_user():
        return UserController.active_user()

    @app.route('/protected', methods=['GET'])
    @jwt_required()
    def protected():
        return make_response(jsonify({
            "mensagem": "Esta é uma rota protegida!",
            "usuario_logado": get_jwt_identity()
        }), 200)
    
    
    #//////////////////////////////////////        PRODUTOS      //////////////////////////////////////////#
    

    @app.route('/products', methods=['POST'])
    @jwt_required()
    def register_product():
        return ProductController.register_product()
    
    @app.route('/products', methods=['GET'])
    @jwt_required()
    def get_products():
        return ProductController.get_products()
    
    @app.route('/products/<int:product_id>', methods=['GET'])
    @jwt_required()
    def get_product(product_id):
        return ProductController.get_product(product_id)
    
    @app.route('/products/<int:product_id>', methods=['PUT'])
    @jwt_required()
    def update_product(product_id):
        return ProductController.update_product(product_id)
    
    @app.route('/products/<int:product_id>/inactivate', methods=['PUT'])
    @jwt_required()
    def inactivate_product(product_id):
        return ProductController.inactivate_product(product_id)
    
        
    #//////////////////////////////////////        VENDAS      //////////////////////////////////////////#
    
    
    @app.route('/sale', methods=['POST'])
    def create_sale():
        return SaleController.create_sale()

    @app.route('/sales', methods=['GET'])
    def get_sales():
        return SaleController.get_sales()

    @app.route('/sales/<int:sale_id>', methods=['GET'])
    def get_sale(sale_id):
        return SaleController.get_sale(sale_id)
    
    @app.route('/seller', methods=['POST'])
    def create_seller():
        return SellerController.create_seller()