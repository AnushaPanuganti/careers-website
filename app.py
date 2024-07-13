from flask import Flask, render_template

app = Flask(
    __name__
)  ##when u run this u will get __main__ as name variable has main value for app.py


@app.route("/")
def hello_world():
  return render_template("home.html")


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
