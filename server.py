from flask import Flask, render_template, request
import datetime
app = Flask(__name__)
today=datetime.datetime.now()
year=today.year()


@app.route("/", methods=["GET", "POST"])
def main_page():
    return render_template("index.html", year=year)

@app.route("/engineeringresume")
def engineering_resume_page():
    return render_template("engineering_resume.html")

@app.route("/codingresume")
def coding_resume_page():
    return render_template("coding_resume.html")

@app.route("/thanks")
def thanks_page():
    return render_template("thanks.html")


if __name__ == "__main__":
    app.run(debug=True)