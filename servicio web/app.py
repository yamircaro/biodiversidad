from flask import Flask, jsonify

app = Flask(__name__)

# Datos dummy de biodiversidad
biodiversidad_data = [
    {"id": 1, "nombre": "Reserva Natural Sogamoso", "especie_dominante": "Orquídeas", "ubicación": "Sogamoso"},
    {"id": 2, "nombre": "Parque Natural Iguaque", "especie_dominante": "Frailejones", "ubicación": "Villa de Leyva"}
]

# Datos dummy de minería
mineria_data = [
    {"id": 1, "mina": "Mina de Sal de Nemocón", "tipo_mineral": "Sal", "ubicación": "Nemocón"},
    {"id": 2, "mina": "Mina de Carbón de Paipa", "tipo_mineral": "Carbón", "ubicación": "Paipa"}
]

@app.route('/biodiversidad', methods=['GET'])
def get_biodiversidad():
    return jsonify(biodiversidad_data)

@app.route('/mineria', methods=['GET'])
def get_mineria():
    return jsonify(mineria_data)

if __name__ == '__main__':
    app.run(debug=True)
