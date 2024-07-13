from flask import Flask
app = Flask(__name__)   ##when u run this u will get __main__ as name variable has main value for app.py

@app.route("/")
def hello_world():
  return "Hello,World"
if __name__ == "__main__":
  app.run(host = "0.0.0.0",debug=True)