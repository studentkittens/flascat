from flask_login import LoginManager, UserMixin, AnonymousUser, login_user, logout_user
from flask import flash, render_template, redirect, url_for


class Anonymous(AnonymousUser):
    name = u"Anonymous"


class User(UserMixin):
    def __init__(self, name, id, active=True):
        self.name = name
        self.id = id
        self.active = active

    def is_active(self):
        return self.active


# Available users
USERS = {
    1: User(u"Notch", 1),
    2: User(u"Steve", 2),
    3: User(u"Creeper", 3, False),
}


# Login Manager to handle login field
login_manager = LoginManager()
login_manager.anonymous_user = Anonymous
login_manager.login_view = "login"
login_manager.login_message = u"Please log in to access this page."


@login_manager.user_loader
def load_user(id):
    return USERS.get(int(id))


def do_login(request):
    if request.method == "POST" and "username" in request.form:
        username = request.form["username"]
        if username in USERS.keys():
            remember = request.form.get("remember", "no") == "yes"
            if login_user(USERS.keys()[username], remember=remember):
                flash("Logged in!")
                return redirect(request.args.get("next") or url_for("index"))
            else:
                flash("Sorry, but you could not log in.")
        else:
            flash(u"Invalid username.")
    return render_template("login.html")


def do_logout(request):
    logout_user()
    flash("Logged out.")
    return redirect(url_for("index"))


def setup(app):
    login_manager.setup_app(app)
