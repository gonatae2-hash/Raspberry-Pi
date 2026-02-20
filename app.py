from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():

    return "온도: 25.3, 습도: 60.5"

if __name__ == '__main__':

    app.run(debug=True)

