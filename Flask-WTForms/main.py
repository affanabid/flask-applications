from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(message='Enter valid email')])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=3, max=10)])
    submit = SubmitField(label='Log In')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        print(form.email.data)
        return render_template('success.html')
    # elif form.validate_on_submit() == False:
    #     return render_template('denied.html')
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
