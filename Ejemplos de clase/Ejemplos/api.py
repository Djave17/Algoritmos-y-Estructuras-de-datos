from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos de ejemplo
items = [
    {'id': 1, 'Saludo': 'BUENOS DIAS MI GENTE'},
    {'id': 2, 'Saludo': 'Item Dos'},
    {'id': 3, 'Saludo': 'Item Tres'}
]

# Ruta para la raíz
@app.route('/', methods=['GET'])
def home():
    """Devuelve un mensaje de bienvenida en la raíz."""
    return jsonify({'message': 'Bienvenido al ejemplo de API con Flask!. Aló'})

# Ruta para obtener todos los items
@app.route('/items', methods=['GET'])
def get_items():
    """Devuelve la lista completa de items en formato JSON."""
    return jsonify(items)

# Ruta para obtener un item específico por ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """Devuelve un item específico por su ID o un error si no existe."""
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({'error': 'Item not found'}), 404

# Manejo de error 404 (ruta no encontrada)
@app.errorhandler(404)
def not_found(error):
    """Maneja errores 404 y devuelve un mensaje en formato JSON."""
    return jsonify({'error': 'Not found'}), 404

# Manejo de error 500 (error interno del servidor)
@app.errorhandler(500)
def internal_error(error):
    """Maneja errores 500 y devuelve un mensaje en formato JSON."""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)