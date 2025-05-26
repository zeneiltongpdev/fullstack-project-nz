from flask import Flask, render_template
from src.config.config import Config  
from src.config.data_base import db, init_db  
from src.routes import init_routes
from flask_jwt_extended import JWTManager
from flask_cors import CORS  # ← Importe o CORS

# AQUI você torna /uploads público, servindo arquivos da pasta src/uploads
app = Flask(
    __name__,
    template_folder="src/Infrastructure/templates",
    static_url_path='/uploads',
    static_folder='src/uploads'
)

CORS(app)
app.config.from_object(Config) 

print("Banco de dados conectado em:", app.config["SQLALCHEMY_DATABASE_URI"])

init_routes(app)
jwt = JWTManager(app)
db.init_app(app)

if __name__ == "__main__":
    init_db(app) 
    print("Rotas registradas:")
    for rule in app.url_map.iter_rules():
        print(rule)

    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)
