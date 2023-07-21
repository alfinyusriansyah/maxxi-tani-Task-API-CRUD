from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load variabel lingkungan dari file .env
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




if __name__ == '__main__':
    # Pindahkan db.create_all() ke dalam blok ini, sehingga hanya dipanggil sekali saat aplikasi dijalankan.
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)
