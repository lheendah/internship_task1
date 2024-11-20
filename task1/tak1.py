from flask import Flask, jsonify 

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def about():
    return jsonify(message = "This is my first flask task")

if __name__ == '__main__':
    app.run(debug = True)

