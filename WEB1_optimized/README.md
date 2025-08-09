# DisetekSolution - WEB1

Proyecto Flask mínimo para la empresa DisetekSolution (reserva de almacenes).

## Estructura
- app.py
- models.py
- forms.py
- database.py
- config.py
- requirements.txt
- static/
  - css/style.css
  - js/main.js
  - img/ (hero.jpg, warehouse1.jpg, warehouse2.jpg, warehouse3.jpg, logo.png)
- templates/
  - base.html, index.html, warehouses.html, warehouse_detail.html, contact.html, 404.html
- data/ (base de datos SQLite creada en tiempo de ejecución)
- java/WarehouseClient.java (opcional)

## Ejecutar localmente
1. Crear virtualenv: `python -m venv venv && source venv/bin/activate` (Windows: `venv\Scripts\activate`)
2. Instalar: `pip install -r requirements.txt`
3. Ejecutar: `python app.py`
4. Abrir `http://127.0.0.1:5000/`

## Despliegue en Render
- Subir a GitHub y conectar Render.
- Comando de start: `gunicorn app:app`
- Añadir variable `SECRET_KEY` en ENV vars de Render.

