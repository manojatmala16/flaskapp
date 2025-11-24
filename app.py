from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    # flask's built-in server (for lab/testing only)
    app.run(host="0.0.0.0", port=5000)
    