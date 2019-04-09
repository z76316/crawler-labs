from flask import Flask, jsonify, request

app = Flask(__name__)

# @app.route("/test")
def crawler(self):
    res = {
        "title": "test",
        "subtitle": "hey hey hey"
    }
    return jsonify(res)

if __name__ == "__main__":
    app.run()