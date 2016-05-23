from app import db

DEFAULT_RESERVATION_LENGTH = 1 # 1 hour

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    phone_number = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<Guest %r>' % (self.name)

class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    capacity = db.Column(db.Integer, index=True)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guest = db.Column(db.Integer, db.ForeignKey('guest.id'))
    table = db.Column(db.Integer, db.ForeignKey('table.id'))
    num_guests = db.Column(db.Integer, index=True)
    reservation_time = db.Column(db.DateTime, index=True)

class ReservationManager(object):
    def create_reservation(self, guest, reservation_datetime):
        pass