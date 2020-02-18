from flask import render_template, redirect, url_for, request
from application import app, bcrypt, db
from application.forms import RegistrationForm, LoginForm, UpdateAccountForm
from application.models import Users, Recipe
from flask_login import login_user, current_user, logout_user, login_required
import random

@app.route('/')
@app.route('/home')
def home():
        return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    print(form.email.errors)
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)

        user = Users(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, password = hash_pw)

        db.session.add(user)
        db.session.commit()
        login_user(user)

        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

@login_required
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@login_required
@app.route("/recipe")
def recipe():
    recipe=Recipe(title="test")
    return render_template('recipe1.html', title='recipe', recipe=recipe)

@login_required
@app.route("/recipe/random")
def randomRecipe():
    recipe_list = Recipe.query.all()
    return render_template("recipe1.html", recipe=random.choice(recipe_list))

@login_required
@app.route("/account", methods=['GET', 'POST'])
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        current_user.password = bcrypt.generate_password_hash(form.password.data)

        db.session.add(current_user)
        db.session.commit()
        return redirect(url_for('account_updated'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)

@login_required
@app.route("/account/updated", methods=['GET'])
def account_updated():
    return render_template("updatesuccess.html")

@app.route("/account/delete", methods=["GET", "POST"])
@login_required
def account_delete():
    user = current_user.id
    account = Users.query.filter_by(id=user).first()
    logout_user()
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for('register'))
