from flask import request
from flask_restx import Resource, fields

from models.supplier import SupplierModel
from schemas.supplier import SupplierSchema

from server.instance import server

supplier_ns = server.supplier_ns

supplier_schema = SupplierSchema()
supplier_list_schema = SupplierSchema(many=True)

ITEM_NOT_FOUND = 'Supplier not found.'

item = supplier_ns.model('Supplier',{
    'name': fields.String(description= 'Name'),
    'cpf': fields.Integer(default=0),
    'hostname': fields.String(description= 'hostname'),
    'model': fields.String(description= 'model'),
    'mac_adress': fields.String(description= 'mac_adress'),
    'area': fields.String(description= 'area'),
    'antivirus': fields.String(description= 'antivirus'),
    'update': fields.String(description= 'update'),
    'company': fields.String(description= 'company'),
    'email': fields.String(description= 'email')
})

class Supplier(Resource):
    def get(self, id):
        supplier_data = SupplierModel.find_by_id(id)
        if supplier_data:
            return supplier_schema.dump(supplier_data), 200
        return {'message': ITEM_NOT_FOUND},404
    
    @supplier_ns.expect(item)
    def put(self, id):
        supplier_data = SupplierModel.find_by_id(id)
        supplier_json = request.get_json()

        supplier_data.name = supplier_json['name']
        supplier_data.cpf = supplier_json['cpf']
        supplier_data.hostname = supplier_json['hostname']
        supplier_data.model = supplier_json['model']
        supplier_data.mac_adress = supplier_json['mac_adress']
        supplier_data.area = supplier_json['area']
        supplier_data.antivirus = supplier_json['antivirus']
        supplier_data.update = supplier_json['update']
        supplier_data.company = supplier_json['company']
        supplier_data.email = supplier_json['email']

        supplier_data.save_to_db()
        return supplier_schema.dump(supplier_data),200
    
    def delete(self, id):
        supplier_data = SupplierModel.find_by_id(id)
        if supplier_data:
            supplier_data.delete_from_db()
            return '', 204
        return {'message': ITEM_NOT_FOUND},404
    

class SupplierList(Resource):
    def get(self, ):
        return supplier_list_schema.dump(SupplierModel.find_all()), 200
    
    @supplier_ns.expect(item)
    @supplier_ns.doc('Create an Item')
    def post(self, ):
        supplier_json = request.get_json()
        supplier_data = supplier_schema.load(supplier_json)
        supplier_data.save_to_db()
        return supplier_schema.dump(supplier_data), 201