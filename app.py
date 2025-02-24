from flask import Flask, render_template

app = Flask(__name__)

#### Start server by typing 'python app.py' in the terminal
@app.route("/")
def index():
    active_index = "active"
    return render_template("index.html", active_index=active_index)

@app.route("/menu")
def menu():
    active_menu = "active"
    return render_template("menu.html", active_menu=active_menu)

@app.route("/contact")
def contact():
    active_contact = "active"
    return render_template("contact.html", active_contact=active_contact)

if __name__ == "__main__":
    app.run(debug=True)