from flask import Flask, render_template, redirect, url_for, flash
from config import Config
from database import db
from models import Warehouse, Reservation
from forms import ContactForm, ReservationForm
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()
        if Warehouse.query.count() == 0:
            sample = [
                Warehouse(name="MiniBox Centro", location="Madrid - Centro", size_m2=3.5, price_per_month=50.0,
                          description="Perfecto para cajas y objetos pequeños.", image="img/warehouse1.jpg"),
                Warehouse(name="Storage Plus", location="Valencia - Polígono", size_m2=12.0, price_per_month=120.0,
                          description="Espacio mediano, ideal para muebles o bicicletas.", image="img/warehouse2.jpg"),
                Warehouse(name="Large Depot", location="Barcelona - Zona Industrial", size_m2=30.0, price_per_month=250.0,
                          description="Gran trastero para muebles y almacenaje a largo plazo.", image="img/warehouse3.jpg")
            ]
            db.session.bulk_save_objects(sample)
            db.session.commit()

    @app.route('/')
    def index():
        featured = Warehouse.query.limit(3).all()
        contact_email = "ismasen1983@gmail.com"
        contact_phone = "674776297"
        return render_template('index.html', featured=featured,
                               email=contact_email, phone=contact_phone)

    @app.route('/almacenes')
    def warehouses():
        all_wh = Warehouse.query.order_by(Warehouse.price_per_month).all()
        return render_template('warehouses.html', warehouses=all_wh)

    @app.route('/almacen/<int:wh_id>', methods=['GET', 'POST'])
    def warehouse_detail(wh_id):
        wh = Warehouse.query.get_or_404(wh_id)
        form = ReservationForm()
        if form.validate_on_submit():
            reservation = Reservation(
                warehouse_id=wh.id,
                name=form.name.data,
                email=form.email.data,
                phone=form.phone.data,
                message=form.message.data
            )
            db.session.add(reservation)
            db.session.commit()
            flash('Reserva enviada. Nos pondremos en contacto contigo.', 'success')
            return redirect(url_for('warehouse_detail', wh_id=wh.id))
            # Nota: aquí podrías enviar email o notificación
        return render_template('warehouse_detail.html', warehouse=wh, form=form)

    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        form = ContactForm()
        if form.validate_on_submit():
            flash('Gracias por contactar. Te responderemos pronto.', 'success')
            return redirect(url_for('contact'))
        company = {
            'name': 'DisetekSolution',
            'email': 'ismasen1983@gmail.com',
            'phone': '674776297'
        }
        return render_template('contact.html', form=form, company=company)

    @app.errorhandler(404)
    def not_found(e):
        return render_template('404.html'), 404

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
