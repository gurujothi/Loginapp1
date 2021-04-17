from flask import Flask, render_template, flash, request
from wtforms import Form, StringField, PasswordField, validators

DEBUG = True 
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '123456'

fixed_user = 'Gurumoorthy'
fixed_password = 'password'

class BITSForm(Form):
    username = StringField('Username:', validators=[
                                              validators.DataRequired()])
    password = PasswordField('Password:', validators=[
                                                  validators.DataRequired()])


@app.route("/", methods=['GET', 'POST'])
def python_form():
    form = BITSForm(request.form)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if form.validate():
#            flash('Username and password entered here is: {} and {}'.format(username, password))
            if username == fixed_user and password == fixed_password:
                flash('Logged IN Successfully')
            else:
                flash('Unsuccessful Login Attempt!! Errored due to Incorrect Username or Password')
        else:
            flash('Unsuccessful Login Attempt. Please make sure you entered Username and Password')

    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run()
