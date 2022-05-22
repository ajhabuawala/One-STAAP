from flask import Flask, render_template, url_for, flash, redirect, session
from forms import RegistrationForm, LoginForm, SearchForm
from air_c02 import get_co2_data


app = Flask(__name__)
app.config['SECRET_KEY'] = '1234567890'


@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        if form.prefered_mot.data == "Air":
            base_c02 = get_co2_data("plane", 5163, int(form.shipment_weight.data))
            session["HighAirC02"] = int(base_c02 * 0.90)
            session["MediumAirC02"] = int(base_c02 * 0.80)
            session["LowAirC02"] = int(base_c02 * 0.70)
            return redirect(url_for('flight_result'))
        elif form.prefered_mot.data == "Container":
            base_c02 = get_co2_data("ship", 11529, int(form.shipment_weight.data))
            session["HighSeaC02"] = int(base_c02 * 0.90)
            session["MediumSeaC02"] = int(base_c02 * 0.80)
            session["LowSeaC02"] = int(base_c02 * 0.70)
            return redirect(url_for('ship_result'))
    return render_template('search.html', form=form)


@app.route('/airresult', methods=['GET'])
def flight_result():
    high_co2_flight = session["HighAirC02"]
    medium_co2_flight = session["MediumAirC02"]
    low_co2_flight = session["LowAirC02"]
    return render_template("air_result.html", co2_high=high_co2_flight, co2_medium=medium_co2_flight, co2_low=low_co2_flight)


@app.route('/shipresult', methods=['GET'])
def ship_result():
    high_sea_co2 = session["HighSeaC02"]
    medium_sea_co2 = session["MediumSeaC02"]
    low_sea_co2 = session["LowSeaC02"]
    return render_template("ship_result.html", co2_high_sea=high_sea_co2, co2_medium_sea=medium_sea_co2, co2_low_sea=low_sea_co2)


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'purchase@zara.com' and form.password.data == '1234':
            flash(f'Login is successful', 'success')
            return redirect(url_for('search'))
        if form.email.data == 'purchase@hnm.com' and form.password.data == 'hnmisthebest':
            flash(f'Login is successful', 'success')
            return redirect(url_for('search'))
        else:
            flash(f'Login is unsuccessful, Please check username or password', 'danger')

    return render_template('login.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
