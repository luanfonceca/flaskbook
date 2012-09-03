from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Rodou maluco!111!!"

if __name__ == "__main__":
    app.run()