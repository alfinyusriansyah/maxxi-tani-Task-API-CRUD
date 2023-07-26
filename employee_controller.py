from flask import request, jsonify
from app import app, db
from model import Employees, Divisions

# ------------------------ Create Employee -----------------------------------
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
        if Employees.query.filter_by(id=data['id']).first() :
            return jsonify({'message': 'Id already exists!', 'code':400})
        
        if Employees.query.filter_by(phone=data['phone']).first() :
            return jsonify({'message': 'Number phone already exists!', 'code':400})

        # Cek apakah ID divisi ada di database
        if not Divisions.query.get(division_id):
            return jsonify({'message': 'Division not found!'}), 404

        new_employee = Employees(id=id, name=name, email=email, phone=phone, 
                                 address=address, division_id=division_id)
        db.session.add(new_employee)
        db.session.commit()

        return jsonify({'message': 'Employee created successfully!', 'data' : data}), 201


# ------------------------ Get All Employee -----------------------------------
@app.route("/employees", methods=['GET'])
def get_all_employee ():
    employees = Employees.query.order_by(Employees.name,Employees.id ).all()

    employee_list = []
    for employee in employees:
        data_employee = {
            "id" : employee.id,
            'name': employee.name,
            'email': employee.email,
            'phone': employee.phone,
            'address': employee.address,
            'division_name': employee.division.name
        }
        employee_list.append(data_employee)
    return jsonify(employee_list), 200

# ------------------------ Get All Employee -----------------------------------
@app.route("/employees/<int:id>", methods=["PUT"])
def update_employee_byid(id):
    with app.app_context():
        data = request.get_json()
        name = data['name']
        email = data['email']
        phone = data['phone']
        address = data['address']
        division_id = data['division_id']

        existing_employee = Employees.query.filter_by(id=id).first()
        print(existing_employee)
        if not existing_employee:
            return jsonify({'massage': 'id Employee not found!'}),404
        
        existing_division = Divisions.query.get(division_id)
        print(existing_division)
        if not existing_division:
            return jsonify({'message' : 'id Division not found!'}), 404
        
            # Update data employee
        existing_employee.name = name
        existing_employee.email = email
        existing_employee.phone = phone
        existing_employee.address = address
        existing_division.id = id
        db.session.commit()

        return jsonify({'message': 'Employee updated successfully!'}), 200
    

