from flask import request, jsonify
from app import app, db
from model import Employees, Divisions

@app.route('/employees', methods=['POST'])
def create_employee():
    with app.app_context():
        data = request.get_json()
        id = data['id']
        name = data['name']
        email = data['email']
        phone = data['phone']
        address = data['address']
        division_id = data['division_id']

        # Cek apakah id dan title sudah ada di database
        existing_id = Employees.query.filter_by(id=data['id']).first()
        existing_phone = Employees.query.filter_by(phone=data['phone']).first()

        if existing_id :
            return jsonify({'message': 'Id already exists!', 'code':400})
        
        if existing_phone :
            return jsonify({'message': 'Number phone already exists!', 'code':400})

        # Cek apakah ID divisi ada di database
        existing_division = Divisions.query.get(division_id)
        if not existing_division:
            return jsonify({'message': 'Division not found!'}), 404

        new_employee = Employees(id=id, name=name, email=email, phone=phone, 
                                 address=address, division_id=division_id)
        db.session.add(new_employee)
        db.session.commit()

        return jsonify({'message': 'Employee created successfully!', 'data' : data}), 201
