from flask.ext.wtf import Form
from wtforms import StringField, DateTimeField, IntegerField

from datetime import datetime


class ReservationForm(Form):
    guest_name = StringField('guest_name')
    guest_phone = StringField('guest_phone')
    num_guests = IntegerField('num_guests')
    reservation_datetime = DateTimeField('reservation_datetime', default=datetime.now())