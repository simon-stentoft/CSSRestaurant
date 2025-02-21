from flask import Flask, render_template

app = Flask(__name__)

#### Start server by typing 'python app.py' in the terminal
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)