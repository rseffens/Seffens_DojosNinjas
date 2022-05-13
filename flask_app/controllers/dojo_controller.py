from flask import redirect, render_template, request, redirect
from flask_app import app
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja
from flask_app.controllers import ninja_controller


@app.route("/dojos")
def dojo_new():
    dojos = Dojo.get_dojo()
    return render_template("dojo.html", dojos = dojos)

@app.route("/dojos/create", methods = ["POST"])
def create_dojo():
    data = {
        "name" : request.form["name"]
}
    Dojo.create_dojo(data)
    print(request.form)
    return redirect("/dojos")

# show dojo info

@app.route("/dojos/<int:id>")
def show_dojo(id):
    data = { 
        "id" : id
    }
    dojo = Dojo.get_dojo()
    ninjas = Ninja.get_in_dojo(data)
    return render_template("show.html", dojo=dojo, ninjas = ninjas)
