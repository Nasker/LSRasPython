from flask import Flask, jsonify, render_template
import adafruit_dht
import board
import RPi.GPIO as GPIO

DHT_PIN = board.D18
RELAY_PIN = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)


app = Flask(__name__)

# Initialize the DHT device
dhtDevice = adafruit_dht.DHT11(DHT_PIN)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/sensor')
def sensor_data():
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        return jsonify({'temperature': temperature_c, 'humidity': humidity})
    except RuntimeError as error:
        return jsonify({'error': str(error)})


@app.route('/api/toggle_relay', methods=['POST'])
def toggle_relay():
    GPIO.output(RELAY_PIN, not GPIO.input(RELAY_PIN))
    print('Relay toggled')
    return 'Relay toggled'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
