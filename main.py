from flask import Flask, render_template, request, redirect, session

app = Flask("Trendsphere")

@app.route("/")
def accueil():
    return render_template("index.html")




@app.route("/register", methods=["GET", "POST"])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        msg = 'You have successfully registered!'
    return render_template("register.html", msg=msg)



# Lance l'application
if __name__ == "__main__":
    app.run("0.0.0.0", port=3904)