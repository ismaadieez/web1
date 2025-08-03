from flask import Flask, render_template, request, redirect
from datetime import datetime
import os
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

ARCHIVO_SUGERENCIAS = "sugerencias.txt"

# ========= CONFIGURACIÓN DE EMAIL =========
EMAIL_DESTINO = "weboficialismaadieez@gmail.com"
EMAIL_REMITENTE = "ismasen1983@gmail.com"            # ← CAMBIA ESTO
EMAIL_PASSWORD = "ismasen2006"               # ← CAMBIA ESTO
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def enviar_correo(sugerencia):
    try:
        msg = MIMEText(f"Nueva sugerencia:\n\n{sugerencia}")
        msg['Subject'] = "Nueva sugerencia recibida"
        msg['From'] = EMAIL_REMITENTE
        msg['To'] = EMAIL_DESTINO

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_REMITENTE, EMAIL_PASSWORD)
            server.send_message(msg)

    except Exception as e:
        print("Error enviando correo:", e)

def obtener_sugerencia():
    if not os.path.exists(ARCHIVO_SUGERENCIAS):
        return "Aún no hay sugerencias. ¡Sé el primero!"
    with open(ARCHIVO_SUGERENCIAS, "r", encoding="utf-8") as f:
        lineas = [line.strip() for line in f if line.strip()]
    return lineas[0] if lineas else "Aún no hay sugerencias. ¡Sé el primero!"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        texto = request.form.get("sugerencia", "").strip()
        if texto:
            with open(ARCHIVO_SUGERENCIAS, "a", encoding="utf-8") as f:
                f.write(texto + "\n")
            enviar_correo(texto)
        return redirect("/")

    hoy = datetime.now()
    dia = hoy.day

    if dia == 31:
        contenido = '''
            📸 <strong>¡Sígueme en Instagram!</strong><br><br>
            <a href="https://www.instagram.com/ismaadieez/?next=%2F" target="_blank">@ismaadieez</a>
        '''
    else:
        tipo_dia = dia % 5
        if tipo_dia == 1:
            frases = [
                "“El que ha naufragado tiembla incluso ante las olas tranquilas.” — Ovidio",
                "“Podrán cortar todas las flores, pero no podrán detener la primavera.” — Neruda",
                "“Vivo sin vivir en mí...” — Santa Teresa",
                "“Tengo en mí todos los sueños del mundo.” — Pessoa",
                "“No hay noche tan larga que no encuentre el día.” — Shakespeare"
            ]
            contenido = f"✒️ <em>{frases[dia % len(frases)]}</em>"
        elif tipo_dia == 2:
            frases2 = [
                'Mama t quiero',
                'Papa t quiero',
                'Hermana t quiero',
                'Viva España',
                'Pedro Sánchez cabrón',
                '“Cuando creíamos que teníamos todas las respuestas, cambiaron todas las preguntas.” — Benedetti',
            ]
            contenido = f"✒️ <em>{frases2[dia % len(frases2)]}</em>"
        elif tipo_dia == 3:
            contenido = f"📝 Sugerencia real enviada:<br>“{obtener_sugerencia()}”"
        elif tipo_dia == 4:
            imagenes = [
                "https://i.imgur.com/B5F7g8p.jpg",
                "https://i.imgur.com/X0ZK9rM.jpg",
                "https://i.imgur.com/kjYOd3O.jpg",
                "https://i.imgur.com/QH1SY6L.jpg"
            ]
            img = imagenes[dia % len(imagenes)]
            contenido = f'<img src="{img}" alt="meme" style="max-width:100%; border-radius:10px;">'
        else:
            contenido = '''
            🎞️ <strong>Animación del día:</strong><br><br>
            <div style="width:100px;height:100px;background:red;animation: girar 2s linear infinite; border-radius:50%; margin:0 auto;"></div>
            <style>
              @keyframes girar {
                from {transform: rotate(0deg);}
                to {transform: rotate(360deg);}
              }
            </style>
            '''

    return render_template("index.html", contenido=contenido)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
