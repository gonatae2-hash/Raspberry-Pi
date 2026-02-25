from flask import Flask, request, render_template

app = Flask(__name__)

# 전역 변수에 저장 (ESP32에서 GET으로 온 데이터 저장)
temperature = "--"
humidity = "--"

@app.route('/products/arduino')
def receive_data():
    global temperature, humidity
    t = request.args.get('temperature')
    h = request.args.get('humidity')
    if t:
        temperature = t
    if h:
        humidity = h
    return "OK", 200

@app.route('/')
def index():
    return render_template('index.html', temperature=temperature, humidity=humidity)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)