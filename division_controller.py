from flask import request, jsonify
from app import app
from database import db
from model import Divisions


@app.route("/divisions", methods=['POST'])
def create_division():
    data = request.get_json()
    id = data['id']
    name = data['name']

    if Divisions.query.filter_by(id = data['id']).first():
        return({'message':'Id already Exist'}), 400
    
    if Divisions.query.filter_by(name = data['name']).first():
        return({'message':'Division Name already exist'}), 400
    
    new_division = Divisions(id=id, name=name)
    db.session.add(new_division)
    db.session.commit()

    return jsonify({'message': 'Division created successfully!', 'data' : data}), 201