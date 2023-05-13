from flask import Flask, jsonify
from main import teste

app= Flask(__name__)

@app.route('/teste', methods=["GET"])
def get_test():
    return jsonify(teste('img2.jpg'))

app.run()

