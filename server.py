from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"


# Index - Home/Survey Form 
@app.route("/")
def index():
    return render_template("index.html")


#Process Form - POST
@app.route("/process", methods = ["POST"])
def process_form():
    print(request.form)

    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comment"] = request.form["comment"]

    return redirect("/result")


# Survey Results - display results to user 
@app.route("/result")
def survey_results():
    print(request.form)

    return render_template(
        "result.html",
        name = session["name"],
        location = session["location"],
        language = session["language"],
        comment = session["comment"]
    )


if __name__ == "__main__":
    app.run(debug = True)