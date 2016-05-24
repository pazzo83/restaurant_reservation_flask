from app import app
from flask import render_template, flash, redirect, session, g

from .forms import ReservationForm
from .controller import create_reservation


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="My Restaurant")

@app.route('/make_reservation', methods=['GET', 'POST'])
def make_reservation():
    form = ReservationForm()
    if form.validate_on_submit():
        reservation = create_reservation(form)
        if reservation:
            flash("Reservation created!")
            return redirect('/index')
        else:
            flash("That time is taken!  Try another time")
            return redirect('/make_reservation')
    return render_template('make_reservation.html', title="Make Reservation", form=form)
