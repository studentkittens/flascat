from flask_login import LoginManager, UserMixin, AnonymousUser, login_user, logout_user
from flask import flash, render_template, redirect, url_for, session


class Anonymous(AnonymousUser):
    name = u"Anonymous"


class User(UserMixin):
    def __init__(self, name, id, active=True, pwd='hello_world'):
        self.name = name
        self.id = id
        self.active = active
        self.pwd = pwd

    def is_active(self):
        return self.active


# Available users
USERS = {
    1: User(u"Elch", 1, pwd='wald'),
    2: User(u"Kitteh", 2, pwd='baum'),
    3: User(u"Alois", 3, pwd='tempo')
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
        password = request.form["password"]

        userobject = None
        for user in USERS.values():
            if user.name == username and password == user.pwd:
                userobject = user

        if userobject is not None:
            remember = request.form.get("remember", "no") == "yes"
            if login_user(userobject, remember=remember):
                session['logged_in'] = userobject
                flash("Logged in!")
                return redirect(url_for("show_entries"))
            else:
                flash("Sorry, but you could not log in.")
        else:
            flash(u"Invalid username/password.")
    return render_template("login.html")


def do_logout(request):
    logout_user()
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


def setup(app):
    login_manager.setup_app(app)
