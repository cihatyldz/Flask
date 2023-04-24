from flask import Flask, render_template, redirect, url_for, request, abort
from app.controllers import UserLogin, UserLogout, GetCurrentUsername, GetContactList, SaveContactRequest
from app.controllers import MySessionInterface

app = Flask(__name__, template_folder="../templates")
# app.secret_key = b"?039eruif3__"
# app.session_interface = MySessionInterface()


@app.route("/")
def Index():
    username, loginAuth = GetCurrentUsername()
    return render_template("index.html", username=username, login_auth=loginAuth)


@app.route("/contact", methods=["GET", "POST"])
def Contact():
    if request.method == "POST":
        if request.form:
            name = request.form.get("name")
            email = request.form.get("email")
            category = request.form.get("category")
            priority = request.form.get("priority")
            message = request.form.get("message")
            SaveContactRequest(name, email, category, priority, message)
            return  redirect(url_for("Contact"))
    username, loginAuth = GetCurrentUsername()
    return render_template("contact.html", username=username, login_auth=loginAuth)


@app.route("/contactlist")
def ContactList():
    username, loginAuth = GetCurrentUsername()
    contactlist = GetContactList()
    return render_template("contact_list.html", username=username, login_auth=loginAuth, contactlist=contactlist)


@app.route("/login", methods=["GET", "POST"])
def Login():
    if request.method == "POST":
        if request.form:
            if "username" in request.form and "password" == request.form:
                username = request.form["username"]
                password = request.form["password"]
                if UserLogin(username, password):
                    return redirect(url_for("Index"))
                else:
                    return redirect(url_for("Login"))
        abort(400)
    username, loginAuth = GetCurrentUsername()
    return render_template("login.html", username=username, login_auth=loginAuth)


@app.route("/logout")
def Logout():
    if UserLogout():
        return  redirect(url_for("Index"))

#
# @app.route("/hello")
# def Hello():
#     return render_template("hello.html")
#
#
# @app.route("/hello-admin")
# def HelloAdmin():
#     return render_template("hello_admin.html")
#
#
# @app.route("/hello-user/<name>")
# def HelloUser(name):
#     if name.lower() == "admin":
#         return redirect(url_for("HelloAdmin"))
#     return render_template("hello_user.html", username=name)
#
#
# @app.route("/add/<int:number1>/<int:number2>")
# def Add(number1, number2):
#     calculation_result = number1 + number2
#     return render_template("add.html", number1=number1, number2=number2, result=calculation_result)
#
#
# @app.route("/login", methods=['POST', 'GET'])
# def Login():
#     if request.method == 'POST':
#         username = request.form["name"]
#         return redirect(url_for("HelloUser", name=username))
#     return render_template("login.html")
#
#
# @app.route("/student")
# def Student():
#     return render_template("student.html")
#
#
# @app.route("/result", methods=['POST'])
# def Result():
#     ContextData = {
#         'name': request.form["name"],
#         'fizik': request.form["fizik"],
#         'matematik': request.form["matematik"],
#         'kimya': request.form["kimya"],
#     }
#     return render_template("student_result.html", **ContextData)
