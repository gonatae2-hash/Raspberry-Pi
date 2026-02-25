from flask import Flask, jsonify, request

app = Flask(__name__)

latest_sensor = {"temperature": None, "humidity": None}

# ESP32가 데이터를 보내는 엔드포인트

@app.route('/api/sensor', methods=['POST'])

def receive_sensor():

    global latest_sensor

    data = request.get_json()

    latest_sensor = {

        "temperature": data.get("temperature"),

        "humidity": data.get("humidity")

    }

    print(f"수신: 온도={latest_sensor['temperature']}, 습도={latest_sensor['humidity']}")

    return jsonify({"status": "ok"})

# 저장된 데이터를 확인하는 엔드포인트

@app.route('/api/sensor', methods=['GET'])

def get_sensor():

    return jsonify(latest_sensor)

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
