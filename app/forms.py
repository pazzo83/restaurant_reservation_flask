from flask.ext.wtf import Form
from wtforms import StringField, DateTimeField


class ReservationForm(Form):
    guest_name = StringField('guest_name')
    reservation_datetime = DateTimeField('reservation_datetime')