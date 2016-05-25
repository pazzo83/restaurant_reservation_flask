# Restaurant Reservation System

This is a simple restaurant reservation system built in Flask & Python

## Installation Requirements
This application requires Flask, the Flask SQL Alchemy extension (which installs SQL Alchemy), and the WTForms package

Flask:
```
pip install Flask
```

Flask SQL Alchemy
```
pip install Flask-SQLAlchemy
```

WTForms
```
pip install WTForms
```

## Running the application
Simply run "run.py", this will start the local web server.

## Admin section
To access the admin portion of the application, go to /admin.

## Notes
Metrics:
* Table utilization on the given day
* Reservation slot utilization (number of reservations on a given day vs number of possible reservations)

Additional metrics to gather:
* Since we are tracking guests who book a reservation, we can build a statistical profile of that guest (e.g. how often they dine, how big their parties are, etc)
* Study which tables are booked more frequently and at which times

Additional Features to add:
* More form validation
* A better date/time picker for forms
* More dynamic tables, sorting, etc on the Admin side for studying reservations and table utilization
* The ability to delete reservations and tables
* A multi-restaurant interface (so you'd need a restaurant table to track that)
* Obviously a better visual design
* Not yet displaying form validation error messages

Trade-Offs
* I am using a set difference to determine which tables of a given capacity are free, but this disrupts my way of trying to efficiently seat each guest.  In other words, for a given reservation, I want to associate that reservation with the table with the closest capacity to the number of guests in that party.
* I am using DateTimes to store the reservation times, so this requires some additional work for dealing with strictly date ranges (as opposed to storing a date and a time separately)
* I'm only tracking Guests by name right now, so I need to build something a bit more complex - probably a login/profile type set up.
* Using Flask / SQL Alchemy vs Django - More work required to put the application together, however you have more flexibility with how you want to structure things.  Using SQL Alchemy, you have a lot of freedom with how you want to map Python objects to database tables.

## Table design
Guest
* ID - Primary Key
* name - String
* phone_number - String

Table
* ID - Primary Key
* Capacity - Integer

Reservation
* ID - Primary Key
* guest_id - Foreign Key(Guest)
* table_id - Foreign Key(Table)
* num_guests - Integer
* reservation_time - DateTime

## Misc
Assumed reservation length - 1 hour (see app/models.py)
Restaurant opening time - 4pm
Restaurant closing time - 10pm (see app/views.py)
