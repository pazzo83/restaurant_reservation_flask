import datetime

from app import app, db
from flask import render_template, flash, redirect, session, g

from .forms import ReservationForm, ShowReservationsOnDateForm, AddTableForm
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
        if form.reservation_datetime.data < datetime.datetime.now():
            flash("You cannot book dates in the past")
            return redirect('/make_reservation')
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

@app.route('/show_tables', methods=['GET', 'POST'])
def show_tables():
    form = AddTableForm()

    if form.validate_on_submit():
        table = Table(capacity=int(form.table_capacity.data))
        db.session.add(table)
        db.session.commit()
        flash("Table created!")
        return redirect('/show_tables')

    tables = Table.query.all()
    return render_template('show_tables.html', title="Tables", tables=tables, form=form)

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
    total_slots = len(Table.query.all()) * (RESTAURANT_CLOSE_TIME - RESTAURANT_OPEN_TIME)
    util = (len(reservations) / float(total_slots)) * 100
    return render_template('show_reservations.html', title="Reservations", reservations=reservations, form=form, total_slots=total_slots, utilization=util)

@app.route('/admin')
def admin():
    return render_template('admin.html', title="Admin")

@app.context_processor
def utility_processor():
    def table_utilization(table):
        start_datetime = datetime.datetime.combine(datetime.datetime.date(datetime.datetime.now()), datetime.datetime.min.time())
        end_datetime = start_datetime + datetime.timedelta(days=1)
        num_reservations = len(Reservation.query.filter(Reservation.table==table, Reservation.reservation_time > start_datetime, Reservation.reservation_time < end_datetime).all())
        return (num_reservations / float(RESTAURANT_CLOSE_TIME - RESTAURANT_OPEN_TIME)) * 100

    return dict(table_utilization=table_utilization)