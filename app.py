from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load variabel lingkungan dari file my .env ini
load_dotenv()

app = Flask(__name__)

# Dapatkan nilai variabel lingkungan menggunakan os.getenv()
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Divisions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

class Employess(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.BigInteger, unique=True, nullable=False)
    address = db.Column(db.String(120), nullable=False)
     # Tambahkan kolom kunci asing (foreign key) untuk menghubungkan dengan tabel Divisions
    division_id = db.Column(db.Integer, db.ForeignKey('divisions.id'), nullable=False)
     # Definisikan relasi antara tabel Employees dan tabel Divisions
    division = db.relationship('Divisions', backref='employees', lazy=True)


# ------------------- CREATE EMPLOYEE (POST) -------------------------------
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
        existing_id = Employess.query.filter_by(id=data['id']).first()
        existing_phone = Employess.query.filter_by(phone=data['phone']).first()

        if existing_id :
            return jsonify({'message': 'Id already exists!', 'code':400})
        
        if existing_phone :
            return jsonify({'message': 'Number phone already exists!', 'code':400})

        # Cek apakah ID divisi ada di database
        existing_division = Divisions.query.get(division_id)
        if not existing_division:
            return jsonify({'message': 'Division not found!'}), 404


        new_employee = Employess(id=id, name=name, email=email, phone=phone, 
                                 address=address, division_id=division_id)
        db.session.add(new_employee)
        db.session.commit()

        return jsonify({'message': 'Employee created successfully!', 'data' : data}), 201

# ---------------------- GET ALL EMPLOYEE (GET) -------------------------------





# --------------------- CREATE DIVISION (POST) -------------------------------
@app.route('/divisions', methods=['POST'])
def create_division():
    with app.app_context():
        data = request.get_json()
        id = data['id']
        name = data['name']

        existing_id = Employess.query.filter_by(id=data['id']).first()
        existing_name = Employess.query.filter_by(name=data['name']).first()

        if existing_id :
            return jsonify({'message': 'Id already exists!', 'code':400})
        
        if existing_name :
            return jsonify({'message': 'Name already exists!', 'code':400})

        new_division = Divisions(id=id,name=name)
        db.session.add(new_division)
        db.session.commit()

        return jsonify({'message': 'Division created successfully!', 'division_id': new_division.id}), 201


if __name__ == '__main__':
    # Pindahkan db.create_all() ke dalam blok ini, sehingga hanya dipanggil sekali saat aplikasi dijalankan.
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)
