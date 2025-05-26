from src.Infrastructure.Model.user import User
from src.config.data_base import db 
from src.Infrastructure.http.whats_app import whats_app_api

class UserService:
    @staticmethod
    def create_user(name, email, password, cnpj, phone, is_active=False):
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            raise ValueError("O email já está existe.")

        user = User(  
            name=name,
            email=email,
            password=password,
            cnpj=cnpj,
            phone=phone,
            is_active=is_active
        )

        db.session.add(user)
        db.session.commit()
        return user