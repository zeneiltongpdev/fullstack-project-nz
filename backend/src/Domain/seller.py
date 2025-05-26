class PureSellerDomain:
    def __init__(self, name, email, status='Ativo'):
        self.name = name
        self.email = email
        self.status = status
    
    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "status": self.status
        }

    def is_active(self):
        return self.status == 'Ativo'

    def validate(self):
        if not self.name:
            raise ValueError("Nome é obrigatório")
        if not self.email:
            raise ValueError("Email é obrigatório")
        if self.status not in ['Ativo', 'Inativo']:
            raise ValueError("Status deve ser 'Ativo' ou 'Inativo'")