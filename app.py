from flask import Flask
from dotenv import load_dotenv
import os

# Load variabel lingkungan dari file my .env
load_dotenv()

app = Flask(__name__)

# Dapatkan nilai variabel lingkungan menggunakan os.getenv()
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Pindahkan definisi route ke file controller.py
from employee_controller import *

# Pindahkan db.create_all() ke dalam blok ini, sehingga hanya dipanggil sekali saat aplikasi dijalankan.
with app.app_context():
    from database import db
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=8000)
