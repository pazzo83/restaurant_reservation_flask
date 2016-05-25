from flask.ext.wtf import Form
from wtforms import StringField, DateTimeField, IntegerField, DateField, SelectField
from wtforms.validators import DataRequired
from .models import MAX_TABLE_CAPACITY

from datetime import datetime


class ReservationForm(Form):
    guest_name = StringField('guest_name', validators=[DataRequired()])
    guest_phone = StringField('guest_phone', validators=[DataRequired()])
    num_guests = SelectField('num_guests', coerce=int, choices = [(x, x) for x in range(1, MAX_TABLE_CAPACITY)])
    reservation_datetime = DateTimeField('reservation_datetime', default=datetime.now(),
                                         validators=[DataRequired()])

class ShowReservationsOnDateForm(Form):
    reservation_date = DateField('reservation_date', default=datetime.now())

class AddTableForm(Form):
    table_capacity = SelectField('table_capacity', coerce=int, choices = [(x, x) for x in range(1, MAX_TABLE_CAPACITY)])