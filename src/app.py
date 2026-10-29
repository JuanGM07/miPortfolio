from pathlib import Path

from flask import Flask, render_template, request, send_file

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

@app.route("/proyectos/clusterclient")
def clusterclient():
    return render_template("clusterclient.html")

@app.route("/proyectos/industrial-io-adapter")
def industrial_io_adapter():
    return render_template("industrial_io_adapter.html")

@app.route("/proyectos/priority-display")
def priority_display():
    return render_template("priority_display.html")

@app.route("/models/industrial-io-adapter.glb")
def industrial_io_adapter_model():
    compressed = request.accept_encodings["gzip"] > 0
    model_path = Path(app.static_folder) / "images" / "Industrial_IO_Adapter.optimized.glb"
    if compressed:
        model_path = model_path.with_suffix(model_path.suffix + ".gz")

    response = send_file(
        model_path,
        mimetype="model/gltf-binary",
        conditional=False,
        etag=True,
        max_age=86400,
    )
    response.vary.add("Accept-Encoding")
    if compressed:
        response.headers["Content-Encoding"] = "gzip"
    return response

@app.route("/models/priority-display.glb")
def priority_display_model():
    compressed = request.accept_encodings["gzip"] > 0
    model_path = Path(app.static_folder) / "images" / "PriorityDisplay.glb"
    if compressed:
        model_path = model_path.with_suffix(model_path.suffix + ".gz")

    response = send_file(
        model_path,
        mimetype="model/gltf-binary",
        conditional=False,
        etag=True,
        max_age=86400,
    )
    response.vary.add("Accept-Encoding")
    if compressed:
        response.headers["Content-Encoding"] = "gzip"
    return response

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

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
