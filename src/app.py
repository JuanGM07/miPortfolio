from flask import Flask, render_template

app = Flask(__name__)

# Configuraciones de seguridad para producción
app.config.update(
    TEMPLATES_AUTO_RELOAD=True,
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/proyectos/facturdash")
def facturdash():
    return render_template("facturdash.html")

@app.route("/proyectos/databasequery")
def databasequery():
    return render_template("databasequery.html")

@app.route("/proyectos/chatbot")
def chabot():
    return render_template("chatbot.html")

@app.route("/proyectos/sentimentanalysis")
def sentimentanalysis():
    return render_template("sentimentanalysis.html")

@app.route("/faqs")
def faqs():
    return render_template("faqs.html")

@app.route("/sobremi")
def sobremi():
    return render_template("sobremi.html")

@app.errorhandler(404)
def pagina_no_encontrada(e):
    return render_template('404.html'), 404

# Necesario para Vercel
def vercel_handler(request):
    with app.app_context():
        response = app.full_dispatch_request()
    return response

