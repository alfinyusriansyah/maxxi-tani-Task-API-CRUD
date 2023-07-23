from database import db

class Divisions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.BigInteger, unique=True, nullable=False)
    address = db.Column(db.String(120), nullable=False)
    # Tambahkan kolom kunci asing (foreign key) untuk menghubungkan dengan tabel Divisions
    division_id = db.Column(db.Integer, db.ForeignKey('divisions.id'), nullable=False)
    # Definisikan relasi antara tabel Employees dan tabel Divisions
    division = db.relationship('Divisions', backref='employees', lazy=True)