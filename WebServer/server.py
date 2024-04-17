from flask import Flask, jsonify, render_template
# import adafruit_dht
# import board

app = Flask(__name__)

# Initialize the DHT device
# dhtDevice = adafruit_dht.DHT11(board.D18)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/sensor')
def sensor_data():
    try:
        temperature_c = 23.0  # dhtDevice.temperature
        humidity = 53.0  # dhtDevice.humidity
        return jsonify({'temperature': temperature_c, 'humidity': humidity})
    except RuntimeError as error:
        return jsonify({'error': str(error)})


@app.route('/api/toggle_relay', methods=['POST'])
def toggle_relay():
    print('Relay toggled')
    return 'Relay toggled'


if __name__ == '__main__':
    app.run(debug=True)
