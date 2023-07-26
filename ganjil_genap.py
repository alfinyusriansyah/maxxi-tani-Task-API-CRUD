from flask import Flask, request, jsonify



app = Flask(__name__)


@app.route('/numbers/<int:number>', methods=['POST'])
def ganjil(number) :
    if number % 2 == 0 :
        return jsonify({'message': 'genap', 'data' : number})
    
    return jsonify({'message': 'hasil ganjil', 'data' : number}), 201


if __name__ == '__main__':
    # Pindahkan db.create_all() ke dalam blok ini, sehingga hanya dipanggil sekali saat aplikasi dijalankan.
    app.run(debug=True, port=8000)