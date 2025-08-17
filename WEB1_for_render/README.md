# DisetekSolution - Reserva de Almacenes (Flask)

Proyecto listo para **PyCharm** y **Render**.

## Estructura
```
WEB1_for_render/
├── app.py
├── config.py
├── database.py
├── forms.py
├── models.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── warehouses.html
│   ├── warehouse_detail.html
│   ├── contact.html
│   └── 404.html
└── static/
    ├── css/style.css
    ├── js/main.js
    └── img/{hero.jpg, warehouse1.jpg, warehouse2.jpg, warehouse3.jpg, logo.png}
```

## Ejecutar en local (PyCharm)
1. (Opcional) Crear venv y activarlo.
2. `pip install -r requirements.txt`
3. `python app.py`
4. Abrir `http://127.0.0.1:5000/`

## Desplegar en Render
1. Sube esta carpeta a un repo en GitHub (raíz con `app.py`, `requirements.txt`, `Procfile`).
2. En Render: **New → Web Service**
3. Conecta tu repo.
4. Configuración:
   - **Root Directory**: `.`
   - **Build Command**: *(vacío)* o `pip install -r requirements.txt`
   - **Start Command**: *(vacío, Render usa el Procfile)* o `gunicorn app:app`
5. (Opcional) Variables de entorno: añade `SECRET_KEY` con un valor seguro.
6. Deploy. Listo.

> La app usa SQLite por defecto. Para persistencia larga en Render, considera una base de datos gestionada (Postgres) y define `DATABASE_URL`.
