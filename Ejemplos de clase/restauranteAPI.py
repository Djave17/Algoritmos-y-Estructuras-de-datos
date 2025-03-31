from flask import Flask, request, jsonify

app = Flask(__name__)

menu = {
    "Spaghetti Carbonara": 12.99,
    "Margherita Pizza": 9.99,
    "Caesar Salad": 7.99
}

# Lista global para almacenar los pedidos realizados
orders = []

@app.route('/')
def index():
    return "Bienvenido a la API del restaurante. Usa /order para hacer un pedido."

@app.route('/order', methods=['POST'])
def place_order():
    data = request.get_json()
    dish = data.get('dish')
    
    if dish in menu:
        price = menu[dish]
        order = {"dish": dish, "price": price}
        orders.append(order)  # Se guarda el pedido en la lista global
        # Línea 23: Mensaje que aparecerá en el navegador al ordenar
        response = {
            "message": f"Tu pedido de {dish} ha sido recibido. Precio total: ${price:.2f}"
        }
        return jsonify(response), 200
    else:
        return jsonify({"error": "Plato no encontrado"}), 404

# Nueva función para obtener todos los pedidos realizados
@app.route('/order', methods=['GET'])
def get_orders():
    return jsonify({"orders": orders}), 200

if __name__ == '__main__':
    app.run(debug=True)
