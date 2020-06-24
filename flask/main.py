# print("Hello W")

# input("Avada Kedavra")

from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get("name", "World")
    return 'Hello, World!'

# @app.route('/time')

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = '4321')
