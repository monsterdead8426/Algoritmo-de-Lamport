from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Reloj lógico local
local_clock = 0
node_name = "Node_A"  # Nombre del nodo (cambia para cada contenedor)

# Función para incrementar el reloj en un evento local
def increment_clock():
    global local_clock
    local_clock += 1
    print(f"{node_name} - Evento local, reloj: {local_clock}")

# Función para actualizar el reloj al recibir un mensaje
def update_clock(received_clock):
    global local_clock
    local_clock = max(local_clock, received_clock) + 1
    print(f"{node_name} - Mensaje recibido, reloj actualizado: {local_clock}")

# Endpoint para recibir mensajes de otros nodos
@app.route('/receive', methods=['POST'])
def receive():
    data = request.json
    received_clock = data.get("clock")
    update_clock(received_clock)
    return jsonify({"status": "success", "local_clock": local_clock})

# Función para enviar un mensaje a otro nodo
def send_message(target_url):
    increment_clock()
    data = {"clock": local_clock}
    response = requests.post(f"http://{target_url}/receive", json=data)
    print(f"{node_name} - Mensaje enviado a {target_url}, reloj: {local_clock}")
    return response.json()

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        node_name = sys.argv[1]
    app.run(host='0.0.0.0', port=5000)
