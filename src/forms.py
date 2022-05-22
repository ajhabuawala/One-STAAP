from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, DateField, DecimalField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class SearchForm(FlaskForm):
    from_destination = StringField("From:", validators=[DataRequired()], render_kw={"placeholder": "Country, City or Aiport"})
    to_desination = StringField("To:", validators=[DataRequired()], render_kw={"placeholder": "Country, City or Aiport"})
    shipment_weight = DecimalField("Weight(kg)", validators=[DataRequired()])
    date_of_shipment = DateField(validators=[DataRequired()])
    prefered_mot = SelectField('Preferred MOT:', choices=['Container', 'Air', 'Ground Transport'])
    submit = SubmitField("Request Quote")


class RegistrationForm(FlaskForm):

    username = StringField("Username",
                           validators=[DataRequired(), Length(min=2, max=9)])

    email = StringField("Email Address",
                        validators=[DataRequired(), Email()])

    password = PasswordField("Password", validators=[DataRequired()])

    confirm_password = PasswordField("Confirm Password",
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):

    email = StringField("Email Address",
                        validators=[DataRequired(), Email()])

    password = PasswordField("Password", validators=[DataRequired()])

    remember = BooleanField("Remember Me")

    submit = SubmitField("Login")
