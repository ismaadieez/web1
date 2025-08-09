from datetime import datetime
from database import db

class Warehouse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    size_m2 = db.Column(db.Float, nullable=False)
    price_per_month = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    image = db.Column(db.String(200), default='static/img/warehouse1.jpg')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Warehouse {self.name}>"

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    warehouse_id = db.Column(db.Integer, db.ForeignKey('warehouse.id'))
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(30), nullable=False)
    message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    warehouse = db.relationship('Warehouse', backref=db.backref('reservations', lazy=True))

    def __repr__(self):
        return f"<Reservation {self.name} - {self.warehouse_id}>"
