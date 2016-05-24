import datetime

from app import app
from flask import render_template, flash, redirect, session, g

from .forms import ReservationForm, ShowReservationsOnDateForm
from .controller import create_reservation
from .models import Table, Reservation

RESTAURANT_OPEN_TIME=16
RESTAURANT_CLOSE_TIME=22


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="My Restaurant")

@app.route('/make_reservation', methods=['GET', 'POST'])
def make_reservation():
    form = ReservationForm()
    if form.validate_on_submit():
        reservation_date = datetime.datetime.combine(form.reservation_datetime.data.date(), datetime.datetime.min.time())
        if form.reservation_datetime.data < reservation_date + datetime.timedelta(hours=RESTAURANT_OPEN_TIME) or \
        form.reservation_datetime.data > reservation_date + datetime.timedelta(hours=RESTAURANT_CLOSE_TIME):
            flash("The restaurant is closed at that hour!")
            return redirect('/make_reservation')
        reservation = create_reservation(form)
        if reservation:
            flash("Reservation created!")
            return redirect('/index')
        else:
            flash("That time is taken!  Try another time")
            return redirect('/make_reservation')
    return render_template('make_reservation.html', title="Make Reservation", form=form)

@app.route('/show_tables')
def show_tables():
    tables = Table.query.all()
    return render_template('show_tables.html', title="Tables", tables=tables)

@app.route('/show_reservations', methods=['GET', 'POST'])
@app.route('/show_reservations/<reservation_date>', methods=['GET', 'POST'])
def show_reservations(reservation_date = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")):
    form = ShowReservationsOnDateForm()
    if form.validate_on_submit():
        res_date = datetime.datetime.strftime(form.reservation_date.data, "%Y-%m-%d")
        return redirect('/show_reservations/' + res_date)
    res_date = datetime.datetime.strptime(reservation_date, "%Y-%m-%d")
    reservations = Reservation.query.filter(Reservation.reservation_time >= res_date,
                                            Reservation.reservation_time < res_date + datetime.timedelta(days=1)).all()

    return render_template('show_reservations.html', title="Reservations", reservations=reservations, form=form)

@app.route('/admin')
def admin():
    return render_template('admin.html', title="Admin")