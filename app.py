from flask import Flask, render_template

app = Flask(__name__, static_folder="public", template_folder="public")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gamepage")
def gamepage():
    return render_template("gamepage.html")

@app.route("/popular")
def popular():
    return render_template("popular.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/profile-settings")
def profile_settings():
    return render_template("profileSettings.html")

@app.route("/sign")
def sign():
    return render_template("sign.html")

@app.route("/tester")
def tester():
    return render_template("tester.html")

if __name__ == "__main__":
    app.run(debug=True)
