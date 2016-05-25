from flask.ext.wtf import Form
from wtforms import StringField, DateTimeField, IntegerField, DateField, SelectField

from .models import MAX_TABLE_CAPACITY

from datetime import datetime


class ReservationForm(Form):
    guest_name = StringField('guest_name')
    guest_phone = StringField('guest_phone')
    num_guests = IntegerField('num_guests')
    reservation_datetime = DateTimeField('reservation_datetime', default=datetime.now())

class ShowReservationsOnDateForm(Form):
    reservation_date = DateField('reservation_date', default=datetime.now())

class AddTableForm(Form):
    table_capacity = SelectField('table_capacity', coerce=int, choices = [(x, x) for x in range(1, MAX_TABLE_CAPACITY)])