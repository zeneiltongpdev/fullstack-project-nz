from src.config.data_base import db
from datetime import datetime

class Seller(db.Model):
    __tablename__ = 'sellers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    status = db.Column(db.String(20), nullable=False, default='Ativo')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, name, email, status='Ativo'):
        self.name = name
        self.email = email
        self.status = status
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    @classmethod
    def from_domain(cls, seller_domain):
        return cls(
            name=seller_domain.name,
            email=seller_domain.email,
            status=seller_domain.status
        )

    def to_domain(self):
        return PureSellerDomain(
            name=self.name,
            email=self.email,
            status=self.status
        )