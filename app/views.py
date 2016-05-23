from app import app
from flask import render_template, flash, redirect

from .forms import ReservationForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="My Restaurant")

@app.route('/make_reservation', methods=['GET', 'POST'])
def make_reservation():
    form = ReservationForm()
    if form.validate_on_submit():
        flash("Reservation created!")
        return redirect('/index')
    return render_template('make_reservation.html', title="Make Reservation", form=form)
