from db import db

class SupplierModel(db.Model):
    __tablename__ = 'suppliers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    cpf = db.Column(db.Integer, nullable=False,unique=True)
    hostname = db.Column(db.String,nullable=False,unique=True)
    model = db.Column(db.String,nullable=False)
    mac_adress = db.Column(db.String,nullable=False,unique=True)
    area = db.Column(db.String,nullable=False)
    antivirus = db.Column(db.String,nullable=False)
    update = db.Column(db.String,nullable=False)
    company = db.Column(db.String, nullable=False)
    email = db.Column(db.String,nullable=False)

    def __init__(self, name,cpf,hostname,model,mac_adress,area,antivirus,update,company,email):
        self.name = name 
        self.cpf = cpf
        self.hostname = hostname
        self.model = model
        self.mac_adress = mac_adress
        self.area = area
        self.antivirus = antivirus
        self.update = update
        self.company = company
        self.email = email
    
    def __repr__(self, ):
        return f'SupplierModel(name={self.name}, company={self.company}, area ={self.area})'

    def json(self, ):
        return {
            'name': self.name,
            'cpf': self.cpf,
            'hostname': self.hostname,
            'model': self.model,
            'mac_adress': self.mac_adress,
            'area': self.area,
            'antivirus': self.antivirus,
            'update': self.update,
            'company': self.company,
            'email': self.email
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    def save_to_db(self, ):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        